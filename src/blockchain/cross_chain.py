from web3 import Web3

class CrossChainBridge:
    """Handles cross-chain compatibility for AI Dungeon Explorers."""

    def __init__(self, source_chain_rpc, target_chain_rpc):
        self.source_web3 = Web3(Web3.HTTPProvider(source_chain_rpc))
        self.target_web3 = Web3(Web3.HTTPProvider(target_chain_rpc))

        if self.source_web3.is_connected():
            print("Connected to Source Blockchain!")
        else:
            print("Failed to connect to Source Blockchain.")

        if self.target_web3.is_connected():
            print("Connected to Target Blockchain!")
        else:
            print("Failed to connect to Target Blockchain.")

    def lock_tokens(self, sender, amount, private_key, contract_address, abi):
        """Locks tokens on the source chain to initiate a cross-chain transfer."""
        try:
            contract = self.source_web3.eth.contract(address=contract_address, abi=abi)
            txn = contract.functions.lockTokens(sender, amount).build_transaction({
                'from': sender,
                'gas': 200000,
                'gasPrice': self.source_web3.to_wei('50', 'gwei'),
                'nonce': self.source_web3.eth.get_transaction_count(sender),
            })
            signed_txn = self.source_web3.eth.account.sign_transaction(txn, private_key)
            tx_hash = self.source_web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f"Tokens locked on source chain! Transaction Hash: {tx_hash.hex()}")
            return tx_hash.hex()
        except Exception as e:
            print(f"Failed to lock tokens: {e}")
            return None

    def mint_tokens(self, recipient, amount, contract_address, abi):
        """Mints equivalent tokens on the target chain."""
        try:
            contract = self.target_web3.eth.contract(address=contract_address, abi=abi)
            txn = contract.functions.mintTokens(recipient, amount).transact({'from': recipient})
            print(f"Tokens minted on target chain for {recipient}!")
            return txn
        except Exception as e:
            print(f"Failed to mint tokens: {e}")
            return None

    def transfer_nft(self, sender, recipient, token_id, contract_address, abi):
        """Transfers an NFT between chains using a locking mechanism."""
        try:
            contract = self.source_web3.eth.contract(address=contract_address, abi=abi)
            txn = contract.functions.lockNFT(sender, token_id).build_transaction({
                'from': sender,
                'gas': 300000,
                'gasPrice': self.source_web3.to_wei('50', 'gwei'),
                'nonce': self.source_web3.eth.get_transaction_count(sender),
            })
            signed_txn = self.source_web3.eth.account.sign_transaction(txn, private_key)
            tx_hash = self.source_web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f"NFT locked on source chain! Transaction Hash: {tx_hash.hex()}")

            # Mint NFT on target chain
            target_contract = self.target_web3.eth.contract
