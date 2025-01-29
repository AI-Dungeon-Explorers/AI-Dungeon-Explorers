import unittest
from src.agents.ai_explorer import AIExplorer
from src.agents.enemy_ai import EnemyAI
from src.agents.npc_ai import NPCAI

class TestAIExplorer(unittest.TestCase):
    """Unit tests for AIExplorer functionality."""

    def setUp(self):
        self.explorer = AIExplorer("TestExplorer")

    def test_initial_attributes(self):
        """Test if AIExplorer initializes correctly."""
        self.assertEqual(self.explorer.name, "TestExplorer")
        self.assertEqual(self.explorer.experience, 0)

    def test_explore(self):
        """Test AIExplorer exploration decision-making."""
        test_dungeon = ["Path", "Monster", "Treasure"]
        self.explorer.explore(test_dungeon)
        self.assertGreaterEqual(len(self.explorer.exploration_history), 1)

    def test_learning_function(self):
        """Test AIExplorer learning from experience."""
        self.explorer.learn(10)
        self.assertEqual(self.explorer.experience, 10)

class TestEnemyAI(unittest.TestCase):
    """Unit tests for EnemyAI behavior."""

    def setUp(self):
        self.enemy = EnemyAI("ShadowBeast", "Normal")

    def test_initial_attributes(self):
        """Test if EnemyAI initializes with correct attributes."""
        self.assertEqual(self.enemy.name, "ShadowBeast")
        self.assertEqual(self.enemy.health, 100)

    def test_attack_decision(self):
        """Test if EnemyAI chooses an attack properly."""
        player_moves = ["attack", "block"]
        attack = self.enemy.choose_attack(player_moves)
        self.assertIn(attack, self.enemy.attack_patterns)

    def test_damage_taken(self):
        """Test if EnemyAI properly reduces health when attacked."""
        self.enemy.take_damage(20)
        self.assertEqual(self.enemy.health, 80)

class TestNPCAI(unittest.TestCase):
    """Unit tests for NPCAI interaction and dialogue."""
