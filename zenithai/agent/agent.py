from langchain.agents import create_agent

from zenithai.config import get_settings
from zenithai.stellarium.interface import StellariumInterface


class Agent:
    def __init__(self) -> None:
        settings = get_settings()
        star_inf = StellariumInterface()
        self.messages: list[dict[str, str]] = []

        self.agent = create_agent(
            model=settings.model,
            tools=[
                star_inf.get_current_view,
                star_inf.get_selected_object,
                star_inf.search_object,
                star_inf.center_on_object,
            ],
            system_prompt=(
                "You are an astronomy assistant embedded with Stellarium. "
                "Use Stellarium tools for current sky/application state. "
                "Be concrete and observationally useful. "
                "If a control action was requested, do it and confirm what changed."
            ),
        )

    def ask(self, message: str) -> str:
        self.messages.append({"role": "user", "content": message})
        result = self.agent.invoke({"messages": self.messages})
        reply = self._extract_text(result)
        self.messages.append({"role": "assistant", "content": reply})
        return reply

    def _extract_text(self, result: object) -> str:
        if isinstance(result, dict):
            messages = result.get("messages")
            if isinstance(messages, list) and messages:
                return self._message_text(messages[-1])
        return str(result)

    def _message_text(self, message: object) -> str:
        content = getattr(message, "content", message)
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            parts: list[str] = []
            for item in content:
                if isinstance(item, str):
                    parts.append(item)
                    continue
                if isinstance(item, dict):
                    text = item.get("text")
                    if text:
                        parts.append(str(text))
            if parts:
                return "\n".join(parts)
        return str(content)
