import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from zenithai import cli


class FakeAgent:
    def __init__(self) -> None:
        self.messages: list[str] = []

    def ask(self, message: str) -> str:
        self.messages.append(message)
        return f"echo: {message}"


class CliTests(unittest.TestCase):
    def test_main_runs_chat_loop(self) -> None:
        output = io.StringIO()
        created_agents: list[FakeAgent] = []

        def build_agent() -> FakeAgent:
            agent = FakeAgent()
            created_agents.append(agent)
            return agent

        with patch("zenithai.cli._load_agent_class", return_value=build_agent):
            with patch("builtins.input", side_effect=["hello", "quit"]):
                with redirect_stdout(output):
                    cli.main()

        self.assertEqual(created_agents[0].messages, ["hello"])
        self.assertIn("ZenithAI chat", output.getvalue())
        self.assertIn("ZenithAI> echo: hello", output.getvalue())
        self.assertTrue(output.getvalue().strip().endswith("Goodbye."))
