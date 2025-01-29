import matplotlib.pyplot as plt

class TokenomicsSimulation:
    """Simulates the flow of $AIDX tokens in the AI Dungeon Explorers economy."""

    def __init__(self, initial_supply=1_000_000_000, burn_rate=0.01, reward_rate=0.05, transaction_volume=100_000):
        """
        :param initial_supply: Total supply of $AIDX tokens
        :param burn_rate: Percentage of tokens burned per transaction
        :param reward_rate: Percentage of tokens issued as player rewards
        :param transaction_volume: Number of token transactions per cycle
        """
        self.initial_supply = initial_supply
        self.current_supply = initial_supply
        self.burn_rate = burn_rate
        self.reward_rate = reward_rate
        self.transaction_volume = transaction_volume
        self.history = []

    def simulate_cycle(self, cycles=50):
        """Simulates the token economy over a number of cycles (e.g., months)."""
        for cycle in range(cycles):
            burned = self.current_supply * self.burn_rate
            rewards_issued = self.transaction_volume * self.reward_rate
            self.current_supply -= burned
            self.current_supply += rewards_issued
            self.history.append(self.current_supply)
            print(f"Cycle {cycle+1}: Burned {burned:.2f}, Rewards Issued {rewards_issued:.2f}, Supply {self.current_supply:.2f}")

    def plot_simulation(self):
        """Plots the token supply change over time."""
        plt.figure(figsize=(10, 5))
        plt.plot(self.history, 

