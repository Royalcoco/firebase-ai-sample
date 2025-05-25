import hashlib
import time
import random
import matplotlib.pyplot as plt
import networkx as nx

class FractalBlock:
    def __init__(self, index, timestamp, data, parent_hash, level=0, difficulty=3, reward=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.parent_hash = parent_hash
        self.level = level
        self.nonce = 0
        self.difficulty = difficulty
        self.reward = reward
        self.hash = self.mine_block()
        self.sub_blocks = []

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.parent_hash}{self.level}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self):
        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith('0' * self.difficulty):
                return self.hash
            self.nonce += 1

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


class FractalBlockchain:
    def __init__(self, difficulty=3, initial_reward=50):
        self.blocks = [self.create_genesis_block(difficulty)]
        self.difficulty = difficulty
        self.reward = initial_reward

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
        self.reward = max(1, self.reward // 2)
        return new_block

    def visualize(self):
        graph = nx.DiGraph()

        def add_block_to_graph(block, parent=None):
            node_label = f"{block.index} (L{block.level})"
            graph.add_node(node_label)
            if parent:
                graph.add_edge(parent, node_label)
            for sub_block in block.sub_blocks:
                add_block_to_graph(sub_block, node_label)

        for block in self.blocks:
            add_block_to_graph(block)

        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold")
        plt.title("Fractal Blockchain Visualization")
        plt.show()


# Simulate Blockchain
blockchain = FractalBlockchain(difficulty=4)

# Adding Blocks and Sub-Blocks
main_block_1 = blockchain.add_block("Main Block 1")
main_block_2 = blockchain.add_block("Main Block 2")
sub_block_1 = main_block_1.add_sub_block("Sub Block 1.1", reward=10)
sub_block_2 = main_block_1.add_sub_block("Sub Block 1.2", reward=15)
sub_sub_block = sub_block_1.add_sub_block("Sub Sub Block 1.1.1", reward=5)

# Visualize the Blockchain Structure
blockchain.visualize()
