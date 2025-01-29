import random

class CombatSystem:
    """AI-powered combat system for handling player and enemy battles."""

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def attack(self, attacker, defender):
        """Executes an attack and calculates damage."""
        attack_power = random.randint(attacker.attack_min, attacker.attack_max)
        defender.health -= attack_power
        print(f"{attacker.name} attacks {defender.name} for {attack_power} damage!")

    def battle(self):
        """Simulates a battle between the player and an AI-controlled enemy."""
        print(f"Battle begins: {self.player.name} vs {self.enemy.name}")

        while self.player.health > 0 and self.enemy.health > 0:
            self.attack(self.player, self.enemy)
            if self.en
