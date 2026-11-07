"""HTTP client for the EON Energiemonitor API (V2, browser TLS)."""

from __future__ import annotations

import logging
from typing import Any, Dict, Optional, Tuple

try:
    from .const import API_BASE_URL, BROWSER_IMPERSONATE, REQUEST_TIMEOUT_S
    from .parsing import is_cloudflare_challenge
except ImportError:  # pragma: no cover - flat import for unit tests
    from const import API_BASE_URL, BROWSER_IMPERSONATE, REQUEST_TIMEOUT_S
    from parsing import is_cloudflare_challenge

try:
    from curl_cffi.requests import AsyncSession
except ImportError:  # pragma: no cover - installed by HA from manifest
    AsyncSession = None  # type: ignore[misc, assignment]

_LOGGER = logging.getLogger(__name__)


class EONEnergiemonitorAPI:
    """Fetch region-data and meter-data with Chrome TLS impersonation."""

    def __init__(self, region_code: str):
        """Initialize the API client."""
        self._base_url = API_BASE_URL
        self._region_code = region_code
        self.last_error: Optional[str] = None

    async def _get_json(self, url: str) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
        """Fetch JSON from the API. Returns (data, error_key)."""
        if AsyncSession is None:
            _LOGGER.error("curl_cffi is not installed; cannot reach the EON API")
            return None, "network"

        try:
            async with AsyncSession(impersonate=BROWSER_IMPERSONATE) as session:
                resp = await session.get(url, timeout=REQUEST_TIMEOUT_S)
        except TimeoutError:
            return None, "timeout"
        except Exception as err:  # noqa: BLE001 — map all transport failures
            _LOGGER.debug("API transport error for %s: %s", url, err)
            return None, "network"

        status = resp.status_code
        headers = dict(resp.headers or {})
        body = resp.text or ""

        if is_cloudflare_challenge(status, body, headers):
            return None, "challenge"

        if status == 404:
            return None, "region_not_found"
        if status != 200:
            return None, f"http_{status}"

        try:
            data = resp.json()
        except Exception:  # noqa: BLE001
            return None, "invalid_response"

        if not isinstance(data, dict):
            # Some 404 bodies are a JSON string; treat as invalid.
            if isinstance(data, str) and "not found" in data.lower():
                return None, "region_not_found"
            return None, "invalid_response"
        return data, None

    async def request_region_info(self) -> Optional[Dict[str, Any]]:
        """Request municipality metadata from region-data API."""
        url = f"{self._base_url}region-data?regionCode={self._region_code}"
        data, error = await self._get_json(url)
        if error:
            _LOGGER.debug("region-data failed for %s: %s", self._region_code, error)
            return None
        _LOGGER.debug("region-data loaded for %s", self._region_code)
        return data

    async def request_data(self) -> Optional[Dict[str, Any]]:
        """Request meter data from the EON Energiemonitor API."""
        self.last_error = None
        url = f"{self._base_url}meter-data?regionCode={self._region_code}"
        data, error = await self._get_json(url)
        if error:
            self.last_error = error
            if error == "region_not_found":
                _LOGGER.error(
                    "Region '%s' not found (HTTP 404). Check region_code.",
                    self._region_code,
                )
            elif error == "challenge":
                _LOGGER.error(
                    "Cloudflare challenge for region '%s'. Retry next interval.",
                    self._region_code,
                )
            else:
                _LOGGER.error("meter-data failed for %s: %s", self._region_code, error)
            return None
        _LOGGER.debug("meter-data loaded for %s", self._region_code)
        return data
