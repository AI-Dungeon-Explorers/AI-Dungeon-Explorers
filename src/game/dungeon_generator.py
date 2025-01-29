import random

class DungeonGenerator:
    """AI-powered procedural dungeon generation."""

    def __init__(self, width=5, height=5, seed=None):
        self.width = width
        self.height = height
        self.seed = seed if seed else random.randint(0, 9999)
        self.dungeon_map = []

    def generate(self):
        """Generate a randomized dungeon layout."""
        random.seed(self.seed)
        self.dungeon_map = [[random.choice(["Path", "Wall", "Treasure", "Monster", "Empty"]) 
                             for _ in range(self.width)] for _ in range(self.height)]
        return self.dungeon_map

    def display(self):
        """Prints the dungeon map in a human-readable format."""
        for row in self.dungeon_map:
            print(" | ".join(row))
        print("\n")

    def get_spawn_points(self):
        """Finds all possible spawn points for players and enemies."""
        spawn_points = []
        for y, row in enumerate(self.dungeon_map):
            for x, cell in enumerate(row):
                if cell == "Path":
                    spawn_points.append((x, y))
        return spawn_points

# Example usage:
if __name__ == "__main__":
    dungeon = DungeonGenerator(width=7, height=7)
    dungeon.generate()
    dungeon.display()
    print(f"Spawn Points: {dungeon.get_spawn_points()}")
