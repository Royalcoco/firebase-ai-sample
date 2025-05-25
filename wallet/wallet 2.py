import sqlite3
import os
import json
import csv
import math
import hashlib
import numpy as np
import sounddevice as sd
import zipfile
import http.server
import socketserver
import threading
from cryptography.fernet import Fernet

# Génération de clé de chiffrement sur un hardware sécurisé
def generate_hardware_key():
    key_path = "key_secure-passe.throw"  # Stockage décentralisé simulé
    if not os.path.exists(key_path):
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)

def load_hardware_key():
    key_path = "key_secure-passe.throw"
    with open(key_path, "rb") as key_file:
        return Fernet(key_file.read())

generate_hardware_key()
cipher = load_hardware_key()

# Création de la base de données sécurisée
def init_db():
    conn = sqlite3.connect("wallet.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            amount REAL,
            price REAL,
            sender TEXT,
            receiver TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS blocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            hash TEXT,
            previous_hash TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Fonction pour envoyer des crypto
def send_crypto(sender, receiver, amount):
    conn = sqlite3.connect("wallet.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (type, amount, sender, receiver) VALUES (?, ?, ?, ?)", ("send", amount, sender, receiver))
    conn.commit()
    conn.close()
    print(f"📤 {amount} crypto envoyés de {sender} à {receiver}.")

# Fonction pour recevoir des crypto
def receive_crypto(sender, receiver, amount):
    conn = sqlite3.connect("wallet.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (type, amount, sender, receiver) VALUES (?, ?, ?, ?)", ("receive", amount, sender, receiver))
    conn.commit()
    conn.close()
    print(f"📥 {amount} crypto reçus de {sender} par {receiver}.")

# Interface CLI améliorée
def main():
    while True:
        print("\n========= TERMINAL WALLET =========")
        print("1️⃣  Acheter Crypto")
        print("2️⃣  Revendre Crypto")
        print("3️⃣  Voir Transactions")
        print("4️⃣  Envoyer Crypto")
        print("5️⃣  Recevoir Crypto")
        print("6️⃣  Miner un Block")
        print("7️⃣  Compresser avec Block")
        print("8️⃣  Décompresser et Vérifier")
        print("9️⃣  Quitter")
        print("===================================")
        choice = input("👉 Choisissez une option: ")
        if choice == "1":
            try:
                amount = float(input("Quantité de crypto: "))
                price = float(input("Prix unitaire (€): "))
                buy_crypto(amount, price)
            except ValueError:
                print("❌ Entrée invalide. Veuillez saisir un nombre valide.")
        elif choice == "2":
            sell_crypto()
        elif choice == "3":
            show_transactions()
        elif choice == "4":
            sender = input("Expéditeur: ")
            receiver = input("Destinataire: ")
            amount = float(input("Montant: "))
            send_crypto(sender, receiver, amount)
        elif choice == "5":
            sender = input("Expéditeur: ")
            receiver = input("Destinataire: ")
            amount = float(input("Montant: "))
            receive_crypto(sender, receiver, amount)
        elif choice == "6":
            data = input("Données du block: ")
            mine_block({"data": data})
        elif choice == "7":
            zip_contract_with_block()
        elif choice == "8":
            unzip_and_verify_block()
        elif choice == "9":
            print("👋 Au revoir!")
            break
        else:
            print("❌ Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
