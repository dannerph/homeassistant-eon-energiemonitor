# GitHub issue (upstream)

| | |
|---|---|
| **Title** | Feature: Multiple EON regions via optional `scope` list (v0.3.0, backward compatible) |
| **Repository** | `dannerph/homeassistant-eon-energiemonitor` |
| **Issue** | [#4](https://github.com/dannerph/homeassistant-eon-energiemonitor/issues/4) |
| **Labels** | `enhancement` |
| **Spec** | [SCOPE_SPEC.md](SCOPE_SPEC.md) |
| **Regenerate** | `python3 scripts/generate-scope-issue.py` |

> Auto-generated from `doc/scope-issue.meta.yaml` and `doc/templates/scope-issue.en.md`.  
> Edit those sources, then run the script. Use **Issue body** below for GitHub (or use `--body-file doc/templates/scope-issue.en.md`).

---

## Issue body (copy from here)

## Summary

The EON Energiemonitor API exposes many regions at different administrative levels (municipality, district, regierungsbezirk, grid area, etc.). Today the integration supports **one** `region_code` only.

I would like **optional additional regions** in the same integration instance, without breaking existing setups (entity IDs, automations, Lovelace).

This is a **design proposal** for a future **v0.3.0** — not implemented yet. Feedback welcome before any PR.

Detailed draft spec: `doc/SCOPE_SPEC.md` in the integration repository (see linked PR or default branch).

## Motivation

- Users may want to compare e.g. their **municipality** and the enclosing **district** (both have separate `regionCode` values in the API).
- The API also lists other levels (Teilnetz, Bundesland, …); a **generic** config is preferable to hard-coding fixed administrative levels.
- Existing installations should keep `sensor.eon_energiemonitor_*` unchanged.

## Proposed configuration

Keep today’s required `region_code` as the **legacy slot** (unprefixed entities). Add an optional list `scope` for further regions:

```yaml
eon-energiemonitor:
  region_code: "01234567"   # legacy / primary region
  scan_interval: 5
  scope:
    - region_code: "01234"
      alias: landkreis
      # scan_interval: 10   # optional per-scope override
```

| Key | Meaning |
|-----|---------|
| `region_code` | Unchanged: drives all current entity names |
| `scan_interval` | Global default (minutes) |
| `scope` | Optional; omit = current behaviour |
| `scope[].region_code` | Numeric EON `regionCode` |
| `scope[].alias` | User-defined prefix for entity / `unique_id` names |
| `scope[].scan_interval` | Optional override for that entry only |

Codes can be resolved via `region-data?regionUrlKey=<slug>` or `region-data?tenantId=<id>` (public API). See also region list documentation in related PRs/docs.

## Entity naming

| Role | Pattern |
|------|---------|
| Legacy | `sensor.eon_energiemonitor_{metric}` / `unique_id` `eon_energy_{metric}` |
| Scope | `sensor.eon_energiemonitor_{alias}_{metric}` / `eon_energy_{alias}_{metric}` |

Each scope should get the **same sensor types** the API provides for that region (including `status` and `region` with `dashboard_url`), not a reduced subset.

Examples:

- `sensor.eon_energiemonitor_autarky` (legacy, unchanged)
- `sensor.eon_energiemonitor_landkreis_autarky`
- `sensor.eon_energiemonitor_landkreis_status`

## Validation

- `alias`: `^[a-z0-9_]+$`, unique within `scope`, duplicates rejected at setup
- Block **reserved** aliases that collide with legacy metric names: `status`, `region`, `autarky`, `secondaryinfeed`, `energymix`, `bio`, `solar`, `wind`, `water`, `others`, `domestic`, `public`, `industrial`
- No hard limit on the number of `scope` entries (practical limit: API load)

## Runtime / repairs

- Missing API value for a metric → sensor exists, state **`unavailable`** (HA standard)
- Invalid / unknown `region_code` for a **scope** entry → repair issue **per `alias`**; legacy region continues if its API calls succeed
- Update failures for a scope → separate repair per `alias`

## Non-goals (initial version)

- Replacing `region_code` with a `regions`-only config (breaking change)
- Config flow / UI (YAML only, as today)
- Auto-detecting administrative level from the API (user chooses `alias`)

## Suggested version

**0.3.0** after any pending v0.2.x work is merged.

## Implementation

Happy to submit a PR if this direction is acceptable.
---

## Recreate or update on GitHub

```bash
gh issue view 4 --repo dannerph/homeassistant-eon-energiemonitor

# New issue:
gh issue create --repo dannerph/homeassistant-eon-energiemonitor \
  --title 'Feature: Multiple EON regions via optional `scope` list (v0.3.0, backward compatible)' \
  --body-file doc/templates/scope-issue.en.md \
  --label enhancement

# Update existing issue #4:
gh issue edit 4 --repo dannerph/homeassistant-eon-energiemonitor \
  --title 'Feature: Multiple EON regions via optional `scope` list (v0.3.0, backward compatible)' \
  --body-file doc/templates/scope-issue.en.md
```

After creating a new issue, set `issue_number` in `doc/scope-issue.meta.yaml` and re-run this script.
