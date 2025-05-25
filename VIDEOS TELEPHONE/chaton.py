import sqlite3

# Créer une connexion à la base de données
conn = sqlite3.connect('ressources.db')

# Créer un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Créer une table pour les ressources
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ressources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        description TEXT,
        lien TEXT
    )
''')

# Exemple d'insertion de données dans la table
cursor.execute('''
    INSERT INTO ressources (nom, description, lien)
    VALUES ('Ressource 1', 'Description de la ressource 1', 'https://exemple.com/ressource1')
''')

# Valider les modifications et fermer la connexion
conn.commit()
conn.close() 
# Récupérer les images de chatons mignons depuis la base de données
cursor.execute("SELECT lien FROM ressources WHERE description LIKE '%chaton mignon%'")
result = cursor.fetchall()

# Parcourir les résultats et afficher les liens des images
for row in result:
    print(row[0])
    # Extraire les images de couleur rouge, vert et bleu depuis la base de données
    cursor.execute("SELECT lien FROM ressources WHERE description LIKE '%rouge%' OR description LIKE '%vert%' OR description LIKE '%bleu%'")
    result = cursor.fetchall()
    # Parcourir les résultats et afficher les liens des images
    for row in result:
        print(row[0])
        # Fais varier les lumières des images en fonction de la densité du noir dans les images
        for row in result:
            image_url = row[0]
            # Charger l'image à partir de l'URL
            image = load_image(image_url)
            # Calculer la densité du noir dans l'image
            black_density = calculate_black_density(image)
            # Faire varier les lumières de l'image en fonction de la densité du noir
            adjusted_image = adjust_lights(image, black_density)
            # Fusionner l'image ajustée avec l'interface de deuxième image
            merged_image = merge_images(adjusted_image, second_image, angle_of_projection)
            # Afficher l'image fusionnée
            show_image(merged_image)
            # Enregistrer l'image fusionnée dans un fichier
            save_image(merged_image, 'image_fusionnee.png')
            # Insérer l'image fusionnée dans la base de données
            cursor.execute("INSERT INTO ressources (nom, description, lien) VALUES ('Image fusionnée', 'Image fusionnée de deux images', 'image_fusionnee.png')")
            
            # Valider les modifications et fermer la connexion
            conn.commit()
            conn.close()

            # Charger l'image à partir de l'URL
            image = load_image(image_url)
            # Calculer la densité du noir dans l'image
            black_density = calculate_black_density(image)
            # Faire varier les lumières de l'image en fonction de la densité du noir
            adjusted_image = adjust_lights(image, black_density)
            # Fusionner l'image ajustée avec l'interface de deuxième image
            merged_image = merge_images(adjusted_image, second_image, angle_of_projection)
            # Afficher l'image fusionnée
            show_image(merged_image)
            # Enregistrer l'image fusionnée dans un fichier
            save_image(merged_image, 'image_fusionnee.png')
            # Insérer l'image fusionnée dans la base de données
            cursor.execute("INSERT INTO ressources (nom, description, lien) VALUES ('Image fusionnée', 'Image fusionnée de deux images', 'image_fusionnee.png')")

            # Valider les modifications et fermer la connexion
            conn.commit()