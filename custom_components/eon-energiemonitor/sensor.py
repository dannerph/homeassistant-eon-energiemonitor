"""Support for EON Energiemonitor."""
import logging

from homeassistant.components.sensor import SensorEntity

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the EON Energiemonitor sensors."""

    if discovery_info is None:
        return

    sensors = []
    eon_energiemonitor = hass.data[DOMAIN]
    sensors.append(EONEnergySensor("autarky", eon_energiemonitor))
    sensors.append(EONEnergySensor("secondaryInFeed", eon_energiemonitor))
    sensors.append(EONEnergySensor("energyMix", eon_energiemonitor))

    sensors.append(EONEnergySensor("bio", eon_energiemonitor))
    sensors.append(EONEnergySensor("solar", eon_energiemonitor))
    sensors.append(EONEnergySensor("wind", eon_energiemonitor))
    sensors.append(EONEnergySensor("water", eon_energiemonitor))
    sensors.append(EONEnergySensor("others", eon_energiemonitor))

    sensors.append(EONEnergySensor("domestic", eon_energiemonitor))
    sensors.append(EONEnergySensor("public", eon_energiemonitor))
    sensors.append(EONEnergySensor("industrial", eon_energiemonitor))

    async_add_entities(sensors)


class EONEnergySensor(SensorEntity):
    """The entity class for EON Energiemonitor charging stations sensors."""

    _attr_should_poll = False

    def __init__(self, name, eon_energiemontior):
        """Initialize the EON Energiemonitor Sensor."""
        self._name = name
        self._eon_energiemonitor = eon_energiemontior
        self._icon = "mdi:flash"
        self._attributes = {}

        self._attr_name = f"eon_energiemonitor_{self._name.capitalize()}"
        self._attr_unique_id = f"eon_energy_{self._name}"

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return self._icon

    @property
    def extra_state_attributes(self):
        """Return the state attributes of the binary sensor."""
        return self._attributes

    async def async_update(self):
        """Get latest cached states from the device."""

        data = self._eon_energiemonitor.get_data(self._name)
        _LOGGER.debug(data)
        if data is not None:
            self._attr_native_value = round(float(data.get("state")), 1)
            self._attributes = data.get("attributes")
            self._attr_native_unit_of_measurement = data.get("unit")

    def update_callback(self):
        """Schedule a state update."""
        self.async_schedule_update_ha_state(True)

    async def async_added_to_hass(self):
        """Add update callback after being added to hass."""
        self._eon_energiemonitor.add_update_listener(self)
