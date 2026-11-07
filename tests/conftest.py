"""Pytest bootstrap: import integration modules without Home Assistant."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
COMPONENT = ROOT / "custom_components" / "eon-energiemonitor"

if str(COMPONENT) not in sys.path:
    sys.path.insert(0, str(COMPONENT))

FIXTURES = Path(__file__).resolve().parent / "fixtures"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES


@pytest.fixture
def meter_data_poing(fixtures_dir: Path) -> dict:
    import json

    return json.loads((fixtures_dir / "meter_data_poing.json").read_text())


@pytest.fixture
def region_data_poing(fixtures_dir: Path) -> dict:
    import json

    return json.loads((fixtures_dir / "region_data_poing.json").read_text())


@pytest.fixture
def cloudflare_html(fixtures_dir: Path) -> str:
    return (fixtures_dir / "cloudflare_challenge.html").read_text()
