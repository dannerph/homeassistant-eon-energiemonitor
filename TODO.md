# TODO

## Done in V2 (v0.4.0)

- [x] Browser-TLS client (`curl_cffi`) instead of plain `aiohttp` (Cloudflare challenge).
- [x] Map website renewable KPI as `renewable_generation_share` (keep `energyMix` unchanged).
- [x] Default `scan_interval` 15 minutes.
- [x] Unit tests for parsing, validation, challenge detection, mocked client.

## Integration optimizations

- [ ] Cache region metadata after startup and only refetch it when missing, so normal polling does not call `region-data` every cycle.
- [ ] Consider migrating the custom update/listener flow to Home Assistant's `DataUpdateCoordinator`.
- [ ] Add listener cleanup for entity removal/reload paths, such as `async_will_remove_from_hass` or unsubscribe callbacks.
- [ ] Reuse one long-lived `AsyncSession` across polls instead of opening a session per request.
- [ ] Optional: expose a single current value from `weather-data` / `intraday-data` (no historic series in the recorder).
