import json
import hashlib
from datetime import datetime
from web3 import Web3
import os

class AuditChain:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        self.contract_address = None
        self.contract = None
        self.account = None
        self.abi = None
        
        self.setup_contract()

    def setup_contract(self):
        if not self.w3.is_connected():
            return False
            
        # Hardhat default account 0
        self.account = self.w3.eth.accounts[0]
        self.w3.eth.default_account = self.account
        
        # Load ABI
        abi_path = os.path.join(os.path.dirname(__file__), '..', 'hardhat', 'artifacts', 'contracts', 'AuditChain.sol', 'AuditChain.json')
        if not os.path.exists(abi_path):
            print(f"WARNING: ABI not found at {abi_path}. Please compile the contract.")
            return
            
        with open(abi_path, 'r') as f:
            contract_json = json.load(f)
            self.abi = contract_json['abi']
            
        # Read the contract address deployed by scripts/deploy.js
        address_path = os.path.join(os.path.dirname(__file__), '..', 'hardhat', 'contract_address.txt')
        if os.path.exists(address_path):
            with open(address_path, 'r') as f:
                self.contract_address = f.read().strip()
                self.contract = self.w3.eth.contract(address=self.contract_address, abi=self.abi)
                return True
        else:
            return False

    def ensure_connected(self):
        if self.contract is not None and self.w3.is_connected():
            return True
        return self.setup_contract()

    def create_block(self, proof, previous_hash, meta):
        if not self.ensure_connected():
            print("ERROR: Contract not initialized. Returning dummy block.")
            return {"hash": "dummy_hash", "index": 0}
            
        timestamp = str(datetime.now())
        
        try:
            tx_hash = self.contract.functions.createBlock(
                timestamp,
                proof,
                previous_hash,
                meta
            ).transact()
            
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            
            return {
                "hash": tx_hash.hex(),
                "index": receipt.blockNumber
            }
        except Exception as e:
            print(f"Error calling contract: {e}")
            return {"hash": "error", "index": -1}

    def get_last_block(self):
        if not self.ensure_connected():
            return {'hash': '0', 'index': 0}
            
        try:
            count = self.contract.functions.getChainCount().call()
            if count == 0:
                return {'hash': '0', 'index': 0}
                
            last_block_data = self.contract.functions.getBlock(count - 1).call()
            
            index = last_block_data[0]
            # Since we need to return the transaction hash of the block, we mock it using the index if we can't get events easily
            mock_hash = f"0x{hashlib.sha256(str(index).encode()).hexdigest()[:40]}"
            
            return {
                'index': index,
                'timestamp': last_block_data[1],
                'proof': last_block_data[2],
                'previous_hash': last_block_data[3],
                'meta': last_block_data[4],
                'hash': mock_hash
            }
        except Exception as e:
            print(f"Error getting last block: {e}")
            return {'hash': '0', 'index': 0}
        
    @property
    def chain(self):
        """Returns the full chain for the API"""
        if not self.ensure_connected():
            return []
            
        try:
            count = self.contract.functions.getChainCount().call()
            chain_data = []
            
            for i in range(count):
                block = self.contract.functions.getBlock(i).call()
                index = block[0]
                mock_hash = f"0x{hashlib.sha256(str(index).encode()).hexdigest()[:40]}"
                
                chain_data.append({
                    'index': index,
                    'timestamp': block[1],
                    'proof': block[2],
                    'previous_hash': block[3],
                    'meta': block[4],
                    'hash': mock_hash
                })
                
            return chain_data
        except Exception as e:
            print(f"Error fetching chain: {e}")
            return []