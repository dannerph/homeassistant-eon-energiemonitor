# EON Energiemonitor

Custom component for [Home Assistant](https://www.home-assistant.io/) — live data from the EON Energiemonitor API (V2 / v0.4.0).

## Configuration

```yaml
eon-energiemonitor:
  region_code: "12345678"
  scan_interval: 15
```

* **region_code** (required, digits only): Resolve via  
  `https://api-energiemonitor.eon.com/region-data?regionUrlKey=<slug>`  
  (`<slug>` = last segment of your dashboard URL)
* **scan_interval** (optional): Minutes between updates (default: 15)

Invalid or unknown `region_code`: see README — status sensor and **Settings → Repairs**.

V2 talks to the API with browser TLS (`curl_cffi`) so Cloudflare challenges do not block Home Assistant the way plain `aiohttp` did.

Dashboard: [power-distribution-card](https://github.com/JonahKr/power-distribution-card) + `ui/eon-energiemonitor-power-card.yaml`.
