from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

class Wallet:
    def __init__(self):
        self.key_pair = RSA.generate(2048)

    def sign_transaction(self, transaction):
        h = SHA256.new(transaction.encode())
        signature = pkcs1_15.new(self.key_pair).sign(h)
        return signature

    def verify_signature(self, transaction, signature):
        h = SHA256.new(transaction.encode())
        try:
            pkcs1_15.new(self.key_pair).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False

class Blockchain:
    # ... existing code ...

    def create_transaction(self, sender_wallet, recipient_address, amount):
        transaction = Transaction(sender_wallet.key_pair.publickey(), recipient_address, amount)
        signature = sender_wallet.sign_transaction(str(transaction))
        if sender_wallet.verify_signature(str(transaction), signature):
            self.pending_transactions.append(transaction)
        else:
            print("Transaction signature is invalid.")
            class Transaction:
    def __init__(self, from_address, to_address, amount):
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount

class Block:
    def __init__(self, transactions, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_string = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
        return hashlib.sha256(hash_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.mining_reward = 100

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def mine_block(self, miner_address):
        block = Block(self.pending_transactions, self.get_latest_block().hash)
        self.chain.append(block)

        self.pending_transactions = [
            Transaction(None, miner_address, self.mining_reward)
        ]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance_of_address(self, address):
        balance = 0
        for block in self.chain:
            for trans in block.transactions:
                if trans.from_address == address:
                    balance -= trans.amount
                if trans.to_address == address:
                    balance += trans.amount

        return balance

    def get_latest_block(self):
        return self.chain[-1]
    class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2  # Adjust this to make mining harder or easier

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(data, previous_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def get_latest_block(self):
        return self.chain[-1]

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        self.nonce = 0

    def calculate_hash(self):
        hash_string = str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(hash_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Block mined: " + self.hash)
        class Block:
    # ... existing code ...

    def is_valid(self, difficulty):
        return (
            self.hash == self.calculate_hash() and
            self.hash[:difficulty] == '0' * difficulty
        )

class Blockchain:
    # ... existing code ...

    def is_chain_valid(self, difficulty):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if not current_block.is_valid(difficulty):
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
    from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

class Wallet:
    def __init__(self):
        self.key_pair = RSA.generate(2048)

    def sign_transaction(self, transaction):
        h = SHA256.new(transaction.encode())
        signature = pkcs1_15.new(self.key_pair).sign(h)
        return signature

    def verify_signature(self, transaction, signature):
        h = SHA256.new(transaction.encode())
        try:
            pkcs1_15.new(self.key_pair).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False

class Blockchain:
    # ... existing code ...

    def create_transaction(self, sender_wallet, recipient_address, amount):
        transaction = Transaction(sender_wallet.key_pair.publickey(), recipient_address, amount)
        signature = sender_wallet.sign_transaction(str(transaction))
        if sender_wallet.verify_signature(str(transaction), signature):
            self.pending_transactions.append(transaction)
        else:
            print("Transaction signature is invalid.")
            from flask import Flask, render_template, request
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/create_transaction', methods=['POST'])
def create_transaction():
    sender_wallet = Wallet()  # You would actually get this from somewhere secure
    recipient_address = request.form.get('recipient_address')
    amount = request.form.get('amount')
    blockchain.create_transaction(sender_wallet, recipient_address, amount)
    return "Transaction created."


if __name__ == '__main__':
    app.run(debug=True)