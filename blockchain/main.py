import hashlib
import time
from ecdsa import SigningKey, VerifyingKey, SECP256k1
import json


class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.transactions = transactions
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{json.dumps([tx.to_dict() for tx in self.transactions], sort_keys=True)}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Transaction:
    def __init__(self, sender, recipient, amount, private_key=None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = None
        if private_key:
            self.sign_transaction(private_key)

    def to_dict(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
        }

    def sign_transaction(self, private_key):
        private_key = SigningKey.from_string(bytes.fromhex(private_key), curve=SECP256k1)
        message = json.dumps(self.to_dict(), sort_keys=True).encode()
        self.signature = private_key.sign(message).hex()

    def is_valid(self):
        if self.sender == "Genesis":
            return True  # Genesis transactions are valid by definition
        if not self.signature:
            return False
        public_key = VerifyingKey.from_string(bytes.fromhex(self.sender), curve=SECP256k1)
        message = json.dumps(self.to_dict(), sort_keys=True).encode()
        return public_key.verify(bytes.fromhex(self.signature), message)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.pending_transactions = []
        self.mining_reward = 1
    
    def create_genesis_block(self):
        return Block(0, "0", [Transaction("Genesis", "Genesis", 0)])
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def mine_pending_transactions(self, miner_address):
        block = Block(len(self.chain), self.get_latest_block().hash, self.pending_transactions)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        
        self.pending_transactions = [Transaction("System", miner_address, self.mining_reward)]
    
    def create_transaction(self, transaction):
        if not transaction.is_valid():
            raise Exception("Invalid transaction")
        self.pending_transactions.append(transaction)
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False

            for transaction in current_block.transactions:
                if not transaction.is_valid():
                    return False
        
        return True

# Example Usage
# Generate private and public keys for Alice
alice_private_key = SigningKey.generate(curve=SECP256k1)
alice_public_key = alice_private_key.get_verifying_key()

# Convert keys to hex for easy storage and sharing
alice_private_key_hex = alice_private_key.to_string().hex()
alice_public_key_hex = alice_public_key.to_string().hex()

# Create a transaction from Alice to Bob
transaction = Transaction(alice_public_key_hex, "Bob", 50, alice_private_key_hex)

# Create a blockchain and add the transaction
blockchain = Blockchain()
blockchain.create_transaction(transaction)

# Mine transactions
print("Starting mining...")
blockchain.mine_pending_transactions(alice_public_key_hex)

print("Blockchain valid?", blockchain.is_chain_valid())

# Print the blockchain
for block in blockchain.chain:
    print(f"Block {block.index} - Hash: {block.hash} - Previous Hash: {block.previous_hash}")
    for tx in block.transactions:
        print(f"  Transaction: {tx.to_dict()} - Signature: {tx.signature}")
