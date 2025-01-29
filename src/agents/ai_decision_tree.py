class DecisionNode:
    """Represents a node in the AI decision tree."""
    
    def __init__(self, condition, yes_branch=None, no_branch=None):
        self.condition = condition
        self.yes_branch = yes_branch
        self.no_branch = no_branch

    def evaluate(self, context):
        """Evaluates the decision tree based on the given context."""
        if self.condition(context):
            if isinstance(self.yes_branch, DecisionNode):
                return self.yes_branch.evaluate(context)
            return self.yes_branch
        else:
            if isinstance(self.no_branch, DecisionNode):
                return self.no_branch.evaluate(context)
            return self.no_branch


# Example decision tree for an AI enemy
def is_player_near(context):
    return context.get("player_distance", 100) < 10

def is_enemy_low_health(context):
    return context.get("enemy_health", 100) < 30

# Constructing decision tree
retreat = DecisionNode(lambda ctx: True, "Retreat")
attack = DecisionNode(lambda ctx: True, "Attack")

enemy_decision_tree = DecisionNode(
    is_enemy_low_health,
    retreat,  # If low health → Retreat
    DecisionNode(is_player_near, attack, "Idle")  # If player is near → Attack, otherwise idle
)

# Example usage:
if __name__ == "__main__":
    test_context_1 = {"player_distance": 5, "enemy_health": 20}
    test_context_2 = {"player_distance": 50, "enemy_health": 80}

    print(f"Enemy decision (low health, player close): {enemy_decision_tree.evaluate(test_context_1)}")
    print(f"Enemy decision (healthy, player far): {enemy_decision_tree.evaluate(test_context_2)}")
