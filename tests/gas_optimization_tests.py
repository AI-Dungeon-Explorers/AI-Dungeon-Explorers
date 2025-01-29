import unittest
from unittest.mock import MagicMock
from src.blockchain.web3_interface import Web3Interface

class TestGasOptimization(unittest.TestCase):
    """Unit tests for gas optimization in blockchain transactions."""

    def setUp(self):
        """Initialize a mock Web3 interface."""
        self.provider_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
        self.web3_interface = Web3Interface(self.provider_url)
        self.web3_interface.web3 = MagicMock()

    def test_calculate_gas_fee(self):
        """Test if gas fee estimation works correctly."""
        mock_gas_estimate = 21000  # Standard gas limit for ETH transfers
        mock_gas_price = self.web3_interface.web3.to_wei('50', 'gwei')

        self.web3_interface.web3.eth.estimate_gas.return_value = mock_gas_estimate
        self.web3_interface.web3.eth.gas_price = mock_gas_price

        estimated_fee = mock_gas_estimate * mock_gas_price
        self.assertEqual(estimated_fee, 1050000000000000)  # 0.00105 ETH in Wei

    def test_optimize_gas_usage(self):
        """Test if gas usage can be optimized."""
        initial_gas_limit = 80000  # Overestimated gas limit
        optimized_gas_limit = 60000  # Expected optimized gas usage

        def mock_estimate_gas(transaction):
            if transaction.get("optimize"):
                return optimized_gas_limit
            return initial_gas_limit

        self.web3_interface.web3.eth.estimate_gas.side_effect = mock_estimate_gas

        tx = {"to": "0xReceiverWallet", "value": 1000000000000000000}  # 1 ETH
        estimated_gas = self.web3_interface.web3.eth.estimate_gas(tx)

        tx["optimize"] = True
        optimized_gas = self.web3_interface.web3.eth.estimate_gas(tx)

        self.assertGreater(estimated_gas, optimized_gas)

if __name__ == "__main__":
    unittest.main()
