import uuid
import time
import random
from queue import Queue
from hashlib import sha256
from typing import List, Dict

class Block:
    def __init__(self, index, previous_hash, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.nonce}"
        return sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", [])
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, transactions)
        self.chain.append(new_block)
        return new_block

class TopicQueue:
    def __init__(self):
        self.queue = Queue()
        self.history = []

    def add_task(self, task):
        self.queue.put(task)
        self.history.append(task)

    def remove_last_task(self):
        if not self.queue.empty():
            removed_task = self.queue.get()
            if len(self.history) > 0:
                last_two = self.history[-2:]
                print(f"Enregistrement des tâches précédentes: {last_two}")
                return last_two + [removed_task]
            return [removed_task]
        return []

class Miner:
    def __init__(self, name):
        self.name = name

    def mine(self, blockchain, transactions):
        last_block = blockchain.chain[-1]
        new_block = blockchain.add_block(transactions)
        print(f"Miner {self.name} a ajouté un bloc avec le hash {new_block.hash}")

def assign_color(index):
    colors = ["#FF0000", "#00FF00", "#0000FF"]
    return colors[index % len(colors)]

def visualize_blocks(blocks: List[Block]):
    print("Visualisation des blocs avec des couleurs...")
    for block in blocks:
        color = assign_color(block.index)
        print(f"Bloc {block.index} avec hash {block.hash} a la couleur {color}")

# Création des nœuds, blockchain et mineurs
topic_queue = TopicQueue()
blockchain = Blockchain()
miners = [Miner("Miner1"), Miner("Miner2"), Miner("Miner3")]

# Ajout de tâches
tasks = ["CommandA", "CommandB", "CommandC", "CommandD", "CommandE"]
for task in tasks:
    topic_queue.add_task(task)

# Suppression de la dernière tâche et enregistrement des précédentes
last_tasks = topic_queue.remove_last_task()

# Minage des informations des tâches restantes
for miner in miners:
    miner.mine(blockchain, last_tasks)

# Visualisation des blocs
visualize_blocks(blockchain.chain)

import numpy as np
import random
from typing import List, Tuple

class PixelBlock:
    def __init__(self, position: Tuple[int, int], state: str, color: Tuple[int, int, int]):
        self.position = position
        self.state = state  # "active", "inactive", "dead"
        self.color = color
        self.signature = self.generate_signature()

    def generate_signature(self):
        # Signature à double facteur pour chaque bloc
        return hash((self.position, self.state, self.color))

    def is_active(self):
        return self.state == "active"

    def is_dead(self):
        return self.state == "dead"

    def update_state(self, new_state: str):
        self.state = new_state
        self.signature = self.generate_signature()

class PixelGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = self.create_grid()
    
    def create_grid(self) -> List[List[PixelBlock]]:
        grid = []
        for x in range(self.width):
            row = []
            for y in range(self.height):
                color = self.calculate_color(x, y)
                state = random.choice(["active", "inactive", "dead"])
                row.append(PixelBlock((x, y), state, color))
            grid.append(row)
        return grid

    def calculate_color(self, x: int, y: int) -> Tuple[int, int, int]:
        # Dégradé simple pour les couleurs, pourrait être amélioré pour des effets plus complexes
        r = int(255 * (x / self.width))
        g = int(255 * (y / self.height))
        b = 255 - r - g
        return (r, g, b)

    def get_active_blocks(self) -> List[PixelBlock]:
        return [block for row in self.grid for block in row if block.is_active()]

    def get_dead_blocks(self) -> List[PixelBlock]:
        return [block for row in self.grid for block in row if block.is_dead()]

    def display_grid(self):
        for row in self.grid:
            for block in row:
                symbol = "A" if block.is_active() else ("D" if block.is_dead() else "I")
                print(f"{symbol}", end=" ")
            print()

    def reassemble_blocks(self, arrangement: List[Tuple[int, int]]):
        # Exemple de réassemblage, ici on prend des blocs et on les réarrange selon une liste de positions
        print("Réassemblage des blocs selon un nouvel arrangement...")
        for (x, y) in arrangement:
            block = self.grid[x][y]
            print(f"Block {block.position} avec état {block.state} et couleur {block.color}.")

