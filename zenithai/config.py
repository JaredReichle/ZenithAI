import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    stellarium_base_url: str
    timeout: float
    model: str


def get_settings() -> Settings:
    return Settings(
        stellarium_base_url=os.getenv(
            "ZENITHAI_STELLARIUM_BASE_URL",
            "http://localhost:8090/api",
        ),
        timeout=float(os.getenv("ZENITHAI_TIMEOUT", "10")),
        model=os.getenv("ZENITHAI_MODEL", "openai:gpt-5.2"),
    )
