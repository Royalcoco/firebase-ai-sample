import os
import random
import bluetooth
from cryptography.fernet import Fernet
from datetime import datetime
from openpyxl import Workbook
import tkinter as tk

# Déclaration des constantes
USB_PATH = "/path/to/usb"
CALL_SIZE_MB = 50

# Initialisation du fichier Excel
EXCEL_FILENAME = "agenda_capsule_temps.xlsx"

def initialize_excel():
    if not os.path.exists(EXCEL_FILENAME):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Agenda"
        sheet.append(["Timestamp", "Dérive du secteur", "Temps total (99.8%)", "Rendu console (0.2%)"])
        workbook.save(EXCEL_FILENAME)

# Fonction pour générer et stocker les clés sur USB
def store_keys_on_usb():
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    key_path = os.path.join(USB_PATH, "encryption_key.key")
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    return cipher_suite

# Fonction pour gérer les communications Bluetooth
def bluetooth_handler():
    target_name = "My Bluetooth Device"  # Changez ceci avec le nom de votre appareil Bluetooth
    target_address = None

    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)
    for addr, name in nearby_devices:
        if target_name == name:
            target_address = addr
            break

    if target_address is not None:
        print(f"Appareil trouvé : {target_name} - {target_address}")
        # Effectuer une connexion et un appel
        port = 1  # Port d'écoute standard pour RFCOMM
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((target_address, port))
        print(f"Connecté à {target_name} sur le port {port}")
        # Envoyer une demande de tirage
        sock.send("Demande de tirage")
        response = sock.recv(1024)
        print(f"Réponse reçue : {response}")
        sock.close()
    else:
        print(f"Appareil {target_name} non trouvé")

# Fonction pour libérer un enregistrement de 50 Mo via USB
def release_usb_record():
    record_data = os.urandom(CALL_SIZE_MB * 1024 * 1024)  # Générer 50 Mo de données aléatoires
    record_path = os.path.join(USB_PATH, "record.bin")
    with open(record_path, "wb") as record_file:
        record_file.write(record_data)
    print(f"Enregistrement de 50 Mo libéré sur {record_path}")

# Fonction pour gérer la dérive du secteur
def derive_secteur():
    # Exemple de calcul pour la dérive du secteur
    sector_drift = random.uniform(0.8, 1.2)  # Facteur aléatoire pour simuler la dérive
    time_total = sector_drift * 0.998
    console_output = sector_drift * 0.002

    print(f"Dérive du secteur: {sector_drift}")
    print(f"Temps total (99.8%): {time_total}")
    print(f"Rendu console (0.2%): {console_output}")

    # Enregistrer les résultats dans le fichier Excel
    workbook = openpyxl.load_workbook(EXCEL_FILENAME)
    sheet = workbook.active
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append([timestamp, sector_drift, time_total, console_output])
    workbook.save(EXCEL_FILENAME)

    # Libérer l'enregistrement de 50 Mo via USB
    release_usb_record()

# Initialisation
initialize_excel()
cipher_suite = store_keys_on_usb()
bluetooth_handler()
derive_secteur()
