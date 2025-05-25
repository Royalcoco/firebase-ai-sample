import os
import random
import requests
import bluetooth
from cryptography.fernet import Fernet
from datetime import datetime
from openpyxl import Workbook
import tkinter as tk

# Déclaration des constantes
EXCEL_FILENAME = "agenda_capsule_temps.xlsx"
USB_PATH = "/path/to/usb"
URL_DOMINANT = "https://cmd.central.net/upload"
TOTTH_URL = "https://totth.org/receive"
DATA_SIZE_MB = 50  # Taille des données à libérer en Mo

# Initialisation du fichier Excel
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

# Fonction pour envoyer les données chiffrées
def send_encrypted_data(url, encrypted_data, key):
    response = requests.post(
        url,
        files={
            'data': encrypted_data,
            'key': key
        }
    )
    return response

# Fonction pour gérer les communications Bluetooth
def bluetooth_handler():
    # Simuler la recherche de dispositifs Bluetooth
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)
    print("Dispositifs Bluetooth détectés :", nearby_devices)
    
    # Simuler l'envoi d'une autorisation et la réception d'une réponse
    for addr, name in nearby_devices:
        print(f"Envoi d'autorisation à {name} ({addr})")
        # Simuler l'envoi et la réception
        response = "authorized"  # Simuler une réponse
        if response == "authorized":
            print(f"Autorisation reçue de {name} ({addr})")
            return addr, name
    return None, None

# Fonction pour libérer un enregistrement de 50 Mo sur USB
def release_usb_record(size_mb):
    data = os.urandom(size_mb * 1024 * 1024)  # Générer des données aléatoires
    file_path = os.path.join(USB_PATH, "data_record.dat")
    with open(file_path, "wb") as file:
        file.write(data)
    print(f"Enregistrement de {size_mb} Mo libéré sur USB.")

# Fonction derive_secteur
def derive_secteur():
    addr, name = bluetooth_handler()
    if addr and name:
        # Simulation de la réception des données Bluetooth
        sector_drift = random.uniform(0.8, 1.2) * 100  # Valeur de dérive simulée
        print(f"Dérive du secteur: {sector_drift}")
        # Libérer un enregistrement de 50 Mo sur USB
        release_usb_record(DATA_SIZE_MB)
        return sector_drift
    else:
        print("Aucun appareil Bluetooth autorisé trouvé.")
        return None

# Fonction pour enregistrer les notifications et envoyer les données
def register_and_send_notifications(cipher_suite):
    # Générer les montants de minage réussis
    mining_amounts = [random.uniform(0.1, 5.0) for _ in range(10)]
    data_str = ','.join(map(str, mining_amounts))
    encrypted_data = cipher_suite.encrypt(data_str.encode())
    
    # Enregistrer les résultats dans le fichier Excel
    workbook = openpyxl.load_workbook(EXCEL_FILENAME)
    sheet = workbook.active
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append([timestamp, encrypted_data])
    workbook.save(EXCEL_FILENAME)
    
    # Envoyer les données chiffrées à l'URL dominante
    send_encrypted_data(URL_DOMINANT, encrypted_data, cipher_suite._encryption_key)

# Fonction pour afficher les résultats et traiter les valeurs sur un terminal d'animation
def display_results():
    root = tk.Tk()
    root.title("Terminal d'animation")

    canvas = tk.Canvas(root, width=200, height=200, bg="white")
    canvas.pack()

    def animate():
        canvas.create_rectangle(50, 50, 150, 150, fill="blue")
        canvas.update()
    
    animate_button = tk.Button(root, text="Animer", command=animate)
    animate_button.pack()

    root.mainloop()

# Initialisation
initialize_excel()
cipher_suite = store_keys_on_usb()
sector_drift = derive_secteur()
if sector_drift is not None:
    register_and_send_notifications(cipher_suite)
display_results()
