import hashlib
import time
import random
import matplotlib.pyplot as plt
import networkx as nx


class FractalBlock:
    def __init__(self, index, timestamp, data, parent_hash, level=0, difficulty=3, reward=0, transactions=None):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.parent_hash = parent_hash
        self.level = level
        self.nonce = 0
        self.difficulty = difficulty
        self.reward = reward
        self.transactions = transactions if transactions else []  # Liste des transactions dans le bloc
        self.hash = self.mine_block()
        self.sub_blocks = []

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.parent_hash}{self.level}{self.nonce}{self.transactions}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self):
        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith('0' * self.difficulty):
                return self.hash
            self.nonce += 1

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def add_sub_block(self, data, reward, transactions=None):
        sub_block = FractalBlock(
            index=f"{self.index}.{len(self.sub_blocks) + 1}",
            timestamp=time.time(),
            data=data,
            parent_hash=self.hash,
            level=self.level + 1,
            difficulty=self.difficulty,
            reward=reward,
            transactions=transactions
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

    def add_block(self, data, transactions=None):
        parent_block = self.blocks[-1]
        new_block = FractalBlock(
            index=len(self.blocks),
            timestamp=time.time(),
            data=data,
            parent_hash=parent_block.hash,
            level=0,
            difficulty=self.difficulty,
            reward=self.reward,
            transactions=transactions
        )
        self.blocks.append(new_block)
        self.reward = max(1, self.reward // 2)  # Réduction progressive de la récompense
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


class Wallet:
    def __init__(self):
        self.accounts = {}  # Stockage des comptes {nom_utilisateur: balance}

    def create_wallet(self, username):
        if username in self.accounts:
            return f"Wallet for {username} already exists."
        self.accounts[username] = 0
        return f"Wallet created for {username}."

    def get_balance(self, username):
        return self.accounts.get(username, "Wallet does not exist.")

    def update_balance(self, username, amount):
        if username in self.accounts:
            self.accounts[username] += amount
            return f"{username}'s balance updated. New balance: {self.accounts[username]}"
        return "Wallet does not exist."

    def send_tokens(self, sender, receiver, amount):
        if sender not in self.accounts or receiver not in self.accounts:
            return "Sender or receiver wallet does not exist."
        if self.accounts[sender] < amount:
            return "Insufficient balance."
        self.accounts[sender] -= amount
        self.accounts[receiver] += amount
        return f"Transaction successful: {amount} tokens sent from {sender} to {receiver}."


# Interface Utilisateur
def mining_interface():
    print("Welcome to the Enhanced FractalLens Mining Interface with Wallets!")
    blockchain = FractalBlockchain(difficulty=4)
    wallet = Wallet()

    while True:
        print("\nMenu:")
        print("1. Create Wallet")
        print("2. Mine a Block")
        print("3. Send Tokens")
        print("4. Display Blockchain")
        print("5. Display Wallet Balances")
        print("6. Visualize Blockchain Structure")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username for the wallet: ")
            print(wallet.create_wallet(username))
        elif choice == '2':
            miner = input("Enter miner's wallet username: ")
            if miner not in wallet.accounts:
                print("Wallet does not exist. Please create a wallet first.")
                continue
            data = input("Enter data for the block: ")
            new_block = blockchain.add_block(data)
            wallet.update_balance(miner, new_block.reward)
            print(f"Block mined by {miner}! Reward: {new_block.reward} tokens.")
        elif choice == '3':
            sender = input("Enter sender's wallet username: ")
            receiver = input("Enter receiver's wallet username: ")
            amount = int(input("Enter amount to send: "))
            print(wallet.send_tokens(sender, receiver, amount))
        elif choice == '4':
            for block in blockchain.blocks:
                print(f"Block {block.index} | Hash: {block.hash[:10]}... | Transactions: {block.transactions}")
        elif choice == '5':
            print("\nWallet Balances:")
            for user, balance in wallet.accounts.items():
                print(f"{user}: {balance} tokens")
        elif choice == '6':
            blockchain.visualize()
        elif choice == '7':
            print("Exiting the interface. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Lancer l'interface utilisateur
if __name__ == "__main__":
    mining_interface()
