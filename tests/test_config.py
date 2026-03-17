import os
import unittest
from unittest.mock import patch

from zenithai.config import Settings, get_settings


class SettingsTests(unittest.TestCase):
    def test_get_settings_uses_defaults(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            settings = get_settings()

        self.assertEqual(
            settings,
            Settings(
                stellarium_base_url="http://localhost:8090/api",
                timeout=10.0,
                model="openai:gpt-5.2",
            ),
        )

    def test_get_settings_reads_environment(self) -> None:
        with patch.dict(
            os.environ,
            {
                "ZENITHAI_STELLARIUM_BASE_URL": "http://example.test/api",
                "ZENITHAI_TIMEOUT": "2.5",
                "ZENITHAI_MODEL": "openai:test-model",
            },
            clear=True,
        ):
            settings = get_settings()

        self.assertEqual(settings.stellarium_base_url, "http://example.test/api")
        self.assertEqual(settings.timeout, 2.5)
        self.assertEqual(settings.model, "openai:test-model")
