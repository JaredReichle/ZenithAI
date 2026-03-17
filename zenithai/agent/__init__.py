__all__ = ["Agent"]


def __getattr__(name: str):
    if name == "Agent":
        from .agent import Agent

        return Agent
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
