class AgentActions:
    """Defines AI agent actions and interactions using the GAME SDK."""

    def __init__(self, sdk):
        self.sdk = sdk

    def move(self, agent_id, direction):
        """Moves the AI agent in a specified direction."""
        response = self.sdk.send_action(agent_id, "move", {"direction": direction})
        if response:
            print(f"Agent {agent_id} moved {direction}. Response: {response}")
        return response

    def attack(self, agent_id, target_id):
        """Commands the AI agent to attack a specified target."""
        response = self.sdk.send_action(agent_id, "attack", {"target_id": target_id})
        if response:
            print(f"Agent {agent_id} attacked target {target_id}. Response: {response}")
        return response

    def interact(self, agent_id, object_id):
        """Interacts with objects in the environment (e.g., doors, items)."""
        response = self.sdk.send_action(agent_id, "interact", {"object_id": object_id})
        if response:
            print(f"Agent {agent_id} interacted with {object_id}. Response: {response}")
        return response

    def collect_item(self, agent_id, item_id):
        """Collects an item found in the environment."""
        response = self.sdk.send_action(agent_id, "collect_item", {"item_id": item_id})
        if response:
            print(f"Agent {agent_id} collected item {item_id}. Response: {response}")
        return response

    def use_ability(self, agent_id, ability_name):
        """Uses a special ability of the AI agent."""
        response = self.sdk.send_action(agent_id, "use_ability", {"ability_name": ability_name})
        if response:
            print(f"Agent {agent_id} used ability {ability_name}. Response: {response}")
      
