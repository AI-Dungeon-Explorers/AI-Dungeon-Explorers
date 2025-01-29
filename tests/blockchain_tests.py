import unittest
from unittest.mock import MagicMock
from src.blockchain.web3_interface import Web3Interface

class TestWeb3Interface(unittest.TestCase):
    """Unit tests for blockchain interactions."""

    def setUp(self):
        """Initialize a mock Web3 interface."""
        self.provider_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
        self.web3_interface = Web3Interface(self.provider_url)
        self.web3_interface.web3 = MagicMock()

    def test_get_balance(self):
        """Test if wallet balance retrieval works correctly."""
        mock_balance = 1000000000000000000  # 1 ETH in Wei
        self.web3_interface.web3.eth.get_balance.return_value = mock_balance

        wallet_address = "0xYourWalletAddress"
        balance = self.web3_interface.get_balance(wallet_address)

        self.assertEqual(balance, 1.0)  # Converted from Wei to ETH

    def test_send_transaction(self):
        """Test if transaction sending works correctly."""
        mock_tx_hash = "0xabcdef1234567890"
        self.web3_interface.web3.eth.send_raw_transaction.return_value = mock_tx_hash

        sender = "0xSenderWallet"
        receiver = "0xReceiverWallet"
        amount = 0.1
        private_key = "PRIVATE_KEY"

        tx_hash = self.web3_interface.send_transaction(sender, receiver, amount, private_key)
        self.assertEqual(tx_hash, mock_tx_hash)

if __name__ == "__main__":
    unittest.main()
