import random
import numpy as np

class AITrainer:
    """AI training system using reinforcement learning principles."""

    def __init__(self):
        self.training_data = []
        self.weights = np.random.rand(3)  # Example weight vector for AI decision-making

    def collect_experience(self, state, action, reward):
        """Stores training data (state, action, reward) for AI learning."""
        self.training_data.append((state, action, reward))

    def train(self, epochs=1000, learning_rate=0.01):
        """Simulates AI learning from collected experiences using simple weight adjustments."""
        if not self.training_data:
            print("No training data available.")
            return

        for _ in range(epochs):
            state, action, reward = random.choice(self.training_data)
            self.weights += learning_rate * reward * np.array(state)  # Simple learning update
        
        print("Training complete. AI has adjusted its decision-making parameters.")

    def predict_action(self, state):
        """Predicts an action based on learned weights."""
        score = np.dot(self.weights, state)
        return "Attack" if score > 0 else "Defend"

# Example usage:
if __name__ == "__main__":
    trainer = AITrainer()
    
    # Simulated training data (state, action, reward)
    trainer.collect_experience([1, 0, -1], "Attack", 10)
    trainer.collect_experience([-1, 1, 0], "Defend", -5)
    
    trainer.train(epochs=500)
    
    test_state = [0.5, -0.2, 0.1]
    print(f"AI prediction for state {test_state}: {trainer.predict_action(test_state)}")
