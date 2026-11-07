# EON API reference (integration mapping)

Base URL: `https://api-energiemonitor.eon.com/`  
Web dashboard: `https://energiemonitor.bayernwerk.de/<regionUrlKey>`

**Region list (snapshot):** [REGIONEN.md](REGIONEN.md) — all municipalities per grid operator, how to look up your `region_code`, and `scripts/generate-regions-doc.py` to refresh the file.

**Multi-region (v0.3.0):** optional `scope` list — see [SCOPE_SPEC.md](SCOPE_SPEC.md).

**V2 (v0.4.0):** HTTP client uses browser TLS (`curl_cffi`, Chrome impersonation) because Cloudflare returns HTTP 403 challenges to plain `aiohttp`/`curl`. Default `scan_interval` is **15** minutes (API aggregation window).

The integration calls **`region-data`** (startup / after errors) and **`meter-data`** on each update. Values for **autarky** and **energyMix** come from the API. The website KPI “der Energie sind aus erneuerbaren Quellen” is **not** `energyMix`; it is `feedInRenewables / feedIn.total` → sensor `renewable_generation_share`. See [Bayernwerk Energiemonitor](https://www.bayernwerk.de/de/fuer-kommunen/digitale-loesungen/energiemonitor.html).

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
| `timestamp.start` / `end` | Unix s | Aggregation interval (~15 min) | attributes on list sensors |
| `autarky` | % | Regional **self-sufficiency** (generation / demand) | `sensor.eon_energiemonitor_autarky` |
| `energyMix` | % | Renewables / **consumption** (`feedInRenewables` / `consumptions.total`) | `sensor.eon_energiemonitor_energymix` |
| `secondaryInFeed` | kWh | **Grid import** (Netzbezug) | `sensor.eon_energiemonitor_secondaryinfeed` |
| `feedInRenewables` | kWh | Renewable share of regional generation (energy) | `sensor.eon_energiemonitor_feed_in_renewables` |
| `feedIn.total` | kWh | Total regional generation | `sensor.eon_energiemonitor_generation_total` |
| `consumptions.total` | kWh | Total regional consumption | `sensor.eon_energiemonitor_consumption_total` |
| `dailyCo2Savings` | kg | Daily CO₂ savings (regional) | `sensor.eon_energiemonitor_co2_savings_today` (state in **t**) |

Derived (integration):

| Sensor | Formula | Matches website |
|--------|---------|-----------------|
| `renewable_generation_share` | `feedInRenewables / feedIn.total × 100` | “der Energie sind aus erneuerbaren Quellen” |
| `dominant_source` | largest `feedIn.list[].usage / feedIn.total × 100` | “der regionalen Stromerzeugung sind aus …” (+ attribute `name`) |

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
| `pubsol` | Public solar | API only; **no** dedicated sensor |

Per item: `usage`, `installedCapacity` → attribute `installedCapacity (kW)`, optional `utilization (%)` (integration: `usage / (capacity/4) × 100`).

## Autarky vs energy mix vs website share

| Term | Is | Is not |
|------|-----|--------|
| **autarky** | Regional self-sufficiency % for the interval | Household autarky |
| **energyMix** | Renewables as % of **consumption** | Website “76 % erneuerbar” KPI |
| **renewable_generation_share** | Renewables as % of **regional generation** | Same as `energyMix` |

## Transport notes (V2)

Plain HTTP clients often receive Cloudflare `cf-mitigated: challenge` (HTTP 403 HTML). DNS A/AAAA records for the API hostname are Cloudflare edge IPs; calling them directly does not bypass the challenge. V2 uses `curl_cffi` with Chrome TLS impersonation against the normal hostname (no cookie bridge).

## Example

```bash
# May return Cloudflare HTML from many CLI clients; browser or curl_cffi works.
curl -s "https://api-energiemonitor.eon.com/meter-data?regionCode=<code>"
```

Regions differ in which `name` entries appear; sensors without data stay unavailable.
