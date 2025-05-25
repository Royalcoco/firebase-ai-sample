import math
import hashlib
import requests
import math
import hashlib
import requests
import numpy as np
from PIL import Image

def equation_degre2(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return "Pas de solution réelle"


def equation_degre2_ping(a, b, c)::
    if a % 10 == 0:
        a = "ping"
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return "Pas de solution réelle"


def equation_degre2_pong(a, b, c):
    if a % 10 == 0:
        a = "pong"
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return "Pas de solution réelle"

def secure_equation_degre2(a, b, c):
    # Convert the coefficients to strings
    a_str = str(a)
    b_str = str(b)
    c_str = str(c)

    # Create a unique hash for the equation using the coefficients
    equation_hash = hashlib.sha256((a_str + b_str + c_str).encode()).hexdigest()

    # Check if the equation is already stored in the blockchain
    if check_blockchain(equation_hash):
        return "Equation already exists in the blockchain"

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return "No real solution"


def check_blockchain(equation_hash):
    # Check if the equation hash exists in the blockchain
    # Implement your blockchain checking logic here
    # Return True if the equation hash exists, False otherwise
    return False  # Placeholder implementation


def connect_to_blockchain(result):
    # Convert the result to a string
    result_str = str(result)
    
    # Create a request to connect to the blockchain with the result
    response = requests.post('https://example.com/blockchain', data=result_str)
    
    # Check the response status code
    if response.status_code == 200:
        return "Successfully connected to the blockchain"
    else:
        return "Failed to connect to the blockchain"

a = 10
b = 20
c = 30
solutions = secure_equation_degre2(a, b, c)
print(solutions)

result = 42
connection_status = connect_to_blockchain(result)
print(connection_status)

# Encode the blockchain data using trigonometry
def encode_blockchain_data(data):
    encoded_data = ""
    for char in data:
        encoded_data += encode_morse_code(char)
    return encoded_data

# Encode a single character using Morse code
def encode_morse_code(char):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
    }
    if char.upper() in morse_code:
        return morse_code[char.upper()]
    else:
        return ''

# Split the encoded blockchain data into three parts
def split_blockchain_data(encoded_data):
    part1 = encoded_data[::3]
    part2 = encoded_data[1::3]
    part3 = encoded_data[2::3]
    return part1, part2, part3

# Test the encoding and splitting functions
encoded_data = encode_blockchain_data(solutions)
part1, part2, part3 = split_blockchain_data(encoded_data)
print(part1)
print(part2)
print(part3)
# Encrypt the blockchain data using trigonometry
def encrypt_blockchain_data(data):
    encrypted_data = ""
    for char in data:
        encrypted_data += encrypt_trigonometry(char)
    return encrypted_data

# Encrypt a single character using trigonometry
def encrypt_trigonometry(char):
    trigonometry = {
        'A': 'sin', 'B': 'cos', 'C': 'tan', 'D': 'csc', 'E': 'sec', 'F': 'cot', 'G': 'asin', 'H': 'acos',
        'I': 'atan', 'J': 'acsc', 'K': 'asec', 'L': 'acot', 'M': 'sinh', 'N': 'cosh', 'O': 'tanh', 'P': 'csch',
        'Q': 'sech', 'R': 'coth', 'S': 'asinh', 'T': 'acosh', 'U': 'atanh', 'V': 'acsch', 'W': 'asech', 'X': 'acoth',
        'Y': 'exp', 'Z': 'log', '0': 'sqrt', '1': 'abs', '2': 'ceil', '3': 'floor', '4': 'round',
        '5': 'trunc', '6': 'factorial', '7': 'gamma', '8': 'lgamma', '9': 'erf', ' ': ''
    }
    if char.upper() in trigonometry:
        return trigonometry[char.upper()]
    else:
        return ''

# Split the encrypted blockchain data into three parts
def split_encrypted_data(encrypted_data):
    part1 = encrypted_data[::3]
    part2 = encrypted_data[1::3]
    part3 = encrypted_data[2::3]
    return part1, part2, part3

# Secure the equation solutions in the blockchain
encrypted_data = encrypt_blockchain_data(solutions)
part1, part2, part3 = split_encrypted_data(encrypted_data)

# Send the encrypted data and keys to the recipients
recipient1_key = part1
recipient2_key = part2
recipient3_key = part3

# Attach the keys to the email as attachments
attach_keys(recipient1_key, recipient2_key, recipient3_key)
import matplotlib.pyplot as plt

# Create a probability distribution plot of the equation
x = range(-10, 11)
y = [a*(x**2) + b*x + c for x in x]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Equation Probability Distribution')
plt.grid(True)
plt.savefig('equation_plot.png')

# Send the equation plot image to the recipients
recipient1_email = 'recipient1@example.com'
recipient2_email = 'recipient2@example.com'
recipient3_email = 'recipient3@example.com'