# Initialisation de la grille de pixels
pixel_grid = PixelGrid(100, 10)

# Affichage initial de la grille
pixel_grid.display_grid()

# Récupération des blocs actifs
active_blocks = pixel_grid.get_active_blocks()
print(f"Nombre de blocs actifs: {len(active_blocks)}")

# Exemple de réassemblage de blocs
arrangement = [(random.randint(0, 99), random.randint(0, 9)) for _ in range(5)]
pixel_grid.reassemble_blocks(arrangement)

# Simuler des modifications d'états de certains blocs pour démonstration
pixel_grid.grid[0][0].update_state("dead")
pixel_grid.grid[50][5].update_state("inactive")

# Récupération des blocs morts
dead_blocks = pixel_grid.get_dead_blocks()
print(f"Nombre de blocs morts: {len(dead_blocks)}")

# Affichage final de la grille
pixel_grid.display_grid()

import numpy as np
import random
from typing import List, Tuple

class PixelBlock:
    def __init__(self, position: Tuple[int, int], state: str, color: Tuple[int, int, int]):
        self.position = position
        self.state = state  # "active", "inactive", "dead"
        self.color = color
        self.signature = self.generate_signature()

    def generate_signature(self):
        return hash((self.position, self.state, self.color))

    def is_active(self):
        return self.state == "active"

    def is_dead(self):
        return self.state == "dead"

    def update_state(self, new_state: str):
        self.state = new_state
        self.signature = self.generate_signature()

class PixelGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = self.create_grid()
        self.dead_blocks = []

    def create_grid(self) -> List[List[PixelBlock]]:
        grid = []
        for x in range(self.width):
            row = []
            for y in range(self.height):
                color = self.calculate_color(x, y)
                state = random.choice(["active", "inactive", "dead"])
                block = PixelBlock((x, y), state, color)
                if block.is_dead():
                    self.dead_blocks.append(block)
                row.append(block)
            grid.append(row)
        return grid

    def calculate_color(self, x: int, y: int) -> Tuple[int, int, int]:
        r = int(255 * (x / self.width))
        g = int(255 * (y / self.height))
        b = 255 - r - g
        return (r, g, b)

    def process_dead_blocks(self):
        # Simuler le traitement des pixels morts en augmentant leur valeur par un nouveau processeur
        print("Traitement des pixels morts pour réassociation et affichage...")
        for block in self.dead_blocks:
            self.reassociate_block(block)
            self.display_dead_block(block)

    def reassociate_block(self, block: PixelBlock):
        # Simuler une réassociation des blocs morts avec des nouvelles chaînes
        print(f"Réassociation du pixel mort à la position {block.position} avec d'autres blocs.")

    def display_dead_block(self, block: PixelBlock):
        # Afficher les informations sur le pixel mort
        print(f"Affichage du pixel mort {block.position} avec signature {block.signature} et couleur {block.color}")

    def count_dead_blocks(self) -> int:
        return len(self.dead_blocks)

    def display_grid(self):
        for row in self.grid:
            for block in row:
                symbol = "A" if block.is_active() else ("D" if block.is_dead() else "I")
                print(f"{symbol}", end=" ")
            print()

# Initialisation de la grille de pixels
pixel_grid = PixelGrid(100, 10)

# Affichage initial de la grille
pixel_grid.display_grid()

# Traitement des pixels morts
pixel_grid.process_dead_blocks()

# Nombre de pixels morts
dead_block_count = pixel_grid.count_dead_blocks()
print(f"Nombre total de pixels morts: {dead_block_count}")

# Enregistrement de la réponse (simulé)
kley_response = f"Kley pour les pixels morts: {dead_block_count}"
print(kley_response)
