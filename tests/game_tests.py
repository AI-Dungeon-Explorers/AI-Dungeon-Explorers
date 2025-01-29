import unittest
from src.game.dungeon_generator import DungeonGenerator
from src.game.combat_system import CombatSystem, Character
from src.game.economy import Economy
from src.game.nft_manager import NFTManager

class TestDungeonGenerator(unittest.TestCase):
    """Unit tests for DungeonGenerator."""

    def setUp(self):
        self.dungeon = DungeonGenerator(width=5, height=5)

    def test_generate_dungeon(self):
        """Test if a dungeon is generated properly."""
        generated_map = self.dungeon.generate()
        self.assertEqual(len(generated_map), 5)  # Check height
        self.assertEqual(len(generated_map[0]), 5)  # Check width

    def test_spawn_points(self):
        """Test if spawn points are correctly identified."""
        self.dungeon.generate()
        spawn_points = self.dungeon.get_spawn_points()
        self.assertIsInstance(spawn_points, list)

class TestCombatSystem(unittest.TestCase):
    """Unit tests for Combat System."""

    def setUp(self):
        self.player = Character("Hero", 100, 10, 20)
        self.enemy = Character("Goblin", 80, 8, 15)
        self.combat = CombatSystem(self.player, self.enemy)

    def test_attack_reduces_health(self):
        """Test if attacking reduces opponent's health."""
        initial_enemy_health = self.enemy.health
        self.combat.attack(self.player, self.enemy)
        self.assertLess(self.enemy.health, initial_enemy_health)

    def test_battle_outcome(self):
        """Test if battle ends when one character's health reaches zero."""
        self.enemy.health = 1  # Set low health
        result = self.combat.battle()
        self.assertEqual(result, "Player Wins")

class TestEconomy(unittest.TestCase):
    """Unit tests for in-game Economy."""

    def setUp(self):
        self.economy = Economy()
        self.economy.add_player("Hero")

    def test_reward_player(self):
        """Test if rewarding player increases balance."""
        initial_balance = self.economy.get_balance("Hero")
        self.economy.reward_player("Hero", 50)
        self.assertEqual(self.economy.get_balance("Hero"), initial_balance + 50)

    def test_spend_currency(self):
        """Test if spending currency decreases balance correctly."""
        self.economy.reward_player("Hero", 100)
        success = self.economy.spend_currency("Hero", 50)
        self.assertTrue(success)
        self.assertEqual(self.economy.get_balance("Hero"), 50)

if __name__ == "__main__":
    uni
