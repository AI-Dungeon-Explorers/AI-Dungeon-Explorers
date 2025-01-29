class Economy:
    """Handles in-game economy, managing currency, rewards, and transactions."""

    def __init__(self):
        self.player_balances = {}

    def add_player(self, player_name):
        """Registers a new player with a starting balance."""
        if player_name not in self.player_balances:
            self.player_balances[player_name] = 100  # Default starting $AIDX balance
            print(f"{player_name} has been added with a balance of 100 $AIDX.")
        else:
            print(f"{player_name} already exists.")

    def get_balance(self, player_name):
        """Retrieves the balance of a player."""
        return self.player_balances.get(player_name, 0)

    def reward_player(self, player_name, amount):
        """Rewards a player with in-game currency ($AIDX)."""
        if player_name in self.player_balances:
            self.player_balances[player_name] += amount
            print(f"{player_name} earned {amount} $AIDX! New balance: {self.player_balances[player_name]}")
        else:
            print(f"Player {player_name} not found.")

    def spend_currency(self, player_name, amount):
        """Handles spending currency, ensuring sufficient balance."""
        if player_name in self.player_balances and self.player_balances[player_name] >= amount:
            self.player_balances[player_name] -= amount
            print(f"{player_name} spent {amount} $AIDX. Remaining balance: {self.player_balances[player_name]}")
            return True
        else:
            print(f"Transaction failed. Insufficient balance for {player_name}.")
            return False

# Example usage:
if __name__ == "__main__":
    game_economy = Economy()

    game_economy.add_player("Hero")
    game_economy.reward_player("Hero", 50)
    game_economy.spend_currency("Hero", 30)
    print(f"Final Balance: {game_economy.get_balance('Hero')} $AIDX"
