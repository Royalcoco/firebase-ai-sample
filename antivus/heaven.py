import os
import random
import string
import qrcode

# Créer le dossier
os.makedirs("dossier_securise")

# Niveaux de sécurité
niveaux_securite = [1, 3, 5, 6, 7]

# Niveaux avec mots de passe
mots_de_passe = {
    1: ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
    3: ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
    5: ''.join(random.choices(string.ascii_letters + string.digits, k=10))
}

# Niveaux avec captcha
captchas = {
    6: "mot1",
    7: "mot2"
}

# Créer les niveaux de sécurité
for niveau in range(1, 16):
    if niveau in niveaux_securite:
        if niveau in mots_de_passe:
            # Appliquer mot de passe
            with open(f"dossier_securise/niveau_{niveau}.txt", "w") as file:
                file.write(f"Mot de passe : {mots_de_passe[niveau]}")
        elif niveau in captchas:
            # Appliquer captcha
            with open(f"dossier_securise/niveau_{niveau}.txt", "w") as file:
                file.write(f"Captcha : {captchas[niveau]}")
        else:
            # Niveaux de sécurité générés par GitHub Copilot
            with open(f"dossier_securise/niveau_{niveau}.txt", "w") as file:
                file.write("Niveau de sécurité généré par GitHub Copilot")
    else:
        # Niveaux non sécurisés
        with open(f"dossier_securise/niveau_{niveau}.txt", "w") as file:
            file.write("Niveau non sécurisé")
            # Niveaux avec mineurs
            mineurs = {
                8: "A",
                9: "B",
                10: "C",
                11: "D",
                12: "E",
                13: "F",
                14: "G",
                15: "H"
            }

            # Créer les niveaux avec mineurs
            for niveau in range(8, 16):
                if niveau in mineurs:
                    with open(f"dossier_securise/niveau_{niveau}.txt", "w") as file:
                        file.write(f"Mineur : {mineurs[niveau]}")
                else:
                    # Niveaux de sécurité générés par GitHub Copilot
                    with open(f"dossier_securise/niveau_{niveau}.txt", "w") as file:
                        file.write(f"Mineur : {mineurs[niveau]}")
                        # Sauvegarder les données du mineur dans un fichier fragmenté en 4
                        data = f"Mineur : {mineurs[niveau]}"
                        fragment_size = len(data) // 4
                        fragments = [data[i:i+fragment_size] for i in range(0, len(data), fragment_size)]
                        for i, fragment in enumerate(fragments):
                            with open(f"dossier_securise/fragment_{niveau}_{i+1}.txt", "w") as fragment_file:
                                fragment_file.write(fragment)
                                
print("Dossier sécurisé créé avec succès !")

# Créer le fichier de vérification
with open("dossier_securise/verification.txt", "w") as file:
    file.write("Vérification : OK")

print("Fichier de vérification créé avec succès !")

# Créer le fichier de vérification
with open("dossier_securise/verification.txt", "w") as file:
    file.write("Vérification : OK")
    
print("Fichier de vérification créé avec succès !")

# Créer le fichier de vérification
with open("dossier_securise/verification.txt", "w") as file:
    file.write("Vérification : OK")
    
    # Ajuster le ping autour de 1500
    ping = 1500

    # Envoyer le résultat dans un input de wallet préalablement choisi dans la bibliothèque de modèle de wallet
    wallet_input = input("Entrez votre wallet : ")

    # Comparer et choisir les 2 wallets à fusionner
    wallets = ["wallet1", "wallet2", "wallet3", "wallet4"]
    selected_wallets = random.sample(wallets, 2)

    # Fusionner les wallets sous HTML
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Fusion de wallets</title>
    </head>
    <body>
        <h1>Wallet fusionné</h1>
        <ul>
            <li>{selected_wallets[0]}</li>
            <li>{selected_wallets[1]}</li>
        </ul>
    </body>
    </html>
    """

    # Écrire le code HTML dans un fichier
    with open("dossier_securise/fusion_wallets.html", "w") as file:
        file.write(html_code)

    print("Fusion de wallets effectuée avec succès !")
    
    # Envoyer le résultat dans un input de wallet préalablement choisi dans la bibliothèque de modèle de wallet
    
    wallet_input = input("Entrez votre wallet : ")
    
    # Comparer et choisir les 2 wallets à fusionner
    wallets = ["wallet1", "wallet2", "wallet3", "wallet4"]
    selected_wallets = random.sample(wallets, 2)
    
    # Fusionner les wallets sous HTML
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Fusion de wallets</title>
    </head>
    <body>
        <h1>Wallet fusionné</h1>
        <ul>
            <li>{selected_wallets[0]}</li>
            <li>{selected_wallets[1]}</li>
        </ul>
    </body>
    </html>
    """
    # Générer un QR code pour la première transaction

    # Montant de la première transaction
    transaction1_amount = 10

    # Générer le QR code pour la première transaction
    transaction1_qr = qrcode.make(f"Montant : {transaction1_amount}")

    # Sauvegarder le QR code dans un fichier
    transaction1_qr.save("dossier_securise/transaction1_qr.png")

    # Générer un QR code pour la deuxième transaction
    # Montant de la deuxième transaction
    transaction2_amount = 15

    # Générer le QR code pour la deuxième transaction
    transaction2_qr = qrcode.make(f"Montant : {transaction2_amount}")

    # Sauvegarder le QR code dans un fichier
    transaction2_qr.save("dossier_securise/transaction2_qr.png")

    print("Sauvegarde des transactions effectuée avec succès !")
    
    # Générer un QR code pour la première transaction
    
    # Montant de la première transaction
    transaction1_amount = 10
    
    # Générer le QR code pour la première transaction
    transaction1_qr = qrcode.make(f"Montant : {transaction1_amount}")
    