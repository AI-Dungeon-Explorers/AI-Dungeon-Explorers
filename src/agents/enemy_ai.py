import random

class EnemyAI:
    """AI-driven enemy that adapts to player strategies and evolves over time."""

    def __init__(self, name, difficulty="Normal"):
        self.name = name
        self.difficulty = difficulty
        self.health = 100
        self.attack_patterns = ["basic attack", "defensive stance", "power strike"]
        self.adaptive_behavior = {}

    def choose_attack(self, player_history):
        """AI selects an attack based on player's previous actions."""
        if not player_history:
            return random.choice(self.attack_patterns)
        
        # Analyze player's past actions and adapt
        last_action = player_history[-1]
        if last_action in self.adaptive_behavior:
            return self.adaptive_behavior[last_action]
        else:
            chosen_attack = random.choice(self.attack_patterns)
            self.adaptive_behavior[last_action] = chosen_attack
            return chosen_attack

    def take_damage(self, damage):
        """Reduces enemy health when attacked."""
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health remaining: {self.health}")

    def evolve(self):
        """Enemy evolves by unlocking new attack patterns."""
        if self.difficulty == "Hard":
            self.attack_patterns.append("critical strike")
        elif self.difficulty == "Expert":
            self.attack_patterns.extend(["critical strike", "counter attack"])
        print(f"{self.name} has evolved! New attack patterns: {self.attack_patterns}")

# Example usage:
if __name__ == "__main__":
    enemy = EnemyAI("Shadow Beast", "Expert")
    player_moves = ["attack", "block", "attack"]
    
    for move in player_moves:
        enemy_move = 
