from web3 import Web3

class Web3Interface:
    """Manages blockchain interactions for AI Dungeon Explorers."""

    def __init__(self, provider_url):
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        if self.web3.is_connected():
            print("Connected to blockchain successfully!")
        else:
            print("Failed to connect to blockchain.")

    def get_balance(self, wallet_address):
        """Retrieves the balance of a given wallet in ETH."""
        try:
            balance_wei = self.web3.eth.get_balance(wallet_address)
            balance_eth = self.web3.from_wei(balance_wei, 'ether')
            return balance_eth
        except Exception as e:
            print(f"Error retrieving balance: {e}")
            return None

    def send_transaction(self, sender, receiver, amount, private_key):
        """Sends a transaction on the blockchain."""
        try:
            nonce = self.web3.eth.get_transaction_count(sender)
            txn = {
                'to': receiver
