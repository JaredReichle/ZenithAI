def _load_agent_class():
    from zenithai.agent.agent import Agent

    return Agent


def main() -> None:
    agent_cls = _load_agent_class()
    agent = agent_cls()

    print("ZenithAI chat")
    print("Type 'exit' to quit.")

    while True:
        try:
            message = input("You> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if not message:
            continue

        if message.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        response = agent.ask(message)
        print(f"ZenithAI> {response}")
