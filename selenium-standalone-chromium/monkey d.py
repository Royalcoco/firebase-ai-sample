import hashlib
import random
import decimal
from decimal import Decimal
from typing import List, Tuple

# Configuration de la précision des décimales
decimal.getcontext().prec = 15

class Block:
    def __init__(self, index: int, previous_hash: str, data: str, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = decimal.Decimal(time.time())
        self.data = data
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", "Genesis Block")
        self.chain.append(genesis_block)

    def add_block(self, data: str) -> Block:
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, data)
        self.chain.append(new_block)
        return new_block

    def validate_chain(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.compute_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print(f"Block {block.index}: {block.hash}")

class Node:
    def __init__(self, id: int):
        self.id = id

    def solve_equation(self, equation: str) -> Decimal:
        # Pour l'exemple, simplification de la résolution d'une équation
        solution = Decimal(eval(equation))
        return solution

    def send_result(self, result: Decimal, blockchain: Blockchain):
        data = f"Node {self.id} result: {result}"
        blockchain.add_block(data)
        return data

def create_wallet(blocks: List[Block]) -> dict:
        wallet = {}
        for block in blocks:
            wallet[block.index] = block.data
        return wallet

def miner_validation(block: Block, difficulty: int = 2) -> bool:
    return block.hash.startswith('0' * difficulty)

# Simulation de la résolution d'une équation par des nœuds
equation = "12345.67890123456789 / 1.23456789"
nodes = [Node(i) for i in range(4)]
blockchain = Blockchain()

# Résolution de l'équation et enregistrement des résultats
for node in nodes:
    result = node.solve_equation(equation)
    node.send_result(result, blockchain)

# Validation de la chaîne par des mineurs
is_valid = blockchain.validate_chain()
print(f"Blockchain valid: {is_valid}")
blockchain.display_chain()

# Création de wallets pour gérer les unités de valeur
wallet = create_wallet(blockchain.chain)
print(f"Wallet: {wallet}")

import hashlib
import random
from decimal import Decimal, getcontext
from typing import List, Dict, Tuple

# Configuration de la précision des décimales
getcontext().prec = 62

class Wallet:
    def __init__(self, id: int):
        self.id = id
        self.values = []
        self.median_value = None

    def add_values(self, values: List[Decimal]):
        self.values.extend(values)
        self.values.sort()
        self.update_median()

    def update_median(self):
        if self.values:
            mid = len(self.values) // 2
            self.median_value = self.values[mid] if len(self.values) % 2 != 0 else (self.values[mid - 1] + self.values[mid]) / 2

    def get_values(self) -> List[Decimal]:
        return self.values

    def get_median_value(self) -> Decimal:
        return self.median_value

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = self.create_block("Genesis Block")
        self.chain.append(genesis_block)

    def create_block(self, data: str) -> Dict:
        index = len(self.chain)
        previous_hash = self.chain[-1]["hash"] if self.chain else "0"
        block = {
            "index": index,
            "previous_hash": previous_hash,
            "data": data,
            "hash": self.compute_hash(index, previous_hash, data)
        }
        self.chain.append(block)
        return block

    def compute_hash(self, index: int, previous_hash: str, data: str) -> str:
        block_string = f"{index}{previous_hash}{data}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def validate_chain(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current["hash"] != self.compute_hash(current["index"], current["previous_hash"], current["data"]):
                return False
            if current["previous_hash"] != previous["hash"]:
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print(f"Block {block['index']}: {block['hash']}")

class Node:
    def __init__(self, id: int):
        self.id = id

    def solve_complex_equation(self, variables: List[Decimal]) -> Decimal:
        # Simulation d'une résolution d'équation complexe
        result = sum(variables) / Decimal(len(variables))
        return result

def simulate_wallet_creation(num_wallets: int) -> List[Wallet]:
    wallets = []
    for i in range(num_wallets):
        wallet = Wallet(i)
        increasing_values = [Decimal(random.uniform(1, 10)) for _ in range(31)]
        decreasing_values = sorted([Decimal(random.uniform(10, 100)) for _ in range(9)], reverse=True)
        median_value = Decimal(random.uniform(5, 50))

        wallet.add_values(increasing_values)
        wallet.add_values(decreasing_values)
        wallet.add_values([median_value])
        
        wallets.append(wallet)
    return wallets

def compress_and_expand_data(data_size: int) -> Tuple[int, int]:
    compressed_size = data_size // 2
    expanded_size = compressed_size * 2
    return compressed_size, expanded_size

# Simulation du système

# 1. Création des wallets avec les valeurs croissantes, décroissantes et médianes
wallets = simulate_wallet_creation(5)
for wallet in wallets:
    print(f"Wallet {wallet.id} values: {wallet.get_values()}")
    print(f"Wallet {wallet.id} median value: {wallet.get_median_value()}")

# 2. Création d'une blockchain et ajout de blocs
blockchain = Blockchain()
for wallet in wallets:
    data = f"Wallet {wallet.id} median value: {wallet.get_median_value()}"
    blockchain.create_block(data)

# 3. Validation de la blockchain
is_valid = blockchain.validate_chain()
print(f"Blockchain valid: {is_valid}")
blockchain.display_chain()

# 4. Simulation de compression et d'expansion des données
initial_data_size = 21000  # en gigabytes, simulation d'une grande quantité de données
compressed_size, expanded_size = compress_and_expand_data(initial_data_size)
print(f"Data compressed to: {compressed_size} TB")
print(f"Data expanded to: {expanded_size} TB")

# 5. Calculs complexes et reboot du système de signatures avec 62 décimales
nodes = [Node(i) for i in range(41)]
complex_results = [node.solve_complex_equation(wallet.get_values()) for node, wallet in zip(nodes, wallets)]

for i, result in enumerate(complex_results):
    print(f"Node {nodes[i].id} complex result: {result}")

# 6. Validation
is_valid = blockchain.validate_chain()
print(f"Blockchain valid: {is_valid}")
blockchain.display_chain()

# 7. Simulation de la création de wallets avec des valeurs croissantes, décroissantes et médianes
wallets = simulate_wallet_creation(5)
for wallet in wallets:
    print(f"Wallet {wallet.id} values: {wallet.get_values()}")
    print(f"Wallet {wallet.id} median value: {wallet.get_median_value()}")
    print() # Saut de ligne pour la lisibilité
    
# 8. Création d'une blockchain et ajout de blocs
blockchain = Blockchain()
for wallet in wallets:
    data = f"Wallet {wallet.id} median value: {wallet.get_median_value()}"
    blockchain.create_block(data)
    
# 9. Validation de la blockchain
is_valid = blockchain.validate_chain()
print(f"Blockchain valid: {is_valid}")
blockchain.display_chain()

# 10. Simulation de la compression et
# de l'expansion des données
initial_data_size = 21000  # en gigabytes, simulation d'une grande quantité de données
compressed_size, expanded_size = compress_and_expand_data(initial_data_size)
print(f"Data compressed to: {compressed_size} TB")
print(f"Data expanded to: {expanded_size} TB")

# 11. Calculs complexes et reboot du système de signatures avec 62 décimales
nodes = [Node(i) for i in range(41)]
complex_results = [node.solve_complex_equation(wallet.get_values()) for node, wallet in zip(nodes, wallets)]

for i, result in enumerate(complex_results):
    print(f"Node {nodes[i].id} complex result: {result}")
    
# 12. Validation de la blockchain après les calculs complexes
is_valid = blockchain.validate_chain()
print(f"Blockchain valid: {is_valid}")
blockchain.display_chain()

# 13. Simulation de la création de wallets avec des valeurs croissantes, décroissantes et médianes
wallets = simulate_wallet_creation(5)
for wallet in wallets:
    print(f"Wallet {wallet.id} values: {wallet.get_values()}")
    print(f"Wallet {wallet.id} median value: {wallet.get_median_value()}")
    print() # Saut de ligne pour la lisibilité
    
# 14. Création d'une blockchain et ajout de blocs
blockchain = Blockchain()
for wallet in wallets:
    data = f"Wallet {wallet.id} median value: {wallet.get_median_value()}"
    blockchain.create_block(data)
    