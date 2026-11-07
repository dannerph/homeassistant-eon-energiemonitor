"""Tests for the V2 API client (mocked transport)."""

from __future__ import annotations

import json
from typing import Any, Dict, Optional
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from client import EONEnergiemonitorAPI


class _FakeResp:
    def __init__(
        self,
        status_code: int,
        *,
        text: str = "",
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
    ):
        self.status_code = status_code
        self.text = text
        self.headers = headers or {}
        self._data = data

    def json(self):
        if self._data is not None:
            return self._data
        return json.loads(self.text)


@pytest.mark.asyncio
async def test_request_data_ok(meter_data_poing: dict) -> None:
    api = EONEnergiemonitorAPI("09175135")
    fake = _FakeResp(200, data=meter_data_poing)

    session = MagicMock()
    session.get = AsyncMock(return_value=fake)
    session.__aenter__ = AsyncMock(return_value=session)
    session.__aexit__ = AsyncMock(return_value=None)

    with patch("client.AsyncSession", create=True):
        # Patch where AsyncSession is imported inside _get_json
        with patch("curl_cffi.requests.AsyncSession", return_value=session):
            data = await api.request_data()

    assert data == meter_data_poing
    assert api.last_error is None


@pytest.mark.asyncio
async def test_request_data_challenge(cloudflare_html: str) -> None:
    api = EONEnergiemonitorAPI("09175135")
    fake = _FakeResp(
        403,
        text=cloudflare_html,
        headers={"cf-mitigated": "challenge"},
    )
    session = MagicMock()
    session.get = AsyncMock(return_value=fake)
    session.__aenter__ = AsyncMock(return_value=session)
    session.__aexit__ = AsyncMock(return_value=None)

    with patch("curl_cffi.requests.AsyncSession", return_value=session):
        data = await api.request_data()

    assert data is None
    assert api.last_error == "challenge"


@pytest.mark.asyncio
async def test_request_data_region_not_found() -> None:
    api = EONEnergiemonitorAPI("09175")
    fake = _FakeResp(404, text='"Region not found"')
    session = MagicMock()
    session.get = AsyncMock(return_value=fake)
    session.__aenter__ = AsyncMock(return_value=session)
    session.__aexit__ = AsyncMock(return_value=None)

    with patch("curl_cffi.requests.AsyncSession", return_value=session):
        data = await api.request_data()

    assert data is None
    assert api.last_error == "region_not_found"


@pytest.mark.asyncio
async def test_request_region_info_ok(region_data_poing: dict) -> None:
    api = EONEnergiemonitorAPI("09175135")
    fake = _FakeResp(200, data=region_data_poing)
    session = MagicMock()
    session.get = AsyncMock(return_value=fake)
    session.__aenter__ = AsyncMock(return_value=session)
    session.__aexit__ = AsyncMock(return_value=None)

    with patch("curl_cffi.requests.AsyncSession", return_value=session):
        data = await api.request_region_info()

    assert data["regionName"] == "Gemeinde Poing"
