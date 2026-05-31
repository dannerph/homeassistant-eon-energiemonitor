"""Support for EON Energiemonitor sensors."""
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import EntityCategory

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the EON Energiemonitor sensors."""
    if DOMAIN not in hass.data:
        _LOGGER.error("EON Energiemonitor coordinator is not initialized")
        return

    eon_energiemonitor = hass.data[DOMAIN]
    sensors = [
        EONStatusSensor(eon_energiemonitor),
        EONRegionSensor(eon_energiemonitor),
        EONEnergySensor("autarky", eon_energiemonitor),
        EONEnergySensor("secondaryInFeed", eon_energiemonitor),
        EONEnergySensor("energyMix", eon_energiemonitor),
        EONEnergySensor("bio", eon_energiemonitor),
        EONEnergySensor("solar", eon_energiemonitor),
        EONEnergySensor("wind", eon_energiemonitor),
        EONEnergySensor("water", eon_energiemonitor),
        EONEnergySensor("others", eon_energiemonitor),
        EONEnergySensor("domestic", eon_energiemonitor),
        EONEnergySensor("public", eon_energiemonitor),
        EONEnergySensor("industrial", eon_energiemonitor),
    ]
    async_add_entities(sensors)


class EONStatusSensor(SensorEntity):
    """Shows whether the integration is configured and receiving data."""

    _attr_should_poll = False
    _attr_icon = "mdi:information-outline"
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, eon_energiemonitor) -> None:
        """Initialize the status sensor."""
        self._eon_energiemonitor = eon_energiemonitor
        self._attr_name = "eon_energiemonitor_status"
        self._attr_unique_id = "eon_energy_status"
        self._attributes: dict = {}

    @property
    def extra_state_attributes(self) -> dict:
        """Return diagnostic attributes."""
        return self._attributes

    async def async_update(self) -> None:
        """Apply coordinator status."""
        data = self._eon_energiemonitor.get_data("status")
        if data is None:
            self._attr_native_value = "Unknown"
            self._attributes = self._eon_energiemonitor.get_region_attributes()
            return

        self._attr_native_value = data.get("state", "Unknown")
        self._attributes = data.get("attributes") or {}

    def update_callback(self) -> None:
        """Schedule a state update."""
        self.async_schedule_update_ha_state(True)

    async def async_added_to_hass(self) -> None:
        """Register for coordinator updates."""
        self._eon_energiemonitor.add_update_listener(self)


class EONRegionSensor(SensorEntity):
    """Municipality name and region metadata from region-data API."""

    _attr_should_poll = False
    _attr_icon = "mdi:map-marker"
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, eon_energiemonitor) -> None:
        """Initialize the region sensor."""
        self._eon_energiemonitor = eon_energiemonitor
        self._attr_name = "eon_energiemonitor_region"
        self._attr_unique_id = "eon_energy_region"
        self._attributes: dict = {}

    @property
    def extra_state_attributes(self) -> dict:
        """Return region metadata for dashboards."""
        return self._attributes

    async def async_update(self) -> None:
        """Apply cached region-data."""
        data = self._eon_energiemonitor.get_data("region")
        if data is None:
            self._attr_native_value = None
            self._attributes = self._eon_energiemonitor.get_region_attributes()
            return

        self._attr_native_value = data.get("state")
        self._attributes = data.get("attributes") or {}

    def update_callback(self) -> None:
        """Schedule a state update."""
        self.async_schedule_update_ha_state(True)

    async def async_added_to_hass(self) -> None:
        """Register for coordinator updates."""
        self._eon_energiemonitor.add_update_listener(self)


class EONEnergySensor(SensorEntity):
    """Sensor entity for EON Energiemonitor values."""

    _attr_should_poll = False
    _attr_icon = "mdi:flash"

    def __init__(self, name: str, eon_energiemonitor) -> None:
        """Initialize the EON Energiemonitor sensor."""
        self._name = name
        self._eon_energiemonitor = eon_energiemonitor
        self._attributes: dict = {}

        self._attr_name = f"eon_energiemonitor_{name}"
        self._attr_unique_id = f"eon_energy_{name}"

    @property
    def extra_state_attributes(self) -> dict:
        """Return sensor attributes."""
        return self._attributes

    async def async_update(self) -> None:
        """Apply the latest cached values from the coordinator."""
        data = self._eon_energiemonitor.get_data(self._name)
        _LOGGER.debug("%s: %s", self._attr_unique_id, data)
        if data is None:
            return

        state = data.get("state")
        if state is None:
            return

        try:
            self._attr_native_value = round(float(state), 1)
        except (TypeError, ValueError):
            _LOGGER.warning(
                "Invalid state for sensor %s: %r", self._attr_unique_id, state
            )
            return

        self._attributes = data.get("attributes") or {}
        self._attr_native_unit_of_measurement = data.get("unit")

    def update_callback(self) -> None:
        """Schedule a state update."""
        self.async_schedule_update_ha_state(True)

    async def async_added_to_hass(self) -> None:
        """Register for coordinator updates."""
        self._eon_energiemonitor.add_update_listener(self)
