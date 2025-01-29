from web3 import Web3

class NFTManager:
    """Handles interactions with blockchain-based NFTs for dungeon assets and AI explorers."""

    def __init__(self, provider_url, contract_address, abi):
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract = self.web3.eth.contract(address=contract_address, abi=abi)

    def mint_nft(self, player_wallet, token_uri):
        """Mints a new NFT for the player."""
        try:
            txn = self.contract.functions.mint(player_wallet, token_uri).build_transaction({
                'from': player_wallet,
                'gas': 1000000,
                'gasPrice': self.web3.to_wei('5', 'gwei')
            })
            signed_txn = self.web3.eth.account.sign_transaction(txn, private_key="PRIVATE_KEY_HERE")
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f"NFT Minted! Transaction Hash: {tx_hash.hex()}")
        except Exception as e:
            print(f"Error minting NFT: {e}")

    def transfer_nft(self, from_wallet, to_wallet, token_id):
        """Transfers an NFT from one player to another."""
        try:
            txn = self.contract.functions.safeTransferFrom(from_wallet, to_wallet, token_id).build_transaction({
                'from': from_wallet,
                'gas': 500000,
                'gasPrice': self.web3.to_wei('5', 'gwei')
            })
            signed_txn = self.web3.eth.account.sign_transaction(txn, private_key="PRIVATE_KEY_HERE")
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f"NFT Transferred! Transaction Hash: {tx_hash.hex()}")
        except Exception as e:
            print(f"Error transferring NFT: {e}")

    def get_nft_owner(self, token_id):
        """Retrieves the owner of a given NFT."""
        try:
            owner = self.contract.functions.ownerOf(token_id).call()
            return owner
        except Exception as e:
            print(f"Error retrieving NFT owner: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    provider = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
    contract_addr = "0xYourNFTContractAddress"
