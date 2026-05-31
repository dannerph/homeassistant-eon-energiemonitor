# EON Energiemonitor

Custom component for [Home Assistant](https://www.home-assistant.io/) — live data from the EON Energiemonitor API.

## Configuration

```yaml
eon-energiemonitor:
  region_code: "12345678"
  scan_interval: 5
```

* **region_code** (required, digits only): Resolve via  
  `https://api-energiemonitor.eon.com/region-data?regionUrlKey=<slug>`  
  (`<slug>` = last segment of your dashboard URL)
* **scan_interval** (optional): Minutes between updates (default: 5)

Invalid or unknown `region_code`: see README — status sensor and **Settings → Repairs**.

Dashboard: [power-distribution-card](https://github.com/JonahKr/power-distribution-card) + `ui/eon-energiemonitor-power-card.yaml`.
