import os
import random
from PIL import Image, ImageDraw, ImageFont
import qrcode
from web3 import Web3
import ipfshttpclient

class CarrotImageGenerator:
    def __init__(self, width=600, height=600):
        self.width = width
        self.height = height

    def generate_carrot_image(self, output_path):
        image = Image.new("RGBA", (self.width, self.height), (255, 255, 255, 255))
        draw = ImageDraw.Draw(image)
        rand = random.Random()

        # Set random background color
        background_color = (rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255), 255)
        draw.rectangle([0, 0, self.width, self.height], fill=background_color)

        # Draw random carrot
        for _ in range(5):  # Drawing 5 carrots for variety
            self.draw_random_carrot(draw, rand)
            
        image.save(output_path)
        
    def draw_random_carrot(self, draw, rand):
        
        # Set random carrot color
        carrot_color = (rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255), 255)
        carrot_outline_color = (0, 0, 0, 255)
        
        # Set random carrot size
        carrot_width = rand.randint(50, 100)
        carrot_height = rand.randint(100, 200)
        
        # Set random carrot position
        carrot_x = rand.randint(0, self.width - carrot_width)
        carrot_y = rand.randint(0, self.height - carrot_height)
        
        # Draw carrot
        draw.rectangle([carrot_x, carrot_y, carrot_x + carrot_width, carrot_y + carrot_height], fill=carrot_color, outline=carrot_outline_color)
        
        # Draw carrot leaves
        leaf_width = rand.randint(50, 100)
        leaf_height = rand.randint(50, 100)
        leaf_x = carrot_x + carrot_width//2 - leaf_width//2
        leaf_y = carrot_y - leaf_height
        draw.polygon([(leaf_x, leaf_y), (leaf_x + leaf_width, leaf_y), (leaf_x + leaf_width//2, leaf_y - leaf_height)], fill=(0, 255, 0, 255), outline=(0, 0, 0, 255))
        # Generate random block data
        block_data = os.urandom(32)

        # Convert block data to hexadecimal string
        block_data_hex = block_data.hex()

        # Draw block data on the image
        font = ImageFont.truetype("arial.ttf", 20)
        draw.text((10, 10), block_data_hex, fill=(0, 0, 0), font=font)
        
        # Generate QR code for block data.
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(block_data_hex)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save("qr.png")
        
        # Load QR code image
        qr_image = Image.open("qr.png")
        
        # Calculate the position to place the QR code in the center of the image
        qr_width, qr_height = qr_image.size
        qr_x = (self.width - qr_width) // 2
        qr_y = (self.height - qr_height) // 2
        
        # Paste the QR code onto the main image
        image.paste(qr_image, (qr_x, qr_y))
        
        # Save the image
        image.save("carrot.png")
        
        # Print the message
        print("Carrot image saved to carrot.png")
        
        # Remove the QR code image
        os.remove("qr.png")
        
# Instantiate the CarrotImageGenerator class
carrot_generator = CarrotImageGenerator()

# Generate a carrot image
carrot_generator.generate_carrot_image("carrot.png")
# Instantiate the DecentralizedLibrary class
library = DecentralizedLibrary()

# Add the generate_random_image function to the library
library.add_code("generate_random_image", generate_random_image)

# Generate a random image using the CarrotImageGenerator class
carrot_generator.generate_carrot_image("random_image.png")
# Add the random image to the library
library.add_code("random_image", "random_image.png")

# Execute the code for the random image
library.execute_code("random_image", "random_image.png")

# Generate a QR code for the block data
generate_qr_code(block_data_hex, "qr_code.png")

# Add the generate_qr_code function to the library
library.add_code("generate_qr_code", generate_qr_code)

# Execute the code for the QR code
library.execute_code("generate_qr_code", "qr_code.png")
# Instantiate the Web3 class
w3 = Web3(Web3.HTTPProvider("http://..."))'(Web3.HTTPProvider("http://..."))

# Add the Web3 class to the library
library.add_code("web3", w3)

# Execute the code for the Web3 class
library.execute_code("web3", "http://...")
# Instantiate the IPFS client
ipfs_client = ipfshttpclient.connect("/ip4/../tcp/...")
# Add the IPFS client to the library
library.add_code("ipfs_client", ipfs_client)

# Execute the code for the IPFS client
library.execute_code("ipfs_client", "/ip4/../tcp/...")
```

# Path: remodk.py
# Compare this snippet from nft'X.py:
#     draw.text((text_x, text_y), text, fill=text_color, font=font)
#
#     image.save(output_path)
#     print("Random NFT saved to", output_path)
#
# def generate_qr_code(data, output_path):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,

# Path: remodk.py
# Compare this snippet from nft'X.py:
#     draw.text((text_x, text_y), text, fill=text_color, font=font)
#
#     image.save(output_path)
#     print("Random NFT saved to", output_path)
#
# def generate_qr_code(data, output_path):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(data)
#     qr.make(fit=True)
#
#     img = qr.make_image(fill='black', back_color='white')
#     img.save(output_path)
#     print("QR code saved to", output_path)
#
# def upload_to_ipfs(output_path):
#     with ipfshttpclient.connect() as client:
#         res = client.add(output_path)
#         print("Upload to IPFS:", res['Hash'])
#         return res['Hash']
import os
import random
from PIL import Image, ImageDraw, ImageFont
import qrcode
from web3 import Web3
import ipfshttpclient

class CarrotImageGenerator:
    def __init__(self, width=600, height=600):
        self.width = width
        self.height = height

    def generate_carrot_image(self, output_path):
        image = Image.new("RGBA", (self.width, self.height), (255, 255, 255, 255))
        draw = ImageDraw.Draw(image)
        rand = random.Random()

        # Set random background color
        background_color = (rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255), 255)
        draw.rectangle([0, 0, self.width, self.height], fill=background_color)

        # Draw random carrot
        for _ in range(5):  # Drawing 5 carrots for variety
            self.draw_random_carrot(draw, rand)
            
        image.save(output_path)
        
    def draw_random_carrot(self, draw, rand):
        
        # Set random carrot color
        carrot_color = (rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255), 255)
        carrot_outline_color = (0, 0, 0, 255)
        
        # Set random carrot size
        carrot_width = rand.randint(50, 100)
        carrot_height = rand.randint(100, 200)
        
        # Set random carrot position
        carrot_x = rand.randint(0, self.width - carrot_width)
        carrot_y = rand.randint(0, self.height - carrot_height)
        
        # Draw carrot
        draw.rectangle([carrot_x, carrot_y, carrot_x + carrot_width, carrot_y + carrot_height], fill=carrot_color, outline=carrot_outline_color)
        
        # Draw carrot leaves
        leaf_width = rand.randint(50, 100)
        leaf_height = rand.randint(50, 100)
        leaf_x = carrot_x + carrot_width//2 - leaf_width//2
        leaf_y = carrot_y - leaf_height
        draw.polygon([(leaf_x, leaf_y), (leaf_x + leaf_width, leaf_y), (leaf_x + leaf_width//2, leaf_y - leaf_height)], fill=(0, 255, 0, 255), outline=(0, 0, 0, 255))
        # Generate random block data
        block_data = os.urandom(32)

        #
        block_data_hex = block_data.hex()
        
        font = ImageFont.truetype("arial.ttf", 20)
        draw.text((10, 10), block_data_hex, fill=(0, 0, 0), font=font)
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(block_data_hex)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save("qr.png")
        
        qr_image = Image.open("qr.png")
        
        qr_width, qr_height = qr_image.size
        qr_x = (self.width - qr_width) // 2
        qr_y = (self.height - qr_height) // 2
        
        image.paste(qr_image, (qr_x, qr_y))
        
        image.save("carrot.png")
        
        print("Carrot image saved to carrot.png")
        
        os.remove("qr.png")
        
# Instantiate the CarrotImageGenerator class
carrot_generator = CarrotImageGenerator()
