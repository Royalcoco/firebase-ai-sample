import socket
import threading

class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.blockchain = FractalBlockchain(difficulty=4)
        self.peers = []  # Liste des nœuds connectés

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"Node running on {self.host}:{self.port}")

        while True:
            conn, addr = server.accept()
            threading.Thread(target=self.handle_peer, args=(conn, addr)).start()

    def handle_peer(self, conn, addr):
        print(f"Connected to {addr}")
        data = conn.recv(1024).decode()
        print(f"Received: {data}")
        if data == "REQUEST_BLOCKCHAIN":
            conn.send(str(self.blockchain).encode())
        conn.close()

    def connect_to_peer(self, peer_host, peer_port):
        peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peer.connect((peer_host, peer_port))
        self.peers.append((peer_host, peer_port))
        peer.send("REQUEST_BLOCKCHAIN".encode())
        data = peer.recv(4096).decode()
        print(f"Blockchain received from {peer_host}:{peer_port}:\n{data}")
        peer.close()

# Create two nodes
node1 = Node("127.0.0.1", 5000)
node2 = Node("127.0.0.1", 5001)

# Start the nodes
threading.Thread(target=node1.start_server).start()
threading.Thread(target=node2.start_server).start()

# Connect the nodes
node2.connect_to_peer("127.0.0.1", 5000)
