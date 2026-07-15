#!/usr/bin/env python3
"""Generate doc/REGIONEN.md from the public EON Energiemonitor API."""

from __future__ import annotations

import json
import urllib.request
from datetime import date
from pathlib import Path

API_BASE = "https://api-energiemonitor.eon.com"
REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = REPO_ROOT / "doc" / "REGIONEN.md"


def fetch(url: str) -> object:
    with urllib.request.urlopen(url, timeout=120) as resp:
        return json.load(resp)


def dashboard_host(tenant: dict) -> str:
    for host in tenant.get("hostnames") or []:
        if host.startswith("energiemonitor.") and not host.startswith("energiemonitor-"):
            return host
    for host in tenant.get("hostnames") or []:
        if not host.startswith(("d-", "q-")):
            return host
    return "energiemonitor.bayernwerk.de"


def main() -> None:
    tenants = fetch(f"{API_BASE}/tenants")
    today = date.today().isoformat()

    sections: list[str] = []
    total_regions = 0
    tenant_summaries: list[tuple[str, str, str, int]] = []

    for tenant in sorted(tenants, key=lambda t: t.get("tenantShort", "")):
        tid = tenant["tenantId"]
        short = tenant.get("tenantShort", tid)
        full = tenant.get("tenantFull", "")
        host = dashboard_host(tenant)

        data = fetch(f"{API_BASE}/region-data?tenantId={tid}")
        regions = data.get("regions", []) if isinstance(data, dict) else []
        regions = sorted(regions, key=lambda r: (r.get("regionName") or "").lower())
        total_regions += len(regions)
        tenant_summaries.append((short, full, tid, len(regions)))

        if not regions:
            sections.append(f"### {short} — {full} (`tenantId={tid}`)\n\n*Keine Regionen in der API (Stand {today}).*\n")
            continue

        rows = [
            "| Gemeinde / Region | `region_code` | URL-Slug | Dashboard |",
            "|---|---|---|---|",
        ]
        for r in regions:
            name = (r.get("regionName") or "").replace("|", "\\|")
            code = r.get("regionCode", "")
            slug = r.get("regionUrlKey", "")
            url = f"https://{host}/{slug}"
            rows.append(f"| {name} | `{code}` | `{slug}` | [{slug}]({url}) |")

        sections.append(
            f"### {short} — {full} (`tenantId={tid}`)\n\n"
            f"Dashboard-Basis: `https://{host}/<regionUrlKey>` — **{len(regions)}** Regionen.\n\n"
            + "\n".join(rows)
            + "\n"
        )

    summary_rows = "\n".join(
        f"| {short} | {full} | `{tid}` | {count} |"
        for short, full, tid, count in tenant_summaries
    )

    body = f"""# EON Energiemonitor — Regionen (Gemeinden)

Abzug aller Regionen, die die öffentliche EON-API pro Netzbetreiber (Tenant) ausliefert.

| | |
|---|---|
| **Stand** | {today} |
| **Quelle** | `{API_BASE}` |
| **Regionen gesamt** | {total_regions} (eindeutige `regionCode`) |
| **Aktualisieren** | `python3 scripts/generate-regions-doc.py` |

> Der Energiemonitor deckt **nicht ganz Deutschland** ab, sondern nur Gemeinden/Regionen in den Netzgebieten der jeweiligen E.ON-Netzbetreiber. Ob eure Gemeinde dabei ist, sieht ihr in der Liste oder über die Suche unten.

## Eigene Gemeinde finden

### 1. Regionsübersicht im Browser

Auf der Seite des zuständigen Netzbetreibers (z. B. [Bayernwerk Regionsübersicht](https://energiemonitor.bayernwerk.de/regions-dashboard)) nach dem Ortsnamen suchen. Die URL der Gemeinde lautet `https://<netzbetreiber-host>/<regionUrlKey>` — der letzte Pfadteil ist der **URL-Slug**.

### 2. `region_code` aus dem URL-Slug (für Home Assistant)

Slug aus der Dashboard-URL nehmen und die API abfragen:

```bash
curl -s "{API_BASE}/region-data?regionUrlKey=<slug>" | python3 -m json.tool
```

Relevantes Feld: **`regionCode`** → Wert für `region_code` in `configuration.yaml`.  
Beispiel Bayernwerk: `curl -s "{API_BASE}/region-data?regionUrlKey=aichach"`

### 3. In dieser Datei suchen

Editor-Suche (`Cmd+F` / `Strg+F`) nach dem Gemeindenamen, oder im Terminal:

```bash
rg -i "Poing" doc/REGIONEN.md
# oder
grep -i "Poing" doc/REGIONEN.md
```

Die Spalte **`region_code`** ist der Wert für die Integration.

### 4. Live in der API (ohne diese Datei)

Alle Netzbetreiber:

```bash
curl -s "{API_BASE}/tenants" | python3 -m json.tool
```

Alle Regionen eines Netzbetreibers (z. B. Bayernwerk `tenantId=3190`):

```bash
curl -s "{API_BASE}/region-data?tenantId=3190" | python3 -m json.tool
```

Einzelne Gemeinde per Slug — siehe Abschnitt 2.

**Hinweis:** `GET /regions` antwortet mit HTTP 403. Die vollständige Liste kommt über **`region-data?tenantId=…`** ohne `regionCode`/`regionUrlKey`.

## Liste neu erzeugen

Diese Markdown-Datei wird nicht von Hand gepflegt:

```bash
cd /path/to/eon-energiemonitor
python3 scripts/generate-regions-doc.py
```

Das Skript liest `tenants` und pro Tenant `region-data?tenantId=…` und überschreibt `doc/REGIONEN.md`.

## Übersicht Netzbetreiber

| Kürzel | Netzbetreiber | `tenantId` | Regionen |
|---|---|---|---|
{summary_rows}

## Regionen nach Netzbetreiber

{"".join(sections)}
"""

    OUT_PATH.write_text(body, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({total_regions} regions, {len(tenants)} tenants)")


if __name__ == "__main__":
    main()
