import hashlib
import json
from datetime import datetime

class AuditChain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0', meta="Genesis Block")

    def create_block(self, proof, previous_hash, meta):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'meta': meta,
            'hash': self.hash_block(len(self.chain) + 1)
        }
        self.chain.append(block)
        return block

    def hash_block(self, index):
        encoded_block = json.dumps(str(index), sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def get_last_block(self):
        return self.chain[-1]