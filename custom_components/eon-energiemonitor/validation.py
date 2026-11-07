"""Configuration validators (no Home Assistant import)."""

from __future__ import annotations

import re
from typing import Iterable, List

import voluptuous as vol

try:
    from .const import RESERVED_ALIASES
except ImportError:  # pragma: no cover - flat import for unit tests
    from const import RESERVED_ALIASES

_ALIAS_PATTERN = re.compile(r"^[a-z0-9_]+$")


def validate_region_code(value: str) -> str:
    """Validate region_code from configuration."""
    code = str(value).strip()
    if not code:
        raise vol.Invalid(
            "region_code must not be empty. See README for how to resolve your code."
        )
    if not code.isdigit():
        raise vol.Invalid(
            "region_code must be numeric (not the URL slug). "
            "Resolve via https://api-energiemonitor.eon.com/region-data?regionUrlKey=<slug>"
        )
    return code


def validate_alias(value: str, reserved: Iterable[str] = RESERVED_ALIASES) -> str:
    """Validate scope alias for entity prefixes."""
    alias = str(value).strip()
    if not alias:
        raise vol.Invalid("scope alias must not be empty.")
    if not _ALIAS_PATTERN.match(alias):
        raise vol.Invalid(
            "scope alias must match ^[a-z0-9_]+$ (lowercase letters, digits, underscore)."
        )
    reserved_set = {r.lower() for r in reserved}
    if alias.lower() in reserved_set:
        raise vol.Invalid(f"scope alias '{alias}' is reserved.")
    return alias


def validate_unique_aliases(scopes: List[dict], alias_key: str = "alias") -> List[dict]:
    """Ensure scope aliases are unique."""
    seen: set[str] = set()
    for entry in scopes:
        alias = entry[alias_key]
        if alias in seen:
            raise vol.Invalid(f"Duplicate scope alias '{alias}'.")
        seen.add(alias)
    return scopes
