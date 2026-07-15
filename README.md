# EON Energiemonitor [[Home Assistant](https://www.home-assistant.io/) Component]

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

This custom component integrates the EON Energiemonitor into Home Assistant. Sensor values are fetched from the same API used by the public dashboards (for example [energiemonitor.bayernwerk.de](https://energiemonitor.bayernwerk.de/demo)).

## Installation

Copy the folder `custom_components/eon-energiemonitor` into your Home Assistant `custom_components` directory, add the configuration below to `configuration.yaml`, and restart Home Assistant.

Via HACS: add this repository as a custom repository (category: Integration), install **EON Energiemonitor**, configure, and restart.

## Configuration

```yaml
eon-energiemonitor:
  region_code: "12345678"
  scan_interval: 5
```

Configuration variables:

* **region_code** (required): Numeric location ID for the EON API (`meter-data?regionCode=…`). Must contain digits only — not the municipality URL slug.
* **scan_interval** (optional): Update interval in **minutes**. Default: `5` (same as the web app).
* **scope** (optional, v0.3.0+): Additional regions (e.g. district vs municipality). Each entry needs `region_code` and `alias` (prefix for entity names). See [doc/SCOPE_SPEC.md](doc/SCOPE_SPEC.md).

### Multiple regions (scope)

Keep **`region_code`** as the primary region (existing entity IDs unchanged). Add further regions under **`scope`**:

```yaml
eon-energiemonitor:
  region_code: "12345678"
  scan_interval: 5
  scope:
    - region_code: "1234"
      alias: landkreis
      # scan_interval: 10   # optional override for this entry
```

Legacy entities stay `sensor.eon_energiemonitor_*`. Scope entities use the alias prefix, e.g. `sensor.eon_energiemonitor_landkreis_autarky`, `sensor.eon_energiemonitor_landkreis_status`.

Example package: [doc/examples/eon_energiemonitor_scope.yaml](doc/examples/eon_energiemonitor_scope.yaml).

Each municipality dashboard has a URL slug (last path segment) and a separate numeric **region_code** for the API.

### Method 1: Region API (recommended)

Replace `<slug>` with the slug from your dashboard URL (e.g. `https://energiemonitor.bayernwerk.de/<slug>`):

```bash
curl -s "https://api-energiemonitor.eon.com/region-data?regionUrlKey=<slug>"
```

Example response shape:

```json
{
  "regionCode": "12345678",
  "regionName": "Example Municipality",
  "regionUrlKey": "example-town",
  "tenantId": "3190"
}
```

Use the **`regionCode`** value in `configuration.yaml`.

### Method 2: Browser network tab

Open your dashboard, open developer tools → Network, and look for `meter-data?regionCode=…`. See `doc/regionCode.png`.

![how to find region code](doc/regionCode.png "Network traffic analysis")

## Configuration errors

| Situation | Example | Behaviour |
|-----------|---------|-----------|
| Missing `eon-energiemonitor:` block | — | Integration does not load |
| Empty or non-numeric `region_code` | `""`, `"my-town"` | `ConfigError` at startup (schema validation) |
| Unknown numeric code | API HTTP 404 | Integration loads; energy sensors stay **unavailable**; status sensor shows **Region not found**; entry under **Settings → Repairs** |
| Temporary network/API error | timeout, 5xx | Status sensor + repair hint; retry every `scan_interval` minutes |

After fixing `region_code`, restart Home Assistant (or wait for the next scheduled update). On success, `sensor.eon_energiemonitor_status` becomes **OK** and repairs are cleared.

### Status sensor

`sensor.eon_energiemonitor_status` (diagnostic) reports e.g. `OK`, `Region not found`, `Network error`. Attributes include `region_code`, `last_error`, and `region_lookup_url`.

### Optional Lovelace helpers

| File | Purpose |
|------|---------|
| `ui/eon-energiemonitor-status-banner.yaml` | Markdown hint when status is not OK |
| `ui/eon-energiemonitor-power-card.yaml` | Example [power-distribution-card](https://github.com/JonahKr/power-distribution-card) layout |
| `ui/eon-energiemonitor-landkreis-title.yaml` + `landkreis-power-card.yaml` | Scope example (alias `landkreis`) |
| `doc/examples/eon_energiemonitor_setup_hint.yaml` | Template sensor when integration is not loaded |

Screenshots and examples live under **`doc/`** (`regionCode.png`, `example.png`, `doc/examples/`).

Full **API field reference**: [doc/API.md](doc/API.md) (region-data, meter-data, autarky, energyMix, entity mapping).

## Entities

* `sensor.eon_energiemonitor_status` (diagnostic; includes `dashboard_url`, region metadata)
* `sensor.eon_energiemonitor_region` (municipality name from region-data)
* `sensor.eon_energiemonitor_autarky`
* `sensor.eon_energiemonitor_secondaryinfeed`
* `sensor.eon_energiemonitor_energymix`
* `sensor.eon_energiemonitor_solar`
* `sensor.eon_energiemonitor_domestic`
* …

Works best with the [power-distribution-card](https://github.com/JonahKr/power-distribution-card) by [JonahKr](https://github.com/JonahKr).

![example power distribution card](doc/example.png "power-distribution-card example")

<details>
  <summary>Power-distribution-card config (see also ui/eon-energiemonitor-power-card.yaml)</summary>

```
type: custom:power-distribution-card
title: Energiemonitor
entities:
  - decimals: 2
    display_abs: true
    name: Bio
    unit_of_display: kWh
    unit_of_measurement: kWh
    icon: mdi:lightning-bolt-outline
    producer: true
    entity: sensor.eon_energiemonitor_bio
    preset: producer
  - decimals: 2
    display_abs: true
    name: Netzbezug
    unit_of_display: kWh
    unit_of_measurement: kWh
    icon: mdi:transmission-tower
    entity: sensor.eon_energiemonitor_secondaryinfeed
    preset: grid
  - decimals: 2
    display_abs: true
    name: Solar
    unit_of_display: kWh
    unit_of_measurement: kWh
    icon: mdi:solar-power
    producer: true
    entity: sensor.eon_energiemonitor_solar
    preset: solar
  - decimals: 2
    display_abs: true
    name: Haushalte
    unit_of_display: kWh
    unit_of_measurement: kWh
    consumer: true
    invert_value: true
    icon: mdi:home-assistant
    entity: sensor.eon_energiemonitor_domestic
    preset: home
  - decimals: 2
    display_abs: true
    name: Wasser
    unit_of_display: kWh
    unit_of_measurement: kWh
    icon: mdi:hydro-power
    producer: true
    entity: sensor.eon_energiemonitor_water
    preset: hydro
  - decimals: 2
    display_abs: true
    name: Gemeinde
    unit_of_display: kWh
    unit_of_measurement: kWh
    consumer: true
    invert_value: true
    icon: mdi:lightbulb
    entity: sensor.eon_energiemonitor_public
    preset: consumer
  - decimals: 2
    display_abs: true
    name: weitere Erzeuger
    unit_of_display: kWh
    unit_of_measurement: kWh
    icon: mdi:lightning-bolt-outline
    producer: true
    entity: sensor.eon_energiemonitor_others
    preset: producer
  - decimals: 2
    display_abs: true
    name: Industrie
    unit_of_display: kWh
    unit_of_measurement: kWh
    consumer: true
    invert_value: true
    icon: mdi:lightbulb
    entity: sensor.eon_energiemonitor_industrial
    preset: consumer
center:
  type: bars
  content:
    - name: Autarky
      preset: custom
      bar_color: lightblue
      bar_bg_color: ""
      entity: sensor.eon_energiemonitor_autarky
    - name: Mix
      preset: custom
      bar_color: green
      bar_bg_color: ""
      entity: sensor.eon_energiemonitor_energymix
animation: slide
```

</details>
