"""Support for EON Energiemonitor."""
import logging
import re
from typing import Any, Dict, List, Optional, Tuple

import aiohttp
import voluptuous as vol

try:
    from homeassistant.exceptions import ConfigError
except ImportError:
    # HA 2025.4+: ConfigError removed; use HomeAssistantError for YAML setup errors
    from homeassistant.exceptions import HomeAssistantError as ConfigError
from homeassistant.helpers import discovery, issue_registry as ir
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.event import async_track_utc_time_change
from homeassistant.helpers.issue_registry import IssueSeverity
from homeassistant.const import CONF_SCAN_INTERVAL
import homeassistant.util.dt as dt_util

_LOGGER = logging.getLogger(__name__)

DOMAIN = "eon-energiemonitor"

CONF_REGION_CODE = "region_code"
CONF_SCOPE = "scope"
CONF_ALIAS = "alias"

API_BASE_URL = "https://api-energiemonitor.eon.com/"
REQUEST_TIMEOUT = aiohttp.ClientTimeout(total=30)
DASHBOARD_BASE_URL = "https://energiemonitor.bayernwerk.de/"

ISSUE_REGION_NOT_FOUND = "region_not_found"
ISSUE_UPDATE_FAILED = "update_failed"
ISSUE_SCOPE_REGION_NOT_FOUND = "scope_region_not_found"
ISSUE_SCOPE_UPDATE_FAILED = "scope_update_failed"

ENERGY_METRICS = (
    "autarky",
    "secondaryInFeed",
    "energyMix",
    "bio",
    "solar",
    "wind",
    "water",
    "others",
    "domestic",
    "public",
    "industrial",
)

RESERVED_ALIASES = frozenset(
    {
        "status",
        "region",
        "autarky",
        "secondaryinfeed",
        "energymix",
        "bio",
        "solar",
        "wind",
        "water",
        "others",
        "domestic",
        "public",
        "industrial",
    }
)

_ALIAS_PATTERN = re.compile(r"^[a-z0-9_]+$")

ERROR_MESSAGES = {
    "region_not_found": "Region not found",
    "network": "Network error",
    "timeout": "Timeout",
    "invalid_response": "Invalid API response",
    "parse": "Failed to parse data",
    "not_configured": "Not configured",
}


def _validate_region_code(value: str) -> str:
    """Validate region_code from configuration."""
    code = str(value).strip()
    if not code:
        raise vol.Invalid(
            "region_code must not be empty. See README for how to resolve your code."
        )
    if not code.isdigit():
        raise vol.Invalid(
            "region_code must be numeric (not the URL slug). "
            "Resolve via https://api-energiemonitor.eon.com/region-data?regionUrlKey=<slug>"
        )
    return code


def _validate_alias(value: str) -> str:
    """Validate scope alias for entity prefixes."""
    alias = str(value).strip()
    if not alias:
        raise vol.Invalid("scope alias must not be empty.")
    if not _ALIAS_PATTERN.match(alias):
        raise vol.Invalid(
            "scope alias must match ^[a-z0-9_]+$ (lowercase letters, digits, underscore)."
        )
    if alias.lower() in RESERVED_ALIASES:
        raise vol.Invalid(f"scope alias '{alias}' is reserved.")
    return alias


def _validate_scope(scopes: List[dict]) -> List[dict]:
    """Ensure scope aliases are unique."""
    seen: set[str] = set()
    for entry in scopes:
        alias = entry[CONF_ALIAS]
        if alias in seen:
            raise vol.Invalid(f"Duplicate scope alias '{alias}'.")
        seen.add(alias)
    return scopes


SCOPE_ENTRY_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_REGION_CODE): vol.All(cv.string, _validate_region_code),
        vol.Required(CONF_ALIAS): vol.All(cv.string, _validate_alias),
        vol.Optional(CONF_SCAN_INTERVAL): cv.positive_int,
    }
)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_REGION_CODE): vol.All(cv.string, _validate_region_code),
                vol.Optional(CONF_SCAN_INTERVAL, default=5): cv.positive_int,
                vol.Optional(CONF_SCOPE, default=[]): vol.All(
                    cv.ensure_list, [SCOPE_ENTRY_SCHEMA], _validate_scope
                ),
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)


def _async_clear_legacy_issues(hass) -> None:
    """Remove legacy repair issues after a successful legacy update."""
    ir.async_delete_issue(hass, DOMAIN, ISSUE_REGION_NOT_FOUND)
    ir.async_delete_issue(hass, DOMAIN, ISSUE_UPDATE_FAILED)


