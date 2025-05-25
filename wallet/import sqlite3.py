import sqlite3
import os
import json
import csv
import math
import numpy as np
import sounddevice as sd
import zipfile
from cryptography.fernet import Fernet

# Génération de clé de chiffrement si elle n'existe pas
def generate_key():
    if not os.path.exists("wallet_key.key"):
        key = Fernet.generate_key()
        with open("wallet_key.key", "wb") as key_file:
            key_file.write(key)

def load_key():
    with open("wallet_key.key", "rb") as key_file:
        return Fernet(key_file.read())

generate_key()
cipher = load_key()

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
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS revenues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            revenue REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reinvestments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS investment_summary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            total_invested REAL,
            total_revenue REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Fonction pour insérer des données brutes et les augmenter à chaque téléchargement
def insert_raw_data(filename="raw_data.txt"):
    initial_value = 100.0  # Valeur initiale
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = float(file.read())
        new_value = data * 1.0004  # Augmentation de 0.04%
    else:
        new_value = initial_value
    
    with open(filename, "w") as file:
        file.write(str(new_value))
    
    print(f"📄 Données mises à jour: {new_value:.4f}")

# Fonction pour compresser et inclure une rupture de contrat
def zip_raw_data_with_contract_break(filename="raw_data.txt", zip_filename="contract_data.zip"):
    with open("contract_break.txt", "w") as file:
        file.write("Rupture du premier contrat en vigueur.")
    
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(filename)
        zipf.write("contract_break.txt")
    print(f"📦 Fichier compressé avec rupture de contrat: {zip_filename}")

# Fonction pour décompresser et exécuter le troisième contrat
def unzip_and_execute_contract(zip_filename="contract_data.zip", extract_to="."):
    with zipfile.ZipFile(zip_filename, "r") as zipf:
        zipf.extractall(extract_to)
    print(f"📂 Fichier extrait depuis {zip_filename}")
    
    third_contract_file = os.path.join(extract_to, "third_contract.txt")
    if os.path.exists(third_contract_file):
        with open(third_contract_file, "r") as file:
            print(f"🔍 Exécution du troisième contrat: {file.read()}")
    else:
        print("⚠️ Aucun troisième contrat trouvé.")

# Interface CLI améliorée
def main():
    while True:
        print("\n========= TERMINAL WALLET =========")
        print("1️⃣  Acheter Crypto")
        print("2️⃣  Revendre Crypto")
        print("3️⃣  Voir Transactions")
        print("4️⃣  Voir Résumé des Investissements")
        print("5️⃣  Mettre à jour les Données Brutes")
        print("6️⃣  Compresser avec Rupture de Contrat")
        print("7️⃣  Décompresser et Exécuter le Troisième Contrat")
        print("8️⃣  Quitter")
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
            show_investment_summary()
        elif choice == "5":
            insert_raw_data()
        elif choice == "6":
            zip_raw_data_with_contract_break()
        elif choice == "7":
            unzip_and_execute_contract()
        elif choice == "8":
            print("👋 Au revoir!")
            break
        else:
            print("❌ Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
