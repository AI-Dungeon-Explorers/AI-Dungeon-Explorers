class AIExplorer:
    """AI-powered dungeon explorer that learns and adapts in real-time."""

    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.exploration_history = []

    def explore(self, dungeon_map):
        """Simulate AI exploring a dynamically generated dungeon."""
        print(f"{self.name} is exploring the dungeon...")
        for room in dungeon_map:
            decision = self.make_decision(room)
            self.exploration_history.append((room, decision))
            print(f"{self.name} encounters {room} and chooses to {decision}.")

    def make_decision(self, room):
        """AI decision-making logic based on exploration history."""
        if room == "Treasure":
            return "collect loot"
        elif room == "Monster":
            return "fight" if self.experience > 10 else "run away"
        else:
            return "move forward"

    def learn(self, experience_points):
        """AI learns from past explorations and improves its decision-making."""
        self.experience += experience_points
        print(f"{self.name} gains {experience_points} experience points!")

# Example usage:
if __name__ == "__main__":
    dungeon = ["Path", "Monster", "T
