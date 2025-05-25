def generate_nft(width, height):
    # Créer une nouvelle image avec la taille spécifiée
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Générer un texte aléatoire pour le NFT
    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    # Dessiner le texte sur l'image
    text_position = (width // 2, height // 2)
    text_color = (0, 0, 0)
    text_font = ImageFont.truetype("arial.ttf", 24)
    draw.text(text_position, text, fill=text_color, font=text_font, anchor="middle")

    # Enregistrer l'image en tant que fichier NFT
    image.save("nft.png")
    # Mémoriser le NFT dans un template
    template = {
        "width": width,
        "height": height,
        "text": text,
        "text_position": text_position,
        "text_color": text_color,
        "text_font": text_font,
        "image_path": "nft.png"
    }
    return template
    # Enregistrer le NFT dans le dossier "documents"
    image.save("documents/nft.png")
    # Mémoriser le NFT dans un template
    template = {
        "width": width,
        "height": height,
        "text": text,
        "text_position": text_position,
        "text_color": text_color,
        "text_font": text_font,
        "image_path": "nft.png",
        "mining_code": None,
        "transaction_input": None,
        "transaction_output": None
    }
    # Calculer la somme possible en cryptomonnaie
    crypto_amount = width * height * 0.001
    
    # Enregistrer la somme dans l'input 1
    template["transaction_input"] = crypto_amount

    # Créer un input de gestion de crypto monnaie
    crypto_input = {
        "amount": crypto_amount,
        "address": "your_wallet_address"
    }

    # Enregistrer l'input de gestion de crypto monnaie dans le template
    template["transaction_input"] = crypto_input

    return template
    # Calculer le poids moyen du NFT
    average_weight = (width + height) / 2

    # Enregistrer le poids moyen dans l'input de gestion de crypto monnaie
    template["transaction_input"]["weight"] = average_weight

    return template
    # Calculer le hash du NFT
    hash = hashlib.sha256()
    hash.update(str(template).encode())
    hash_code = hash.hexdigest()
    
    # Enregistrer le hash dans le template
    template["mining_code"] = hash_code
    
    return template
    # Créer un output de gestion de crypto monnaie
    crypto_output = {
        "amount": crypto_amount,
        "address": "your_wallet_address"
    }
    
    # Enregistrer l'output de gestion de crypto monnaie dans le template
    template["transaction_output"] = crypto_output
    
    return template
    # Enregistrer le NFT dans le dossier "documents"
    image.save("documents/nft.png")
    # Mémoriser le NFT dans un template
    template = {
        "width": width,
        "height": height,
        "text": text,
        "text_position": text_position,
        "text_color": text_color,
        "text_font": text_font,
        "image_path": "nft.png",
        "mining_code": None,
        "transaction_input": None,
        "transaction_output": None
    }
    # Calculer la somme possible en cryptomonnaie
    crypto_amount = width * height * 0.001
    
    # Enregistrer la somme dans l'input 1
    template["transaction_input"] = crypto_amount
    
    # Créer un input de gestion de crypto monnaie
    crypto_input = {
        "amount": crypto_amount,
        "address": "your_wallet_address"
    }
    
    # Enregistrer l'input de gestion de crypto monnaie dans le template
    template["transaction_input"] = crypto_input
    
    # Calculer le poids moyen du NFT
    average_weight = (width + height) / 2

    # Enregistrer le poids moyen dans l'input de gestion de crypto monnaie
    template["transaction_input"]["weight"] = average_weight
    
    # Calculer le hash du NFT
    hash = hashlib.sha256()
    hash.update(str(template).encode())
    hash_code = hash.hexdigest()

    # Enregistrer le hash dans le template
    template["mining_code"] = hash_code
    
    # Créer un output de gestion de crypto monnaie
    crypto_output = {
        "amount": crypto_amount,
        "address": "your_wallet_address"
    }
    