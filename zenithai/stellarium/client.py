from typing import Any

import requests

from zenithai.config import get_settings


class StellariumClient:
    def __init__(self, base_url: str | None = None) -> None:
        settings = get_settings()
        self.base_url = (base_url or settings.stellarium_base_url).rstrip("/")
        self.timeout = settings.timeout

    def _get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        resp = requests.get(
            f"{self.base_url}/{path.lstrip('/')}",
            params=params,
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()

    def _post(self, path: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        resp = requests.post(
            f"{self.base_url}/{path.lstrip('/')}",
            data=data or {},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        if resp.text.strip():
            return resp.json()
        return {"ok": True}
