import requests
from typing import Any, Dict, Optional

from config import STELLARIUM_BASE_URL, timeout


class StellariumClient:
    def __init__(self, base_url: str = STELLARIUM_BASE_URL):
        self.base_url = base_url.rstrip("/")

    def _get(self, path: str, params: Optional[dict] = None) -> Dict[str, Any]:
        resp = requests.get(f"{self.base_url}/{path.lstrip('/')}", params=params, timeout = timeout)
        resp.raise_for_status()
        return resp.json()
    
    def _post(self, path: str, data: Optional[dict] = None) -> Dict[str, Any]:
        resp = requests.post(f"{self.base_url}/{path.lstrip('/')}", data=data or {}, timeout = timeout)
        resp.raise_for_status()
        if resp.text.strip():
            return resp.json()
        return {"ok": True}