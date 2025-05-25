from selenium import webdriver

# Chemin vers le fichier exécutable du navigateur
chromedriver_path = '/chemin/vers/chromedriver.exe'

# Initialiser le navigateur Chrome
driver = webdriver.Chrome(chromedriver_path)

# Liste des URLs à visiter
urls = ['https://www.example.com/page1', 'https://www.example.com/page2', 'https://www.example.com/page3']

# Parcourir chaque URL
for url in urls:
    # Charger l'URL dans le navigateur
    driver.get(url)
    
    # Effectuer des actions sur la page (par exemple, extraire des données)
    # ...
    
    # Attendre quelques secondes avant de passer à la page suivante
    driver.implicitly_wait(5)

# Fermer le navigateur
driver.quit()
# Effectuer des actions supplémentaires sur la page (par exemple, cliquer sur un bouton)
# ...


# Attendre quelques secondes avant de passer à la page suivante
driver.implicitly_wait(5)
