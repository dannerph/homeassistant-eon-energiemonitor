"""Tests for meter-data → sensor mapping."""

from __future__ import annotations

import copy

import pytest

from parsing import is_cloudflare_challenge, prepare_meter_data


def test_prepare_poing_fixture_core_metrics(meter_data_poing: dict) -> None:
    out = prepare_meter_data(meter_data_poing)

    assert "autarky" in out
    assert float(out["autarky"]["state"]) == pytest.approx(
        float(meter_data_poing["autarky"])
    )
    assert out["energyMix"]["unit"] == "%"
    assert float(out["energyMix"]["state"]) == pytest.approx(
        float(meter_data_poing["energyMix"])
    )
    assert out["secondaryInFeed"]["unit"] == "kWh"
    assert out["solar"]["unit"] == "kWh"
    assert out["domestic"]["attributes"]["numberOfInstallations"] == "7863"


def test_prepare_website_renewable_share(meter_data_poing: dict) -> None:
    out = prepare_meter_data(meter_data_poing)
    renewables = float(meter_data_poing["feedInRenewables"])
    generation = float(meter_data_poing["feedIn"]["total"])
    expected = renewables / generation * 100.0

    share = out["renewable_generation_share"]
    assert share["unit"] == "%"
    assert float(share["state"]) == pytest.approx(expected)
    # Must differ from API energyMix (renewables / consumption).
    assert float(share["state"]) != pytest.approx(float(out["energyMix"]["state"]))


def test_prepare_totals_and_co2(meter_data_poing: dict) -> None:
    out = prepare_meter_data(meter_data_poing)
    assert float(out["generation_total"]["state"]) == pytest.approx(
        float(meter_data_poing["feedIn"]["total"])
    )
    assert float(out["consumption_total"]["state"]) == pytest.approx(
        float(meter_data_poing["consumptions"]["total"])
    )
    assert float(out["feed_in_renewables"]["state"]) == pytest.approx(
        float(meter_data_poing["feedInRenewables"])
    )
    co2_kg = float(meter_data_poing["dailyCo2Savings"])
    assert out["co2_savings_today"]["unit"] == "t"
    assert float(out["co2_savings_today"]["state"]) == pytest.approx(
        round(co2_kg / 1000.0, 2)
    )
    assert out["co2_savings_today"]["attributes"]["daily_co2_savings_kg"] == co2_kg


def test_prepare_dominant_source_is_largest_feed_in(meter_data_poing: dict) -> None:
    out = prepare_meter_data(meter_data_poing)
    items = meter_data_poing["feedIn"]["list"]
    top = max(items, key=lambda i: float(i["usage"]))
    total = float(meter_data_poing["feedIn"]["total"])

    dom = out["dominant_source"]
    assert dom["attributes"]["name"] == top["name"]
    assert float(dom["state"]) == pytest.approx(float(top["usage"]) / total * 100.0)


def test_secondary_infeed_fallback_without_field(meter_data_poing: dict) -> None:
    payload = copy.deepcopy(meter_data_poing)
    del payload["secondaryInFeed"]
    out = prepare_meter_data(payload)
    expected = float(payload["consumptions"]["total"]) - float(payload["feedIn"]["total"])
    assert float(out["secondaryInFeed"]["state"]) == pytest.approx(expected)


def test_utilization_attribute_when_capacity_present(meter_data_poing: dict) -> None:
    out = prepare_meter_data(meter_data_poing)
    solar = next(i for i in meter_data_poing["feedIn"]["list"] if i["name"] == "solar")
    usage = float(solar["usage"])
    capacity = float(solar["installedCapacity"])
    expected = usage / (capacity / 4.0) * 100.0
    assert out["solar"]["attributes"]["utilization (%)"] == round(expected, 1)


def test_prepare_rejects_non_dict() -> None:
    with pytest.raises(TypeError):
        prepare_meter_data([])  # type: ignore[arg-type]


def test_is_cloudflare_challenge_header() -> None:
    assert is_cloudflare_challenge(
        403, "", {"cf-mitigated": "challenge", "server": "cloudflare"}
    )


def test_is_cloudflare_challenge_body(cloudflare_html: str) -> None:
    assert is_cloudflare_challenge(403, cloudflare_html, {})


def test_is_cloudflare_challenge_false_for_plain_404() -> None:
    assert not is_cloudflare_challenge(404, "Region not found", {})
    assert not is_cloudflare_challenge(200, '{"autarky":"1"}', {})
