import hashlib
import time

class FractalBlock:
    def __init__(self, index, timestamp, data, parent_hash, level=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.parent_hash = parent_hash
        self.level = level  # Niveau fractal (0 = principal)
        self.sub_blocks = []  # Sous-blocs fractals
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.parent_hash}{self.level}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_sub_block(self, data):
        sub_block = FractalBlock(
            index=f"{self.index}.{len(self.sub_blocks) + 1}",
            timestamp=time.time(),
            data=data,
            parent_hash=self.hash,
            level=self.level + 1
        )
        self.sub_blocks.append(sub_block)
        return sub_block

    def __repr__(self):
        return (f"Block(Index: {self.index}, Level: {self.level}, Hash: {self.hash[:10]}..., "
                f"Sub-blocks: {len(self.sub_blocks)})")


class FractalBlockchain:
    def __init__(self):
        self.blocks = [self.create_genesis_block()]

    def create_genesis_block(self):
        return FractalBlock(index=0, timestamp=time.time(), data="Genesis Block", parent_hash="0", level=0)

    def add_block(self, data):
        parent_block = self.blocks[-1]
        new_block = FractalBlock(
            index=len(self.blocks),
            timestamp=time.time(),
            data=data,
            parent_hash=parent_block.hash,
            level=0
        )
        self.blocks.append(new_block)
        return new_block

    def __repr__(self):
        chain_repr = "\n".join([str(block) for block in self.blocks])
        return f"Fractal Blockchain:\n{chain_repr}"


# Example: Create a fractal blockchain and add blocks/sub-blocks
blockchain = FractalBlockchain()

# Add main blocks
main_block_1 = blockchain.add_block("Main Block 1 Data")
main_block_2 = blockchain.add_block("Main Block 2 Data")

# Add sub-blocks to Main Block 1
sub_block_1_1 = main_block_1.add_sub_block("Sub Block 1.1 Data")
sub_block_1_2 = main_block_1.add_sub_block("Sub Block 1.2 Data")

# Add sub-blocks to Sub Block 1.1
sub_block_1_1_1 = sub_block_1_1.add_sub_block("Sub Block 1.1.1 Data")

# Add sub-blocks to Main Block 2
sub_block_2_1 = main_block_2.add_sub_block("Sub Block 2.1 Data")

# Print the blockchain
print(blockchain)

# Print details of Main Block 1
print("\nDetails of Main Block 1 and its Sub-blocks:")
print(main_block_1)
for sub_block in main_block_1.sub_blocks:
    print("  ", sub_block)
    for sub_sub_block in sub_block.sub_blocks:
        print("      ", sub_sub_block)
