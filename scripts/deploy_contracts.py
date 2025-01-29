from web3 import Web3
import json

class ContractDeployer:
    """Deploys smart contracts to Ethereum-compatible networks."""

    def __init__(self, provider_url, private_key):
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        self.account = self.web3.eth.account.from_key(private_key)
        self.web3.eth.default_account = self.account.address
        print(f"Connected to blockchain: {self.web3.is_connected()}")
        print(f"Deploying from account: {self.account.address}")

    def load_contract(self, contract_json_path):
        """Loads compiled contract ABI and bytecode."""
        with open(contract_json_path, "r") as file:
            contract_data = json.load(file)
        return contract_data["abi"], contract_data["bytecode"]

    def deploy_contract(self, contract_json_path):
        """Deploys a smart contract and returns its address."""
        abi, bytecode = self.load_contract(contract_json_path)

        contract = self.web3.eth.contract(abi=abi, bytecode=byte
