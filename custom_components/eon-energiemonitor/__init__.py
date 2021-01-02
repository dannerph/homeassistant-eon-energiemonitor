"""Support for EON Energiemonitor."""
from enum import Enum
import logging

import aiohttp
import voluptuous as vol
import json

from homeassistant.helpers import discovery
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.event import (
    async_call_later,
    async_track_utc_time_change,
)
from homeassistant.const import CONF_SCAN_INTERVAL
import homeassistant.util.dt as dt_util

_LOGGER = logging.getLogger(__name__)

DOMAIN = "eon-energiemonitor"

CONF_REGION_CODE = "region_code"

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_REGION_CODE): cv.string,
                vol.Optional(CONF_SCAN_INTERVAL, default=5): cv.positive_int, # minutes
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

async def async_setup(hass, config):
    """Set up parameters."""
    
    region_code = config[DOMAIN][CONF_REGION_CODE]
    scan_interval = config[DOMAIN][CONF_SCAN_INTERVAL]

    eon_monitor = EONEnergiemonitor(hass, region_code)
    hass.data[DOMAIN] = eon_monitor

    # Register update every scan_interval minutes, starting now
    # this should even out the load on the servers
    now = dt_util.utcnow()
    async_track_utc_time_change(
        hass,
        eon_monitor.update,
        minute=range(now.minute % scan_interval, 60, scan_interval),
        second=now.second,
    )

    # initial update
    await eon_monitor.update()

    # Load sensors
    hass.async_create_task(
        discovery.async_load_platform(hass, "sensor", DOMAIN, {}, config)
    )

    return True


class SensorType(Enum):
    """Representation of Solcast SensorTypes."""

    feedIn = 1
    consumptions = 2


class EONEnergiemonitorAPI:
    """Representation of the EON Energiemonitor API."""

    def __init__(self, region_code):
        """Initialize solcast API."""

        self._base_url = "https://api-energiemonitor.eon.com/"
        self._region_code = region_code

    async def request_data(self, ssl=True):
        """Request data via EON Energiemonitor API."""

        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=f"{self._base_url}meter-data?regionCode={self._region_code}",ssl=ssl
            ) as resp:
                json = await resp.json()
                status = resp.status
        if status == 404:
            _LOGGER.error("The EON Energiemonitor site cannot be found or is not accessible.")
        elif status == 200:
            _LOGGER.debug("get request successful")

        return json


class EONEnergiemonitor(EONEnergiemonitorAPI):
    """Representation of a EON Energiemonitor."""

    def __init__(self, hass, region_code):
        """Initialize EON Energiemonitor."""

        super().__init__(region_code)
        self._hass = hass
        self._data = {}
        self._update_listeners = []

    def get_data(self, name):
        """Get EON energiemonitor data."""

        return self._data.get(name)

    async def update(self, *args):
        """Fetch new data from EON energiemonitor."""

        json = await self.request_data()
        self._data = self._prepare_data(json)

    def _prepare_data(self, json):
        
        # Copy default sensors
        out = {
            'autarky': {
                'state': json['autarky'],
                'attributes': None,
                'unit': '%',
                },
            'secondaryInFeed': {
                'state': json['secondaryInFeed'],
                'attributes': None,
                'unit': 'kWh',
                },
            'energyMix': {
                'state': json['energyMix'],
                'attributes': None,
                'unit': '%',
            },
        }

        # Convert lists
        try:
            for item in json.get("consumptions").get('list') :
                out[item['name']] = {
                    'state': item['usage'],
                    'attributes': {
                        'numberOfInstallations': item['numberOfInstallations'],
                    },
                    'unit': item['unit'],
                }
            for item in json.get("feedIn").get('list') :
                utilization_percentage = float(item['usage']) / (float(item['installedCapacity']) / 4.0) * 100.0
                out[item['name']] = {
                    'state': item['usage'],
                    'attributes': {
                        'numberOfInstallations': item['numberOfInstallations'],
                        'installedCapacity (kW)': item['installedCapacity'],
                        'utilization (%)': round(utilization_percentage, 1),
                    },
                    'unit': item['unit'],
                }
        except:
            print("An exception occurred")
        
        return out

    def add_update_listener(self, listener):
        """Add a listener for update notifications."""

        self._update_listeners.append(listener)
        _LOGGER.debug(f"registered sensor: {listener.entity_id}")
        
        # initial data is already loaded, thus update the component
        listener.update_callback()

    def _notify_listeners(self):

        # Inform entities about updated values
        for listener in self._update_listeners:
            listener.update_callback()
        _LOGGER.debug("Notifying all listeners")