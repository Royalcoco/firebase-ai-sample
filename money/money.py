import hashlib
import time

class FractalBlock:
    def __init__(self, index, timestamp, data, parent_hash, level=0, difficulty=3):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.parent_hash = parent_hash
        self.level = level  # Niveau fractal
        self.nonce = 0  # Utilisé pour le minage
        self.difficulty = difficulty  # Nombre de zéros requis en début de hash
        self.hash = self.mine_block()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.parent_hash}{self.level}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self):
        print(f"Mining block {self.index} at level {self.level}...")
        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith('0' * self.difficulty):
                print(f"Block mined! Nonce: {self.nonce}, Hash: {self.hash[:10]}...")
                return self.hash
            self.nonce += 1

    def __repr__(self):
        return (f"Block(Index: {self.index}, Level: {self.level}, Hash: {self.hash[:10]}..., "
                f"Nonce: {self.nonce}, Sub-blocks: {len(self.sub_blocks)})")

    def add_sub_block(self, data):
        sub_block = FractalBlock(
            index=f"{self.index}.{len(self.sub_blocks) + 1}",
            timestamp=time.time(),
            data=data,
            parent_hash=self.hash,
            level=self.level + 1,
            difficulty=self.difficulty
        )
        self.sub_blocks.append(sub_block)
        return sub_block

    sub_blocks = []  # Défini en dehors du constructeur pour supporter des sous-blocs multiples


class FractalBlockchain:
    def __init__(self, difficulty=3):
        self.blocks = [self.create_genesis_block(difficulty)]
        self.difficulty = difficulty

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
            difficulty=self.difficulty
        )
        self.blocks.append(new_block)
        return new_block

    def __repr__(self):
        chain_repr = "\n".join([str(block) for block in self.blocks])
        return f"Fractal Blockchain:\n{chain_repr}"


# Interface minière
def mining_interface():
    print("Welcome to the FractalLens Mining Interface!")
    blockchain = FractalBlockchain(difficulty=4)  # Augmentez la difficulté ici si nécessaire

    while True:
        print("\nMenu:")
        print("1. Mine a new block")
        print("2. Add and mine a sub-block to the last block")
        print("3. Display blockchain")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter data for the new block: ")
            blockchain.add_block(data)
        elif choice == '2':
            if len(blockchain.blocks) > 1:
                last_block = blockchain.blocks[-1]
                data = input(f"Enter data for a sub-block of Block {last_block.index}: ")
                last_block.add_sub_block(data)
            else:
                print("No blocks available to add a sub-block to.")
        elif choice == '3':
            print(blockchain)
        elif choice == '4':
            print("Exiting the mining interface. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Launch the mining interface
if __name__ == "__main__":
    mining_interface()
