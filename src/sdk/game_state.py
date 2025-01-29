import json

class GameState:
    """Manages and tracks the AI agent's game state."""

    def __init__(self):
        self.state = {
            "agent_id": None,
            "location": {"x": 0, "y": 0},
            "health": 100,
            "mana": 100,
            "inventory": [],
            "status_effects": [],
            "current_quest": None
        }

    def update_location(self, x, y):
        """Updates the agent's location."""
        self.state["location"] = {"x": x, "y": y}
        print(f"Agent moved to ({x}, {y})")

    def update_health(self, amount):
        """Modifies the agent's health value."""
        self.state["health"] = max(0, self.state["health"] + amount)
        print(f"Agent health updated: {self.state['health']}")

    def update_mana(self, amount):
  
