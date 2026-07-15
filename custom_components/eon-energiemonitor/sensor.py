"""Support for EON Energiemonitor sensors."""
import logging
from typing import List, Optional

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import EntityCategory

from . import DOMAIN, ENERGY_METRICS, EONEnergiemonitor, EONEnergiemonitorHub

_LOGGER = logging.getLogger(__name__)


def _sensor_names(metric: str, alias: Optional[str]) -> tuple[str, str]:
    """Return (entity_name, unique_id) for a metric."""
    if alias:
        return (
            f"eon_energiemonitor_{alias}_{metric}",
            f"eon_energy_{alias}_{metric}",
        )
    return (f"eon_energiemonitor_{metric}", f"eon_energy_{metric}")


def _build_coordinator_sensors(coordinator: EONEnergiemonitor) -> List[SensorEntity]:
    """Create the full sensor set for one coordinator."""
    alias = coordinator.alias
    return [
        EONStatusSensor(coordinator, alias),
        EONRegionSensor(coordinator, alias),
        *[EONEnergySensor(metric, coordinator, alias) for metric in ENERGY_METRICS],
    ]


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the EON Energiemonitor sensors."""
    if DOMAIN not in hass.data:
        _LOGGER.error("EON Energiemonitor hub is not initialized")
        return

    hub: EONEnergiemonitorHub = hass.data[DOMAIN]
    sensors: List[SensorEntity] = _build_coordinator_sensors(hub.legacy)
    for coordinator in hub.scopes.values():
        sensors.extend(_build_coordinator_sensors(coordinator))

    async_add_entities(sensors)


class EONStatusSensor(SensorEntity):
    """Shows whether the integration is configured and receiving data."""

    _attr_should_poll = False
    _attr_icon = "mdi:information-outline"
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, coordinator: EONEnergiemonitor, alias: Optional[str]) -> None:
        """Initialize the status sensor."""
        self._coordinator = coordinator
        name, unique_id = _sensor_names("status", alias)
        self._attr_name = name
        self._attr_unique_id = unique_id
        self._attributes: dict = {}

    @property
    def extra_state_attributes(self) -> dict:
        """Return diagnostic attributes."""
        return self._attributes

    async def async_update(self) -> None:
        """Apply coordinator status."""
        data = self._coordinator.get_data("status")
        if data is None:
            self._attr_native_value = None
            self._attributes = self._coordinator.get_region_attributes()
            self._attr_available = False
            return

        self._attr_available = True
        self._attr_native_value = data.get("state")
        self._attributes = data.get("attributes") or {}

    def update_callback(self) -> None:
        """Schedule a state update."""
        self.async_schedule_update_ha_state(True)

    async def async_added_to_hass(self) -> None:
        """Register for coordinator updates."""
        self._coordinator.add_update_listener(self)


class EONRegionSensor(SensorEntity):
    """Municipality name and region metadata from region-data API."""

    _attr_should_poll = False
    _attr_icon = "mdi:map-marker"
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, coordinator: EONEnergiemonitor, alias: Optional[str]) -> None:
        """Initialize the region sensor."""
        self._coordinator = coordinator
        name, unique_id = _sensor_names("region", alias)
        self._attr_name = name
        self._attr_unique_id = unique_id
        self._attributes: dict = {}

    @property
    def extra_state_attributes(self) -> dict:
        """Return region metadata for dashboards."""
        return self._attributes

    async def async_update(self) -> None:
        """Apply cached region-data."""
        data = self._coordinator.get_data("region")
        if data is None:
            self._attr_native_value = None
            self._attributes = self._coordinator.get_region_attributes()
            self._attr_available = False
            return

        self._attr_native_value = data.get("state")
        self._attributes = data.get("attributes") or {}
        self._attr_available = self._attr_native_value is not None

    def update_callback(self) -> None:
        """Schedule a state update."""
        self.async_schedule_update_ha_state(True)

    async def async_added_to_hass(self) -> None:
        """Register for coordinator updates."""
        self._coordinator.add_update_listener(self)


class EONEnergySensor(SensorEntity):
    """Sensor entity for EON Energiemonitor values."""

    _attr_should_poll = False
    _attr_icon = "mdi:flash"

    def __init__(
        self,
        metric: str,
        coordinator: EONEnergiemonitor,
        alias: Optional[str],
    ) -> None:
        """Initialize the EON Energiemonitor sensor."""
        self._metric = metric
        self._coordinator = coordinator
        self._attributes: dict = {}
        name, unique_id = _sensor_names(metric, alias)
        self._attr_name = name
        self._attr_unique_id = unique_id

    @property
    def extra_state_attributes(self) -> dict:
        """Return sensor attributes."""
        return self._attributes

    async def async_update(self) -> None:
        """Apply the latest cached values from the coordinator."""
        data = self._coordinator.get_data(self._metric)
        _LOGGER.debug("%s: %s", self._attr_unique_id, data)
        if data is None:
            self._attr_native_value = None
            self._attributes = {}
            self._attr_native_unit_of_measurement = None
            self._attr_available = False
            return

        state = data.get("state")
        if state is None:
            self._attr_native_value = None
            self._attributes = data.get("attributes") or {}
            self._attr_native_unit_of_measurement = data.get("unit")
            self._attr_available = False
            return

        try:
            self._attr_native_value = round(float(state), 1)
        except (TypeError, ValueError):
            _LOGGER.warning(
                "Invalid state for sensor %s: %r", self._attr_unique_id, state
            )
            self._attr_available = False
            return

        self._attr_available = True
        self._attributes = data.get("attributes") or {}
        self._attr_native_unit_of_measurement = data.get("unit")

    def update_callback(self) -> None:
        """Schedule a state update."""
        self.async_schedule_update_ha_state(True)

    async def async_added_to_hass(self) -> None:
        """Register for coordinator updates."""
        self._coordinator.add_update_listener(self)
