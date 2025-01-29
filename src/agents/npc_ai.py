import random

class NPCAI:
    """AI-driven NPC that interacts with players and responds dynamically."""

    def __init__(self, name, role="merchant"):
        self.name = name
        self.role = role
        self.dialogues = {
            "merchant": ["Welcome, traveler! Looking for something special?",
                         "I have rare items for sale. Interested?",
                         "Gold or trade? Let's make a deal."],
            "guide": ["This dungeon is dangerous. Proceed with caution!",
                      "If you get lost, look for the glowing runes.",
                      "Many adventurers have perished here. Don't be the next one!"],
            "villager": ["Life is peaceful here, but we hear strange noises from the dungeon.",
                         "Have you met the elder? He knows ancient secrets.",
                         "Beware of the cursed ruins beyond the mountains."]
        }

    def interact(self):
        """NPC interacts with the player based on its role."""
        if self.role in self.dialogues:
            return random.choice(self.dialogues[self.role])
        else:
            return "I don't have much to say..."

    def give_quest(self):
        """Assigns a quest to the player if the NPC is a quest giver."""
        if self.role == "quest_giver":
            quests = [
                "Retrieve the ancient relic from the dungeon.",
                "Defeat the Shadow Beast haunting our village.",
                "Gather 5 rare herbs from the enchanted forest."
            ]
            return random.choice(quests)
        return "I don't have any quests for you."

# Example usage:
if __name__ == "__main__":
    npc_merchant = NPCAI("Garrik", "merchant")
    print(f"{npc_merchant.name}: {npc_merchant.interact()}")

    npc_guide = NPCAI("Elder Rylen", "guide")
    print(f"{npc_guide.name}: {npc_guide.interact()}")

    npc_quest_giver = NPCAI("Knight Commander", "quest_giver")
    print(f"{npc_quest_giver.name}: {npc_quest_giver.give_quest()}")
