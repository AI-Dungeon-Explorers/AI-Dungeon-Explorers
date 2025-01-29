import json
from datetime import datetime

class ReplaySystem:
    """Records and replays player actions for strategic analysis and AI training."""

    def __init__(self):
        self.replay_data = []

    def record_action(self, player, action, result):
        """Records a player's action and its outcome."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.replay_data.append({
            "timestamp": timestamp,
            "player": player,
            "action": action,
            "result": result
        })
        print(f"Recorded action: {player} performed {action} with result: {result}")

    def save_replay(self, filename):
        """Saves recorded actions to a JSON file for later review."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.replay_data, file, indent=4)
            print(f"Replay saved to {filename}")
        except Exception as e:
            print(f"Error saving replay: {e}")

    def load_replay(self, filename):
        """Loads a saved replay from a JSON file."""
        try:
            with open(filename, 'r') as file:
                self.replay_data = json.load(file)
            print(f"Replay loaded from {filename}")
        except Exception as e:
            print(f"Error loading replay: {e}")

    def display_replay(self):
        """Displays the recorded actions in a readable format."""
        for entry in self.replay_data:
            print(f"{entry['timestamp']} - {entry['player']} performed {entry['action']} resulting in {entry['result']}")

# Example usage:
if __name__ == "__main__":
    replay_system = ReplaySystem()
    replay_system.record_action("Hero", "Attack", "Success")
    replay_system.record_action("Hero", "Dodge", "Failed")
    replay_system.save_replay("replay_log.json")

    replay_system.load_replay("replay_log.json")
    replay_system.display_replay()
