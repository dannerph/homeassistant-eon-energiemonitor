# Multi-scope regions (planned v0.3.0)

Specification for supporting several EON regions in one Home Assistant integration while keeping existing installations unchanged.

**Status:** Spec only — not implemented yet.

| | |
|---|---|
| **Upstream issue** | [dannerph/homeassistant-eon-energiemonitor#4](https://github.com/dannerph/homeassistant-eon-energiemonitor/issues/4) |
| **Issue text (regenerate)** | `python3 scripts/generate-scope-issue.py` → [SCOPE_ISSUE.md](SCOPE_ISSUE.md) |

## Goals

- **Backward compatible:** Existing configs with only `region_code` keep the same entity IDs (`sensor.eon_energiemonitor_*`, `unique_id` `eon_energy_*`).
- **Generic:** Any administrative level the API offers (municipality, district, regierungsbezirk, …) via user-defined `alias`, not hard-coded “Gemeinde + Landkreis”.
- **Parity:** Each scope gets the same sensor types the API provides for that region, plus `status` and `region` sensors with `dashboard_url`.

## Configuration

```yaml
eon-energiemonitor:
  region_code: "01234567"   # legacy slot (your primary region)
  scan_interval: 5          # default for all regions
  scope:
    - region_code: "01234"
      alias: landkreis
      # scan_interval: 10   # optional override for this scope only
```

| Key | Required | Meaning |
|-----|----------|---------|
| `region_code` | yes | Legacy region; drives unprefixed entities |
| `scan_interval` | no (default 5) | Global poll interval (minutes) |
| `scope` | no | Extra regions; empty or omitted = current behaviour |
| `scope[].region_code` | yes per entry | Numeric EON `regionCode` |
| `scope[].alias` | yes per entry | Prefix for entity / `unique_id` names |
| `scope[].scan_interval` | no | Overrides global interval for this entry only |

Example (municipality + enclosing district):

| Role | `region_code` | `alias` | Dashboard slug (from API `regionUrlKey`) |
|------|---------------|---------|------------------------------------------|
| Legacy | `01234567` | — | `gemeinde-beispiel` |
| Scope | `01234` | `landkreis` | `landkreis-beispiel` |

Resolve real codes via [REGIONEN.md](REGIONEN.md) or `region-data?regionUrlKey=<slug>`.

## Entity naming

| Role | `entity_id` pattern | `unique_id` pattern |
|------|---------------------|---------------------|
| Legacy | `sensor.eon_energiemonitor_{metric}` | `eon_energy_{metric}` |
| Scope | `sensor.eon_energiemonitor_{alias}_{metric}` | `eon_energy_{alias}_{metric}` |

`{metric}` includes: `status`, `region`, `autarky`, `energymix`, `secondaryinfeed`, and all consumption/generation keys exposed today (same set as legacy, driven by API payload per region).

**Examples**

- Legacy: `sensor.eon_energiemonitor_autarky`
- Scope: `sensor.eon_energiemonitor_landkreis_autarky`, `sensor.eon_energiemonitor_landkreis_status`

## Validation

| Rule | On violation |
|------|----------------|
| `region_code` / `scope[].region_code` non-empty, numeric | `ConfigError` at setup |
| `alias` matches `^[a-z0-9_]+$` | `ConfigError` at setup |
| `alias` unique within `scope` | `ConfigError` at setup |
| `alias` not in **reserved** list | `ConfigError` at setup |
| No limit on number of `scope` entries | — |

**Reserved `alias` values** (collision with legacy metric names):  
`status`, `region`, `autarky`, `secondaryinfeed`, `energymix`, `bio`, `solar`, `wind`, `water`, `others`, `domestic`, `public`, `industrial`.

## Runtime behaviour

- One coordinator (or equivalent) per configured region; legacy and scopes polled on their intervals.
- API returns no value for a metric → sensor exists, state **`unavailable`** (HA standard).
- HTTP 404 / invalid `region_code` for a scope → scope sensors `unavailable`; **Repair issue per `alias`** (`region_not_found_{alias}` or similar). Legacy region unaffected if its API calls succeed.
- Update failures for a scope → **Repair issue per `alias`**; legacy issues unchanged when only a scope fails.

## Repairs

| Case | Behaviour |
|------|-----------|
| Legacy `region_code` not found | Existing `region_not_found` issue |
| Scope `region_code` not found | New issue, placeholders include `alias` and `region_code` |
| Scope update failed (network, parse, …) | New issue per `alias` |
| Legacy OK, scope failing | No regression on legacy entities |

## Non-goals (v0.3.0)

- Replacing `region_code` with a single `regions:` list only (would break existing YAML).
- Config UI / config flow (YAML only, as today).
- Auto-discovery of administrative level from API (only user `alias`).

## Implementation notes (for developers)

- Refactor `hass.data[DOMAIN]` to hold legacy coordinator + map `alias → coordinator`.
- `async_setup_platform`: register legacy sensors first (unchanged classes/IDs), then loop `scope` and register prefixed sensors.
- Issue registry IDs must be unique per `alias`.
- Document in README + `doc/API.md`; example under `doc/examples/`.
- Version bump: **0.3.0** in `manifest.json` when implemented.

## Open questions (none blocking spec)

- Exact translation keys / repair issue IDs (to be aligned with `strings.json` at implementation).

## References

- Region list: [REGIONEN.md](REGIONEN.md)
- API fields: [API.md](API.md)
- GitHub issue template: [scope-issue.meta.yaml](scope-issue.meta.yaml), [templates/scope-issue.en.md](templates/scope-issue.en.md)
