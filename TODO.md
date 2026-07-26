# TODO

## Integration optimizations

- [ ] Reuse Home Assistant's shared aiohttp session via `async_get_clientsession(hass)` instead of creating a new `ClientSession` per request.
- [ ] Cache region metadata after startup and only refetch it when missing, so normal polling does not call `region-data` every cycle.
- [ ] Consider migrating the custom update/listener flow to Home Assistant's `DataUpdateCoordinator`.
- [ ] Add listener cleanup for entity removal/reload paths, such as `async_will_remove_from_hass` or unsubscribe callbacks.
- [ ] Add sensor metadata where applicable, including `device_class`, `state_class`, and units for energy and percentage sensors.
- [ ] Clarify scan interval handling, ideally by using a `timedelta`-style config validator or a clearly named minute-based option.
- [ ] Add focused tests for config validation and `_prepare_data`, including missing fields, invalid values, `secondaryInFeed` fallback, and utilization calculation.
- [ ] Review manifest metadata: remove the explicit `aiohttp` requirement if Home Assistant already provides it, and add appropriate quality metadata such as cloud polling class where supported.
