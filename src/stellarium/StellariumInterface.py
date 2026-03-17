from src.stellarium.StellariumClient import StellariumClient

class StellariumInterface:
    def __init__(self):
        self.client = StellariumClient()

    def get_current_view(self) -> str:
        """Return the current Stellarium view state, including camera and selection info"""
        data = self.client._get("main/status")
        return str(data)
    
    def get_selected_object(self) -> str:
        """Return the currently selected Stellarium object"""
        data = self.client._get("objects/info", params = {"format": "json"})
        return str(data)
    
    def search_object(self, name:str) -> str:
        """Search Stellarium for an object by name"""
        data = self.client._get("objects/find", params={"str": name})
        return str(data)
    
    def center_on_object(self, name: str) -> str:
        """Find and center Stellarium on an object by name."""
        result = self.client._get("objects/find", params={"str": name})
        matches = result if isinstance(result, list) else [result]
        if not matches:
            return f"No object found for {name!r}."
        target = matches[0]
        self.client._post("main/focus", data={"target": target})
        return f"Centered on {target}."