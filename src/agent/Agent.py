from langchain.agents import create_agent
from config import model
from src.stellarium.StellariumInterface import StellariumInterface
)

class Agent:
    def __init__(self):
        
        star_inf = StellariumInterface()

        self.agent = create_agent(
            model = model,
            tools = [
                star_inf.get_current_view,
                star_inf.get_selected_object,
                star_inf.search_object,
                star_inf.center_on_object
            ],
            system_prompt = (
                "You are an astronomy assistant embedded with Stellarium. "
                "Use Stellarium tools for current sky/application state. "
                "Be concrete and observationally useful. "
                "If a control action was requested, do it and confirm what changed."
            )
        )