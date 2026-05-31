"""Support for EON Energiemonitor."""
import logging
from typing import Any, Dict, Optional, Tuple

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

API_BASE_URL = "https://api-energiemonitor.eon.com/"
REQUEST_TIMEOUT = aiohttp.ClientTimeout(total=30)
DASHBOARD_BASE_URL = "https://energiemonitor.bayernwerk.de/"

ISSUE_REGION_NOT_FOUND = "region_not_found"
ISSUE_UPDATE_FAILED = "update_failed"

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


CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_REGION_CODE): vol.All(cv.string, _validate_region_code),
                vol.Optional(CONF_SCAN_INTERVAL, default=5): cv.positive_int,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)


def _async_clear_issues(hass) -> None:
    """Remove known issues after a successful update."""
    ir.async_delete_issue(hass, DOMAIN, ISSUE_REGION_NOT_FOUND)
    ir.async_delete_issue(hass, DOMAIN, ISSUE_UPDATE_FAILED)


def _async_manage_issues(hass, region_code: str, last_error: Optional[str]) -> None:
    """Surface configuration or API problems in Settings → Repairs."""
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

    def __init__(self, hass, region_code: str):
        """Initialize EON Energiemonitor."""
        super().__init__(region_code)
        self._hass = hass
        self._data: Dict[str, Dict[str, Any]] = {}
        self._region_info: Dict[str, Any] = {}
        self._update_listeners = []

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

    async def update(self, *_args) -> bool:
        """Fetch region metadata and meter data."""
        await self._fetch_region_info()

        payload = await self.request_data()
        if payload is None:
            self._set_status_data(ok=False)
            _async_manage_issues(self._hass, self._region_code, self.last_error)
            self._notify_listeners()
            return False

        try:
            self._data = self._prepare_data(payload)
            self.last_error = None
            self._set_status_data(ok=True)
            _async_clear_issues(self._hass)
        except (KeyError, TypeError, ValueError) as err:
            self.last_error = "parse"
            _LOGGER.error("Failed to parse EON Energiemonitor data: %s", err)
            self._set_status_data(ok=False)
            _async_manage_issues(self._hass, self._region_code, self.last_error)
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
            "state": region_name or "unknown",
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
                utilization = (
                    float(item["usage"]) / (capacity / 4.0) * 100.0
                )
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


async def async_setup(hass, config):
    """Set up the EON Energiemonitor integration."""
    if DOMAIN not in config:
        raise ConfigError(
            "Missing eon-energiemonitor configuration. "
            "Add eon-energiemonitor: to configuration.yaml (see README)."
        )

    region_code = config[DOMAIN][CONF_REGION_CODE]
    scan_interval = config[DOMAIN][CONF_SCAN_INTERVAL]

    eon_monitor = EONEnergiemonitor(hass, region_code)
    hass.data[DOMAIN] = eon_monitor

    now = dt_util.utcnow()
    async_track_utc_time_change(
        hass,
        eon_monitor.update,
        minute=range(now.minute % scan_interval, 60, scan_interval),
        second=now.second,
    )

    if not await eon_monitor.update():
        _async_manage_issues(hass, region_code, eon_monitor.last_error)
        _LOGGER.warning(
            "Initial EON Energiemonitor update failed (%s)",
            eon_monitor.last_error,
        )
    else:
        _async_clear_issues(hass)

    await discovery.async_load_platform(hass, "sensor", DOMAIN, {}, config)

    return True
