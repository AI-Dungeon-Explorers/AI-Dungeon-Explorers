import os
import json
import pandas as pd

class DataProcessor:
    """Processes AI training data for model training and analytics."""

    def __init__(self, data_dir="data/training_data"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

    def load_json_data(self, filename):
        """Loads AI training data from a JSON file."""
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
            print(f"Loaded data from {filename}.")
            return data
        except Exception as e:
            print(f"Error loading file {filename}: {e}")
            return None

    def save_json_data(self, filename, data):
        """Saves AI training data to a JSON file."""
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Data saved to {filename}.")
        except Exception as e:
            print(f"Error saving file {filename}: {e}")

    def convert_to_csv(self, json_filename, csv_filename):
        """Converts JSON training data to CSV format."""
        data = self.load_json_data(json_filename)
        if data:
            df = pd.DataFrame(data)
            df.to_csv(os.path.join(self.data_dir, csv_filename), index=False)
            print(f"Converted {json_filename} to {csv_filename}.")

    def filter_training_data(self, filename, key, min_value):
        """Filters AI training data based on a given key and threshold value."""
        data = self.load_json_data(filename)
        if data:
            filtered_data = [entry for entry in data if entry.get(key, 0) >= min_value]
            self.save_json_data(f"filtered_{filename}", filtered_data)
            print(f"Filtered {filename} based on {key} >= {min_value}.")

# Example usage:
if __name__ == "__main__":
    processor = DataProcessor()

    # Example data structure
    sample_data = [
        {"action": "attack", "success_rate": 85, "reward": 10},
        {"action": "defend", "success_rate": 60, "reward": 5},
        {"action": "run", "success_rate": 90, "reward": 2}
    ]

    processor.save_json_data("sample_training_data.json", sample_data)
    processor.convert_to_csv("sample_training_data.json", "sample_training_data.csv")
    processor.filter_training_data("sample_training_data.json", "success_rate", 80)
