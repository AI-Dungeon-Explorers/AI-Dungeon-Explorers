import requests

class GameSDKAPI:
    """Handles communication with the GAME SDK for AI Dungeon Explorers."""

    def __init__(self, base_url):
        self.base_url = base_url

    def send_action(self, agent_id, action, params={}):
        """Sends an action request to the GAME SDK."""
        url = f"{self.base_url}/agent/{agent_id}/action"
        payload = {
            "action": action,
            "params": params
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Request failed: {e}")
            return None

    def get_agent_state(self, agent_id):
        """Retrieves the current state of an AI agent from the GAME SDK."""
        url = f"{self.base_url}/agent/{agent_id}/state"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Request failed: {e}")
            return None

    def register_agent(self, agent_name, attributes):
        """Registers a new AI agent in the GAME SDK."""
        url = f"{self.base_url}/agent/register"
        payload = {
            "name": agent_name,
            "attributes": attributes
        }
        try:
            response =
