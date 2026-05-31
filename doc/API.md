# EON API reference (integration mapping)

Base URL: `https://api-energiemonitor.eon.com/`  
Web dashboard: `https://energiemonitor.bayernwerk.de/<regionUrlKey>`

**Region list (snapshot):** [REGIONEN.md](REGIONEN.md) — all municipalities per grid operator, how to look up your `region_code`, and `scripts/generate-regions-doc.py` to refresh the file.

The integration calls **two endpoints** on each update (`scan_interval` minutes). Values for **autarky** and **energyMix** are provided by the API (regional balance, not calculated in Home Assistant). See [Bayernwerk Energiemonitor](https://www.bayernwerk.de/de/fuer-kommunen/digitale-loesungen/energiemonitor.html) for the public product description.

## `region-data`

| Query | Purpose |
|-------|---------|
| `regionCode=<code>` | Metadata for the configured region |
| `regionUrlKey=<slug>` | Resolve numeric `regionCode` from the dashboard URL slug |
| `tenantId=<id>` (no region param) | List all regions for a grid operator (`regions[]` in response) |

| Field | Meaning | Home Assistant |
|-------|---------|----------------|
| `regionCode` | Numeric region ID | Attribute `region_code` |
| `regionName` | Display name | State of `sensor.eon_energiemonitor_region` |
| `regionUrlKey` | URL slug | Attribute `region_url_key` |
| `latitude` / `longitude` | Coordinates | Attributes |
| `tenantId` | Tenant ID (internal) | Attribute `tenant_id` |
| `coatOfArmsMimeType` | Coat of arms MIME type | Attribute `coat_of_arms_mime_type` |

Derived: `dashboard_url` = `https://energiemonitor.bayernwerk.de/{regionUrlKey}` on `sensor.eon_energiemonitor_status`.

## `meter-data`

| Field | Unit | Meaning | Entity |
|-------|------|---------|--------|
| `timestamp.start` / `end` | Unix s | Aggregation interval | not exposed |
| `autarky` | % | Regional **self-sufficiency** (local generation vs demand in the interval) | `sensor.eon_energiemonitor_autarky` |
| `energyMix` | % | **Renewable share** in the regional mix | `sensor.eon_energiemonitor_energymix` |
| `secondaryInFeed` | kWh | **Grid import** (Netzbezug) | `sensor.eon_energiemonitor_secondaryinfeed` |
| `dailyCo2Savings` | API-specific | Daily CO₂ savings (regional) | **not mapped** in 0.2.1 |

If `secondaryInFeed` is missing: `consumptions.total − feedIn.total`.

### `consumptions.list[]`

| `name` | Meaning | Entity |
|--------|---------|--------|
| `domestic` | Households | `sensor.eon_energiemonitor_domestic` |
| `public` | Public consumers | `sensor.eon_energiemonitor_public` |
| `industrial` | Industry | `sensor.eon_energiemonitor_industrial` |

Per item: `usage` (state), `numberOfInstallations` (attribute).

### `feedIn.list[]`

| `name` | Meaning | Entity |
|--------|---------|--------|
| `solar` | Solar | `sensor.eon_energiemonitor_solar` |
| `wind` | Wind | `sensor.eon_energiemonitor_wind` |
| `water` | Hydro (if present) | `sensor.eon_energiemonitor_water` |
| `bio` | Biomass (if present) | `sensor.eon_energiemonitor_bio` |
| `others` | Other local generation (no further breakdown in API) | `sensor.eon_energiemonitor_others` |
| `pubsol` | Public solar | API only; **no** sensor in 0.2.1 |

Per item: `usage`, `installedCapacity` → attribute `installedCapacity (kW)`, optional `utilization (%)` (integration: `usage / (capacity/4) × 100`).

## Autarky vs energy mix

| Term | Is | Is not |
|------|-----|--------|
| **autarky** | Regional self-sufficiency % for the interval | Household autarky; not “consumption − PV” |
| **energyMix** | Renewable share % in the regional mix | PV self-consumption |

## Example

```bash
curl -s "https://api-energiemonitor.eon.com/meter-data?regionCode=<code>"
```

Regions differ in which `name` entries appear; sensors without data stay unavailable.