send_email(recipient1_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')
send_email(recipient2_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')
send_email(recipient3_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')

# Convert the equation plot image to an NFT
nft_image = convert_to_nft('equation_plot.png')

# Send the NFT image to the recipients
send_email(recipient1_email, 'NFT Image', 'Please find the NFT image attached.', nft_image)
send_email(recipient2_email, 'NFT Image', 'Please find the NFT image attached.', nft_image)
send_email(recipient3_email, 'NFT Image', 'Please find the NFT image attached.', nft_image)
# Convert the encoded data to a numpy array
encoded_data_array = np.array(list(encoded_data))

# Reshape the array to match the dimensions of the equation plot image
encoded_data_array = encoded_data_array.reshape((len(part1), len(part1[0])))

# Scale the values of the array to the range of RGB colors
scaled_array = (encoded_data_array / np.max(encoded_data_array)) * 255

# Create a color map using the scaled array
color_map = Image.fromarray(scaled_array.astype(np.uint8), mode='L')

# Open the equation plot image
equation_plot = Image.open('equation_plot.png')

# Resize the equation plot image to match the dimensions of the color map
equation_plot = equation_plot.resize(color_map.size)

# Convert the equation plot image to grayscale
equation_plot = equation_plot.convert('L')

# Apply the color map to the equation plot image
colored_equation_plot = equation_plot.convert('RGB')
colored_equation_plot.paste(color_map, (0, 0), mask=color_map)

# Save the final image with the NFT and Morse code colors
colored_equation_plot.save('colored_equation_plot.png')
# Display the final image with the NFT and Morse code colors
colored_equation_plot.show()
# Send the final image with the NFT and Morse code colors to the recipients
send_email(recipient1_email, 'Colored Equation Plot', 'Please find the colored equation plot attached.', 'colored_equation_plot.png')
send_email(recipient2_email, 'Colored Equation Plot', 'Please find the colored equation plot attached.', 'colored_equation_plot.png')
send_email(recipient3_email, 'Colored Equation Plot', 'Please find the colored equation plot attached.', 'colored_equation_plot.png')
# Create a probability distribution plot of the equation
x = range(-10, 11)
y = [a*(x**2) + b*x + c for x in x]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Equation Probability Distribution')
plt.grid(True)
plt.savefig('equation_plot.png')

# Send the equation plot image to the recipients
recipient1_email = ' recipients = ' + recipients + ' and recipients = ' + recipients + ' and recipients = ' + recipients + ' and recipients = ' + recipients + ' and recipients = ' + recipients + ' and recipients = ' + recipients + ' and recipients = ' + recipients + ' and recipients = ' + recipients + ' and recipients = ' + recipients + ' and recipients = ' + recipients
send_email(recipient1_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')
send_email(recipient2_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')
send_email(recipient3_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')

# Convert the equation plot image to an NFT
nft_image = convert_to_nft('equation_plot.png')

# Send the NFT image to the recipients
send_email(recipient1_email, 'NFT Image', 'Please find the NFT image attached.', nft_image)
send_email(recipient2_email, 'NFT Image', 'Please find the NFT image attached.', nft_image)
send_email(recipient3_email, 'NFT Image', 'Please find the NFT image attached.', nft_image)
# Convert the encoded data to a numpy array
encoded_data_array = np.array(list(encoded_data))

# Reshape the array to match the dimensions of the equation plot image
encoded_data_array = encoded_data_array.reshape((len(part1), len(part1[0])))
# Scale the values of the array to the range of RGB colors
scaled_array = (encoded_data_array / np.max(encoded_data_array)) * 255

# Create a color map using the scaled array
color_map = Image.fromarray(scaled_array.astype(np.uint8), mode='L')

# Open the equation plot image
equation_plot = Image.open('equation_plot.png')

# Resize the equation plot image to match the dimensions of the color map
equation_plot = equation_plot.resize(color_map.size)

# Convert the equation plot image to grayscale
equation_plot = equation_plot.convert('L')

# Apply the color map to the equation plot image
colored_equation_plot = equation_plot.convert('RGB')
colored_equation_plot.paste(color_map, (0, 0), mask=color_map)

# Save the final image with the NFT and Morse code colors
colored_equation_plot.save('colored_equation_plot.png')
# Display the final image with the NFT and Morse code colors
colored_equation_plot.show()
# Send the final image with the NFT and Morse code colors to the recipients
send_email(recipient1_email, 'Colored Equation Plot', 'Please find the colored equation plot attached.', 'colored_equation_plot.png')
send_email(recipient2_email, 'Colored Equation Plot', 'Please find the colored equation plot attached.', 'colored_equation_plot.png')
send_email(recipient3_email, 'Colored Equation Plot', 'Please find the colored equation plot attached.', 'colored_equation_plot.png')
# Create a probability distribution plot of the equation
x = range(-10, 11)
y = [a*(x**2) + b*x + c for x in x]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Equation Probability Distribution')
plt.grid(True)
plt.savefig('equation_plot.png')

# Send the equation plot image to the recipients
recipient1_email = '
send_email(recipient1_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')
send_email(recipient2_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')
send_email(recipient3_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')

# Convert the equation plot image to an NFT
nft_image = convert_to_nft('equation_plot.png')

# Send the NFT image to the recipients
send_email(recipient1_email, 'NFT Image', 'Please find the NFT image attached.', nft_image)
send_email(recipient2_email, 'NFT Image', 'Please find the NFT image attached.', nft_image)
send_email(recipient3_email, 'NFT Image', 'Please find the NFT image attached.', nft_image)
# Convert the encoded data to a numpy array
encoded_data_array = np.array(list(encoded_data))

# Reshape the array to match the dimensions of the equation plot image
encoded_data_array = encoded_data_array.reshape((len(part1), len(part1[0])))
# Scale the values of the array to the range of RGB colors
scaled_array = (encoded_data_array / np.max(encoded_data_array)) * 255

# Create a color map using the scaled array
color_map = Image.fromarray(scaled_array.astype(np.uint8), mode='L')

# Open the equation plot image
equation_plot = Image.open('equation_plot.png')

# Resize the equation plot image to match the dimensions of the color map
equation_plot = equation_plot.resize(color_map.size)

# Convert the equation plot image to grayscale
equation_plot = equation_plot.convert('L')

# Apply the color map to the equation plot image
colored_equation_plot = equation_plot.convert('RGB')
colored_equation_plot.paste(color_map, (0, 0), mask=color_map)

# Save the final image with the NFT and Morse code colors
colored_equation_plot.save('colored_equation_plot.png')
# Display the final image with the NFT and Morse code colors
colored_equation_plot.show()
# Send the final image with the NFT and Morse code colors to the recipients
send_email(recipient1_email, 'Colored Equation Plot', 'Please find the colored equation plot attached.', 'colored_equation_plot.png')
send_email(recipient2_email, 'Colored Equation Plot', 'Please find the colored equation plot attached.', 'colored_equation_plot.png')
send_email(recipient3_email, 'Colored Equation Plot', 'Please find the colored equation plot attached.', 'colored_equation_plot.png')
# Create a probability distribution plot of the equation
x = range(-10, 11)
y = [a*(x**2) + b*x + c for x in x]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Equation Probability Distribution')
plt.grid(True)
plt.savefig('equation_plot.png')

# Send the equation plot image to the recipients
recipient1_email = '
send_email(recipient1_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')
send_email(recipient2_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')
send_email(recipient3_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')

# Convert the equation plot image to an NFT
nft_image = convert_to_nft('equation_plot.png')

# Send the NFT image to the recipients
send_email(recipient1_email, 'NFT Image', 'Please find the NFT image attached.', nft_image)
send_email(recipient2_email, 'NFT Image', 'Please find the NFT image attached.', nft_image)
send_email(recipient3_email, 'NFT Image', 'Please find the NFT image attached.', nft_image)
# Convert the encoded data to a numpy array
encoded_data_array = np.array(list(encoded_data))

# Reshape the array to match the dimensions of the equation plot image
encoded_data_array = encoded_data_array.reshape((len(part1), len(part1[0])))
# Scale the values of the array to the range of RGB colors
scaled_array = (encoded_data_array / np.max(encoded_data_array)) * 255

# Create a color map using the scaled array
color_map = Image.fromarray(scaled_array.astype(np.uint8), mode='L')

# Open the equation plot image
equation_plot = Image.open('equation_plot.png')

# Resize the equation plot image to match the dimensions of the color map
equation_plot = equation_plot.resize(color_map.size)

# Convert the equation plot image to grayscale
equation_plot = equation_plot.convert('L')

# Apply the color map to the equation plot image
colored_equation_plot = equation_plot.convert('RGB')
colored_equation_plot.paste(color_map, (0, 0), mask=color_map)

# Save the final image with the NFT and Morse code colors
colored_equation_plot.save('colored_equation_plot.png')
# Display the final image with the NFT and Morse code colors
colored_equation_plot.show()
# Send the final image with the NFT and Morse code colors to the recipients
send_email(recipient1_email, 'Colored Equation Plot', 'Please find the colored equation plot attached.', 'colored_equation_plot.png')
send_email(recipient2_email, 'Colored Equation Plot', 'Please find the colored equation plot attached.', 'colored_equation_plot.png')
send_email(recipient3_email, 'Colored Equation Plot', 'Please find the colored equation plot attached.', 'colored_equation_plot.png')
# Create a probability distribution plot of the equation
x = range(-10, 11)
y = [a*(x**2) + b*x + c for x in x]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Equation Probability Distribution')
plt.grid(True)
plt.savefig('equation_plot.png')

# Send the equation plot image to the recipients
recipient1_email = '
send_email(recipient1_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')
send_email(recipient2_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')
send_email(recipient3_email, 'Equation Plot', 'Please find the equation plot attached.', 'equation_plot.png')

# Convert the equation plot image to an NFT
nft_image = convert_to_nft('equation_plot.png')
