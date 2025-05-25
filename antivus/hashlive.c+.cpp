import hashlib
import sys
import datetime

#include <openssl/evp.h>
#include <openssl/rand.h>
#include <iostream>
#include <string>

// Fonction pour chiffrer les données
std::string encryptData(const std::string& data, const std::string& key) {
    // Initialisation du contexte de chiffrement
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, (const unsigned char*)key.c_str(), NULL);

    // Chiffrement des données
    int cipherTextLen = data.length() + EVP_MAX_BLOCK_LENGTH;
    unsigned char* cipherText = new unsigned char[cipherTextLen];
    int len;
    EVP_EncryptUpdate(ctx, cipherText, &len, (const unsigned char*)data.c_str(), data.length());
    cipherTextLen = len;

    // Finalisation du chiffrement
    EVP_EncryptFinal_ex(ctx, cipherText + len, &len);
    cipherTextLen += len;

    // Conversion du texte chiffré en une chaîne de caractères
    std::string encryptedData((char*)cipherText, cipherTextLen);

    // Nettoyage des ressources
    delete[] cipherText;
    EVP_CIPHER_CTX_free(ctx);

    return encryptedData;
}

// Fonction pour déchiffrer les données
std::string decryptData(const std::string& encryptedData, const std::string& key) {
    // Initialisation du contexte de déchiffrement
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, (const unsigned char*)key.c_str(), NULL);

    // Déchiffrement des données
    int plainTextLen = encryptedData.length() + EVP_MAX_BLOCK_LENGTH;
    unsigned char* plainText = new unsigned char[plainTextLen];
    int len;
    EVP_DecryptUpdate(ctx, plainText, &len, (const unsigned char*)encryptedData.c_str(), encryptedData.length());
    plainTextLen = len;

    // Finalisation du déchiffrement
    EVP_DecryptFinal_ex(ctx, plainText + len, &len);
    plainTextLen += len;

    // Conversion du texte déchiffré en une chaîne de caractères
    std::string decryptedData((char*)plainText, plainTextLen);

    // Nettoyage des ressources
    delete[] plainText;
    EVP_CIPHER_CTX_free(ctx);

    return decryptedData;
}

int main() {
    // Clé de chiffrement
    std::string key = "MaCleDeChiffrement";

    // Données à chiffrer
    std::string data = "Bonjour, ceci est un message secret.";

    // Chiffrement des données
    std::string encryptedData = encryptData(data, key);
    std::cout << "Données chiffrées : " << encryptedData << std::endl;

    // Déchiffrement des données
    std::string decryptedData = decryptData(encryptedData, key);
    std::cout << "Données déchiffrées : " << decryptedData << std::endl;

    return 0;
}
// 3eme niveau
std::string puzzle = "This is the puzzle message.";
std::string minedData = "";
int cursor = 0;

while (cursor < puzzle.length()) {
    std::string packet = puzzle.substr(cursor, 8); // Retrieve 8 bytes as a packet
    std::string encryptedPacket = encryptData(packet, key); // Encrypt the packet
    minedData += encryptedPacket; // Append the encrypted packet to mined data
    cursor += 8; // Move the cursor to the next packet
}

std::cout << "Mined data: " << minedData << std::endl;
// 4eme niveau
std::string decryptedMinedData = "";
cursor = 0;

while (cursor < minedData.length()) {
    std::string encryptedPacket = minedData.substr(cursor, 16); // Retrieve 16 bytes as an encrypted packet
    std::string packet = decryptData(encryptedPacket, key); // Decrypt the encrypted packet
    decryptedMinedData += packet; // Append the decrypted packet to the mined data
    cursor += 16; // Move the cursor to the next encrypted packet
}

std::cout << "Decrypted mined data: " << decryptedMinedData << std::endl;
// 5eme niveau
std::string decryptedPuzzle = "";
cursor = 0;

while (cursor < decryptedMinedData.length()) {
    std::string packet = decryptedMinedData.substr(cursor, 8); // Retrieve 8 bytes as a packet
    decryptedPuzzle += packet; // Append the packet to the decrypted puzzle
    cursor += 8; // Move the cursor to the next packet
}

std::cout << "Decrypted puzzle: " << decryptedPuzzle << std::endl;
// 6eme niveau
std::string finalData = decryptData(decryptedPuzzle, key);
std::cout << "Final data: " << finalData << std::endl;
// 7eme niveau
std::string decryptedFinalData = decryptData(finalData, key);
std::cout << "Decrypted final data: " << decryptedFinalData << std::endl;
// 8eme niveau
std::string decryptedDecryptedFinalData = decryptData(decryptedFinalData, key);
std::cout << "Decrypted decrypted final data: " << decryptedDecryptedFinalData << std::endl;
// 9eme niveau
std::string decryptedDecryptedDecryptedFinalData = decryptData(decryptedDecryptedFinalData, key);
std::cout << "Decrypted decrypted decrypted final data: " << decryptedDecryptedDecryptedFinalData << std::endl;
pip install pyobjc pyjnius
# Importation des bibliothèques nécessaires

# Fonction pour générer un hashh
def generate_hash(data):
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()


# Interface pour MacOSr MacOS
def mac_interface():
    data = input("Enter data to hash: ")
    hash_value = generate_hash(data)
    print(f"Generated Hash: {hash_value}")

# Interface pour Windows
def windows_interface():
    data = input("Enter data to hash: ")
    hash_value = generate_hash(data)
    print(f"Generated Hash: {hash_value}")


# Sélection de l'interface en fonction du système d'exploitation
if sys.platform == "darwin":
    mac_interface()
elif sys.platform == "win32":
    windows_interface()
else:
    print("Unsupported platform.")

# Minage de données et calcul de la valeur crypto
def mine_data(data):
    num_dates_in_year = 365
    crypto_value = 700_000_000
    value_per_date = crypto_value / num_dates_in_year
    print(f"Value per date: {value_per_date}")

mine_data(data)
ed platform.")
// 10eme niveau
std::string hashedData = generate_hash(data);
std::cout << "Generated Hash: " << hashedData << std::endl;

// Template wizard
std::string userInput;
std::cout << "Enter command: ";
std::getline(std::cin, userInput);
std::string output = executeCommand(userInput);
std::cout << "Output: " << output << std::endl;