def _async_clear_scope_issues(hass, alias: str) -> None:
    """Remove repair issues for a scope after a successful update."""
    ir.async_delete_issue(hass, DOMAIN, f"{ISSUE_REGION_NOT_FOUND}_{alias}")
    ir.async_delete_issue(hass, DOMAIN, f"{ISSUE_UPDATE_FAILED}_{alias}")


def _async_manage_legacy_issues(
    hass, region_code: str, last_error: Optional[str]
) -> None:
    """Surface legacy configuration or API problems in Settings → Repairs."""
    if last_error == "region_not_found":
        ir.async_create_issue(
            hass,
            DOMAIN,
            ISSUE_REGION_NOT_FOUND,
            is_fixable=False,
            issue_domain=DOMAIN,
            severity=IssueSeverity.ERROR,
            translation_key=ISSUE_REGION_NOT_FOUND,
            translation_placeholders={"region_code": region_code},
        )
        ir.async_delete_issue(hass, DOMAIN, ISSUE_UPDATE_FAILED)
        return

    if last_error:
        ir.async_create_issue(
            hass,
            DOMAIN,
            ISSUE_UPDATE_FAILED,
            is_fixable=False,
            issue_domain=DOMAIN,
            severity=IssueSeverity.WARNING,
            translation_key=ISSUE_UPDATE_FAILED,
            translation_placeholders={
                "error": ERROR_MESSAGES.get(last_error, last_error),
            },
        )


def _async_manage_scope_issues(
    hass, alias: str, region_code: str, last_error: Optional[str]
) -> None:
    """Surface scope-specific problems without affecting legacy repairs."""
    if last_error == "region_not_found":
        ir.async_create_issue(
            hass,
            DOMAIN,
            f"{ISSUE_REGION_NOT_FOUND}_{alias}",
            is_fixable=False,
            issue_domain=DOMAIN,
            severity=IssueSeverity.ERROR,
            translation_key=ISSUE_SCOPE_REGION_NOT_FOUND,
            translation_placeholders={"alias": alias, "region_code": region_code},
        )
        ir.async_delete_issue(hass, DOMAIN, f"{ISSUE_UPDATE_FAILED}_{alias}")
        return

    if last_error:
        ir.async_create_issue(
            hass,
            DOMAIN,
            f"{ISSUE_UPDATE_FAILED}_{alias}",
            is_fixable=False,
            issue_domain=DOMAIN,
            severity=IssueSeverity.WARNING,
            translation_key=ISSUE_SCOPE_UPDATE_FAILED,
            translation_placeholders={
                "alias": alias,
                "error": ERROR_MESSAGES.get(last_error, last_error),
            },
        )


class EONEnergiemonitorAPI:
    """Representation of the EON Energiemonitor API."""

    def __init__(self, region_code: str):
        """Initialize the API client."""
        self._base_url = API_BASE_URL
        self._region_code = region_code
        self.last_error: Optional[str] = None

    async def _get_json(self, url: str) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
        """Fetch JSON from the API. Returns (data, error_key)."""
        try:
            async with aiohttp.ClientSession(timeout=REQUEST_TIMEOUT) as session:
                async with session.get(url) as resp:
                    if resp.status == 404:
                        return None, "region_not_found"
                    if resp.status != 200:
                        return None, f"http_{resp.status}"
                    data = await resp.json()
        except aiohttp.ClientError:
            return None, "network"
        except TimeoutError:
            return None, "timeout"

        if not isinstance(data, dict):
            return None, "invalid_response"
        return data, None

    async def request_region_info(self) -> Optional[Dict[str, Any]]:
        """Request municipality metadata from region-data API."""
        url = f"{self._base_url}region-data?regionCode={self._region_code}"
        data, error = await self._get_json(url)
        if error:
            _LOGGER.debug("region-data failed for %s: %s", self._region_code, error)
            return None
        _LOGGER.debug("region-data loaded for %s", self._region_code)
        return data

    async def request_data(self) -> Optional[Dict[str, Any]]:
        """Request meter data from the EON Energiemonitor API."""
        self.last_error = None
        url = f"{self._base_url}meter-data?regionCode={self._region_code}"
        data, error = await self._get_json(url)
        if error:
            self.last_error = error
            if error == "region_not_found":
                _LOGGER.error(
                    "Region '%s' not found (HTTP 404). Check region_code.",
                    self._region_code,
                )
            else:
                _LOGGER.error("meter-data failed for %s: %s", self._region_code, error)
            return None
        _LOGGER.debug("meter-data loaded for %s", self._region_code)
        return data


