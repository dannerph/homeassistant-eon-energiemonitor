"""Tests for YAML config validators."""

from __future__ import annotations

import pytest
import voluptuous as vol

from validation import validate_alias, validate_region_code, validate_unique_aliases


def test_region_code_accepts_digits() -> None:
    assert validate_region_code("09175135") == "09175135"
    assert validate_region_code(" 09175 ") == "09175"


@pytest.mark.parametrize("value", ["", "   ", "poing", "09-175"])
def test_region_code_rejects_invalid(value: str) -> None:
    with pytest.raises(vol.Invalid):
        validate_region_code(value)


def test_alias_accepts_valid() -> None:
    assert validate_alias("landkreis") == "landkreis"
    assert validate_alias("lk_ebe") == "lk_ebe"


@pytest.mark.parametrize("value", ["", "Landkreis", "lk-ebe", "autarky", "energymix"])
def test_alias_rejects_invalid_or_reserved(value: str) -> None:
    with pytest.raises(vol.Invalid):
        validate_alias(value)


def test_new_v2_metric_names_are_reserved() -> None:
    with pytest.raises(vol.Invalid):
        validate_alias("renewable_generation_share")
    with pytest.raises(vol.Invalid):
        validate_alias("co2_savings_today")


def test_unique_aliases() -> None:
    scopes = [{"alias": "a", "region_code": "1"}, {"alias": "b", "region_code": "2"}]
    assert validate_unique_aliases(scopes) == scopes
    with pytest.raises(vol.Invalid):
        validate_unique_aliases(
            [{"alias": "a", "region_code": "1"}, {"alias": "a", "region_code": "2"}]
        )
