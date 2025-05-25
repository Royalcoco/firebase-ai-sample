import hashlib
import time
import json
from Crypto.PublicKey import RSA

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

class Block:
    def __init__(self, transactions, previous_hash):
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({"timestamp": self.timestamp, "transactions": [vars(t) for t in self.transactions], "previous_hash": self.previous_hash, "nonce": self.nonce}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Block mined: ", self.hash)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block([Transaction("", "", 0)], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

class Wallet:
    def __init__(self):
        self.key_pair = RSA.generate(2048)

    def get_address(self):
        return hashlib.sha256(self.key_pair.publickey().exportKey(format='PEM')).hexdigest()

    def send_transaction(self, recipient_address, amount, blockchain):
        transaction = Transaction(self.get_address(), recipient_address, amount)
        block = Block([transaction], blockchain.get_latest_block().hash)
        blockchain.add_block(block)

# Test the code
blockchain = Blockchain()
wallet1 = Wallet()
wallet2 = Wallet()

wallet1.send_transaction(wallet2.get_address(), 50, blockchain)
wallet2.send_transaction(wallet1.get_address(), 25, blockchain)

for block in blockchain.chain:
    print(vars(block))
    for transaction in block.transactions:
        print("Sender:", transaction.sender)
        print("Recipient:", transaction.recipient)
        print("Amount:", transaction.amount)
        print("Hash:", block.hash)
        print("Transaction:", transaction)
        print("----------------------------")
        print("Blockchain validation:")
        is_valid = True
        for i in range(1, len(blockchain.chain)):
            current_block = blockchain.chain[i]
            previous_block = blockchain.chain[i - 1]
            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                is_valid = False
                print("Invalid block hash at index", i)
            # Check if the previous block's hash matches the current block's previous hash
            if current_block.previous_hash != previous_block.hash:
                is_valid = False
                print("Invalid previous hash at index", i)
            # Check if the block has been mined with the correct difficulty
            if current_block.hash[:blockchain.difficulty] != "0" * blockchain.difficulty:
                is_valid = False
                print("Invalid block mining at index", i)
        if is_valid:
            print("Blockchain is valid.")
        else:
            print("Blockchain is invalid.")
            