class EONEnergiemonitor(EONEnergiemonitorAPI):
    """Coordinator for EON Energiemonitor sensor data."""

    def __init__(
        self,
        hass,
        region_code: str,
        *,
        alias: Optional[str] = None,
        scan_interval: int = 5,
    ):
        """Initialize EON Energiemonitor."""
        super().__init__(region_code)
        self._hass = hass
        self.alias = alias
        self.scan_interval = scan_interval
        self._data: Dict[str, Dict[str, Any]] = {}
        self._region_info: Dict[str, Any] = {}
        self._update_listeners = []

    @property
    def region_code(self) -> str:
        """Configured region code."""
        return self._region_code

    def get_data(self, name: str) -> Optional[Dict[str, Any]]:
        """Return cached data for a sensor name."""
        return self._data.get(name)

    def get_region_info(self) -> Dict[str, Any]:
        """Return cached region-data API payload."""
        return self._region_info

    def get_region_attributes(self) -> Dict[str, Any]:
        """Return region metadata for sensor attributes and dashboards."""
        if not self._region_info:
            return {"region_code": self._region_code}

        url_key = self._region_info.get("regionUrlKey")
        attrs = {
            "region_code": self._region_info.get("regionCode", self._region_code),
            "region_name": self._region_info.get("regionName"),
            "region_url_key": url_key,
            "latitude": self._region_info.get("latitude"),
            "longitude": self._region_info.get("longitude"),
            "tenant_id": self._region_info.get("tenantId"),
            "coat_of_arms_mime_type": self._region_info.get("coatOfArmsMimeType"),
        }
        if url_key:
            attrs["dashboard_url"] = f"{DASHBOARD_BASE_URL}{url_key}"
        if self.alias:
            attrs["scope_alias"] = self.alias
        return {k: v for k, v in attrs.items() if v is not None}

    def get_status_message(self) -> str:
        """Return a short status label for the status sensor."""
        if not self.last_error:
            return "OK"
        return ERROR_MESSAGES.get(self.last_error, self.last_error)

    async def _fetch_region_info(self) -> None:
        """Load municipality metadata (region-data API)."""
        region_info = await self.request_region_info()
        if region_info:
            self._region_info = region_info

    def _clear_energy_data(self) -> None:
        """Remove cached energy metrics so sensors become unavailable."""
        for key in ENERGY_METRICS:
            self._data.pop(key, None)

    def _manage_issues(self) -> None:
        """Create or clear repair issues for this coordinator."""
        if self.alias:
            if self.last_error:
                _async_manage_scope_issues(
                    self._hass, self.alias, self._region_code, self.last_error
                )
            else:
                _async_clear_scope_issues(self._hass, self.alias)
        elif self.last_error:
            _async_manage_legacy_issues(self._hass, self._region_code, self.last_error)
        else:
            _async_clear_legacy_issues(self._hass)

    async def update(self, *_args) -> bool:
        """Fetch region metadata and meter data."""
        await self._fetch_region_info()

        payload = await self.request_data()
        if payload is None:
            self._clear_energy_data()
            self._set_status_data(ok=False)
            self._manage_issues()
            self._notify_listeners()
            return False

        try:
            self._data = self._prepare_data(payload)
            self.last_error = None
            self._set_status_data(ok=True)
            self._manage_issues()
        except (KeyError, TypeError, ValueError) as err:
            self.last_error = "parse"
            _LOGGER.error("Failed to parse EON Energiemonitor data: %s", err)
            self._clear_energy_data()
            self._set_status_data(ok=False)
            self._manage_issues()
            self._notify_listeners()
            return False

        self._notify_listeners()
        return True

    def _set_status_data(self, ok: bool) -> None:
        """Update the synthetic status entry used by the status sensor."""
        if ok:
            state = "OK"
        elif self.last_error:
            state = self.get_status_message()
        else:
            state = "No data"

        attrs = self.get_region_attributes()
        attrs["last_error"] = self.last_error
        attrs["region_lookup_url"] = (
            f"{API_BASE_URL}region-data?regionCode={self._region_code}"
        )

        self._data["status"] = {
            "state": state,
            "attributes": attrs,
            "unit": None,
        }

        region_name = self._region_info.get("regionName")
        self._data["region"] = {
            "state": region_name,
            "attributes": self.get_region_attributes(),
            "unit": None,
        }

    def _prepare_data(self, payload: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """Map API payload to sensor data."""
        out: Dict[str, Dict[str, Any]] = {}

        if "autarky" in payload:
            out["autarky"] = {
                "state": payload["autarky"],
                "attributes": {},
                "unit": "%",
            }

        if "energyMix" in payload:
            out["energyMix"] = {
                "state": payload["energyMix"],
                "attributes": {},
                "unit": "%",
            }

        consumptions = payload.get("consumptions") or {}
        feed_in = payload.get("feedIn") or {}

        if "secondaryInFeed" in payload:
            secondary_value = payload["secondaryInFeed"]
        elif consumptions.get("total") is not None and feed_in.get("total") is not None:
            secondary_value = float(consumptions["total"]) - float(feed_in["total"])
        else:
            secondary_value = None

        if secondary_value is not None:
            out["secondaryInFeed"] = {
                "state": secondary_value,
                "attributes": {},
                "unit": "kWh",
            }

        for item in consumptions.get("list") or []:
            if not item.get("name"):
                continue
            out[item["name"]] = {
                "state": item["usage"],
                "attributes": {
                    "numberOfInstallations": item.get("numberOfInstallations"),
                },
                "unit": item.get("unit", "kWh"),
            }

        for item in feed_in.get("list") or []:
            if not item.get("name"):
                continue
            attributes = {
                "numberOfInstallations": item.get("numberOfInstallations"),
                "installedCapacity (kW)": item.get("installedCapacity"),
            }
            capacity = float(item.get("installedCapacity") or 0)
            if capacity > 0:
                utilization = float(item["usage"]) / (capacity / 4.0) * 100.0
                attributes["utilization (%)"] = round(utilization, 1)

            out[item["name"]] = {
                "state": item["usage"],
                "attributes": attributes,
                "unit": item.get("unit", "kWh"),
            }

        return out

    def add_update_listener(self, listener) -> None:
        """Register a sensor listener for update notifications."""
        self._update_listeners.append(listener)
        _LOGGER.debug("Registered sensor: %s", listener.entity_id)
        listener.update_callback()

    def _notify_listeners(self) -> None:
        """Notify all registered sensors."""
        for listener in self._update_listeners:
            listener.update_callback()
        _LOGGER.debug("Notified %s listener(s)", len(self._update_listeners))


class EONEnergiemonitorHub:
    """Legacy coordinator plus optional scoped coordinators."""

    def __init__(
        self,
        legacy: EONEnergiemonitor,
        scopes: Dict[str, EONEnergiemonitor],
    ):
        """Initialize hub."""
        self.legacy = legacy
        self.scopes = scopes


def _schedule_coordinator(hass, coordinator: EONEnergiemonitor) -> None:
    """Poll a coordinator on its scan_interval."""
    interval = coordinator.scan_interval
    now = dt_util.utcnow()
    async_track_utc_time_change(
        hass,
        coordinator.update,
        minute=range(now.minute % interval, 60, interval),
        second=now.second,
    )


async def async_setup(hass, config):
    """Set up the EON Energiemonitor integration."""
    if DOMAIN not in config:
        raise ConfigError(
            "Missing eon-energiemonitor configuration. "
            "Add eon-energiemonitor: to configuration.yaml (see README)."
        )

    domain_config = config[DOMAIN]
    region_code = domain_config[CONF_REGION_CODE]
    default_interval = domain_config[CONF_SCAN_INTERVAL]
    scope_entries = domain_config.get(CONF_SCOPE, [])

    legacy = EONEnergiemonitor(
        hass, region_code, scan_interval=default_interval
    )
    scopes: Dict[str, EONEnergiemonitor] = {}
    for entry in scope_entries:
        alias = entry[CONF_ALIAS]
        interval = entry.get(CONF_SCAN_INTERVAL, default_interval)
        scopes[alias] = EONEnergiemonitor(
            hass,
            entry[CONF_REGION_CODE],
            alias=alias,
            scan_interval=interval,
        )

    hub = EONEnergiemonitorHub(legacy=legacy, scopes=scopes)
    hass.data[DOMAIN] = hub

    _schedule_coordinator(hass, legacy)
    for coordinator in scopes.values():
        _schedule_coordinator(hass, coordinator)

    if not await legacy.update():
        _LOGGER.warning(
            "Initial EON Energiemonitor update failed (%s)",
            legacy.last_error,
        )

    for alias, coordinator in scopes.items():
        if not await coordinator.update():
            _LOGGER.warning(
                "Initial EON Energiemonitor scope '%s' update failed (%s)",
                alias,
                coordinator.last_error,
            )

    await discovery.async_load_platform(hass, "sensor", DOMAIN, {}, config)

    return True
