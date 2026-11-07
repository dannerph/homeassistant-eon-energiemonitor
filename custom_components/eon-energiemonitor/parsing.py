"""Pure mapping of EON meter-data JSON to sensor payloads (V2)."""

from __future__ import annotations

from typing import Any, Dict, Optional


def is_cloudflare_challenge(
    status: int,
    body: str = "",
    headers: Optional[Dict[str, str]] = None,
) -> bool:
    """Return True when the response is a Cloudflare browser challenge."""
    headers = {k.lower(): v for k, v in (headers or {}).items()}
    if headers.get("cf-mitigated", "").lower() == "challenge":
        return True
    if status != 403:
        return False
    low = (body or "").lower()
    return (
        "just a moment" in low
        or "cf_chl" in low
        or "challenge-platform" in low
    )


def _float_or_none(value: Any) -> Optional[float]:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def prepare_meter_data(payload: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Map a meter-data API payload to coordinator sensor entries.

    Raises KeyError / TypeError / ValueError on structurally invalid payloads
    that the caller should treat as parse errors.
    """
    if not isinstance(payload, dict):
        raise TypeError("meter-data payload must be a dict")

    out: Dict[str, Dict[str, Any]] = {}

    if "autarky" in payload:
        out["autarky"] = {
            "state": payload["autarky"],
            "attributes": {},
            "unit": "%",
        }

    if "energyMix" in payload:
        out["energyMix"] = {
            "state": payload["energyMix"],
            "attributes": {},
            "unit": "%",
        }

    consumptions = payload.get("consumptions") or {}
    feed_in = payload.get("feedIn") or {}
    if not isinstance(consumptions, dict) or not isinstance(feed_in, dict):
        raise TypeError("consumptions and feedIn must be objects")

    if "secondaryInFeed" in payload:
        secondary_value = payload["secondaryInFeed"]
    elif consumptions.get("total") is not None and feed_in.get("total") is not None:
        secondary_value = float(consumptions["total"]) - float(feed_in["total"])
    else:
        secondary_value = None

    if secondary_value is not None:
        out["secondaryInFeed"] = {
            "state": secondary_value,
            "attributes": {},
            "unit": "kWh",
        }

    consumption_total = _float_or_none(consumptions.get("total"))
    if consumption_total is not None:
        out["consumption_total"] = {
            "state": consumption_total,
            "attributes": {},
            "unit": "kWh",
        }

    generation_total = _float_or_none(feed_in.get("total"))
    if generation_total is not None:
        out["generation_total"] = {
            "state": generation_total,
            "attributes": {},
            "unit": "kWh",
        }

    renewables = _float_or_none(payload.get("feedInRenewables"))
    if renewables is not None:
        out["feed_in_renewables"] = {
            "state": renewables,
            "attributes": {},
            "unit": "kWh",
        }
        if generation_total and generation_total > 0:
            out["renewable_generation_share"] = {
                "state": renewables / generation_total * 100.0,
                "attributes": {
                    "feed_in_renewables": renewables,
                    "generation_total": generation_total,
                },
                "unit": "%",
            }

    co2_kg = _float_or_none(payload.get("dailyCo2Savings"))
    if co2_kg is not None:
        out["co2_savings_today"] = {
            "state": round(co2_kg / 1000.0, 2),
            "attributes": {"daily_co2_savings_kg": co2_kg},
            "unit": "t",
        }

    timestamp = payload.get("timestamp")
    if isinstance(timestamp, dict):
        interval_attrs = {
            k: v
            for k, v in {
                "interval_start": timestamp.get("start"),
                "interval_end": timestamp.get("end"),
            }.items()
            if v is not None
        }
    else:
        interval_attrs = {}

    for item in consumptions.get("list") or []:
        if not item.get("name"):
            continue
        attrs = {
            "numberOfInstallations": item.get("numberOfInstallations"),
        }
        attrs.update(interval_attrs)
        out[item["name"]] = {
            "state": item["usage"],
            "attributes": attrs,
            "unit": item.get("unit", "kWh"),
        }

    dominant_name: Optional[str] = None
    dominant_usage = -1.0
    for item in feed_in.get("list") or []:
        if not item.get("name"):
            continue
        attributes = {
            "numberOfInstallations": item.get("numberOfInstallations"),
            "installedCapacity (kW)": item.get("installedCapacity"),
        }
        attributes.update(interval_attrs)
        capacity = float(item.get("installedCapacity") or 0)
        usage = float(item["usage"])
        if capacity > 0:
            utilization = usage / (capacity / 4.0) * 100.0
            attributes["utilization (%)"] = round(utilization, 1)

        out[item["name"]] = {
            "state": item["usage"],
            "attributes": attributes,
            "unit": item.get("unit", "kWh"),
        }

        if usage > dominant_usage:
            dominant_usage = usage
            dominant_name = item["name"]

    if (
        dominant_name is not None
        and generation_total is not None
        and generation_total > 0
    ):
        out["dominant_source"] = {
            "state": dominant_usage / generation_total * 100.0,
            "attributes": {"name": dominant_name, **interval_attrs},
            "unit": "%",
        }

    return out
