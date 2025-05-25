import hashlib
import time
import random

class FractalBlock:
    def __init__(self, index, timestamp, data, parent_hash, level=0, difficulty=3, reward=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.parent_hash = parent_hash
        self.level = level  # Niveau fractal
        self.nonce = 0  # Utilisé pour le minage
        self.difficulty = difficulty  # Nombre de zéros requis
        self.reward = reward  # Récompense pour le minage
        self.hash = self.mine_block()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.parent_hash}{self.level}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self):
        print(f"Mining block {self.index} at level {self.level}...")
        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith('0' * self.difficulty):
                print(f"Block mined! Nonce: {self.nonce}, Hash: {self.hash[:10]}..., Reward: {self.reward} tokens")
                return self.hash
            self.nonce += 1

    def __repr__(self):
        return (f"Block(Index: {self.index}, Level: {self.level}, Hash: {self.hash[:10]}..., "
                f"Nonce: {self.nonce}, Reward: {self.reward}, Sub-blocks: {len(self.sub_blocks)})")

    def add_sub_block(self, data, reward):
        sub_block = FractalBlock(
            index=f"{self.index}.{len(self.sub_blocks) + 1}",
            timestamp=time.time(),
            data=data,
            parent_hash=self.hash,
            level=self.level + 1,
            difficulty=self.difficulty,
            reward=reward
        )
        self.sub_blocks.append(sub_block)
        return sub_block

    sub_blocks = []


class FractalBlockchain:
    def __init__(self, difficulty=3, initial_reward=50):
        self.blocks = [self.create_genesis_block(difficulty)]
        self.difficulty = difficulty
        self.reward = initial_reward  # Récompense initiale pour les mineurs

    def create_genesis_block(self, difficulty):
        return FractalBlock(index=0, timestamp=time.time(), data="Genesis Block", parent_hash="0", level=0, difficulty=difficulty)

    def add_block(self, data):
        parent_block = self.blocks[-1]
        new_block = FractalBlock(
            index=len(self.blocks),
            timestamp=time.time(),
            data=data,
            parent_hash=parent_block.hash,
            level=0,
            difficulty=self.difficulty,
            reward=self.reward
        )
        self.blocks.append(new_block)
        # Réduire la récompense pour les prochains blocs (halving)
        self.reward = max(1, self.reward // 2)
        return new_block

    def __repr__(self):
        chain_repr = "\n".join([str(block) for block in self.blocks])
        return f"Fractal Blockchain:\n{chain_repr}"


# Interface utilisateur améliorée avec visualisation graphique et récompenses
def mining_interface():
    print("Welcome to the Enhanced FractalLens Mining Interface!")
    blockchain = FractalBlockchain(difficulty=4)  # Augmentez la difficulté pour un minage plus complexe

    users = {}  # Stocker les soldes des mineurs

    while True:
        print("\nMenu:")
        print("1. Mine a new block")
        print("2. Add and mine a sub-block to the last block")
        print("3. Display blockchain")
        print("4. Display user balances")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter data for the new block: ")
            miner = input("Enter miner's name: ")
            new_block = blockchain.add_block(data)
            # Récompense le mineur
            users[miner] = users.get(miner, 0) + new_block.reward
        elif choice == '2':
            if len(blockchain.blocks) > 1:
                last_block = blockchain.blocks[-1]
                data = input(f"Enter data for a sub-block of Block {last_block.index}: ")
                miner = input("Enter miner's name: ")
                reward = random.randint(5, 15)  # Récompense aléatoire pour les sous-blocs
                new_sub_block = last_block.add_sub_block(data, reward)
                # Récompense le mineur
                users[miner] = users.get(miner, 0) + new_sub_block.reward
            else:
                print("No blocks available to add a sub-block to.")
        elif choice == '3':
            print(blockchain)
        elif choice == '4':
            print("\nUser Balances:")
            for user, balance in users.items():
                print(f"{user}: {balance} tokens")
        elif choice == '5':
            print("Exiting the mining interface. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Lancer l'interface utilisateur
if __name__ == "__main__":
    mining_interface()
