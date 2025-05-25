from PIL import Image, ImageDraw, ImageFont
import shutil
import lculate_average_ping_time from lculate_average_ping_time
from encrypt_decrypt import encrypt_colorimetry, decrypt_colorimetry, encrypt_spectrum, decrypt_spectrum
import shutil
import socket
import statistics
import shutil
import random
import os


# Créer une nouvelle image
image = Image.new('RGB', (800, 800), color='white')
draw = ImageDraw.Draw(image)

# Ajouter du texte à l'image
font = ImageFont.truetype('arial.ttf', size=50)
text = "Mon NFT"
text_width, text_height = draw.textsize(text, font=font)
text_position = ((800 - text_width) // 2, (800 - text_height) // 2)
draw.text(text_position, text, font=font, fill='black')

# Enregistrer l'image en tant que fichier NFT
image.save('mon_nft.png')
# Encrypt the colorimetry
encrypted_colorimetry = encrypt_colorimetry(colorimetry)

# Add the encrypted colorimetry to the image metadata
image.info['colorimetry'] = encrypted_colorimetry
# Encrypt the color spectrums
encrypted_red_spectrum = encrypt_spectrum(red_spectrum)
encrypted_green_spectrum = encrypt_spectrum(green_spectrum)
encrypted_blue_spectrum = encrypt_spectrum(blue_spectrum)

# Add the encrypted color spectrums to the image metadata
image.info['red_spectrum'] = encrypted_red_spectrum
image.info['green_spectrum'] = encrypted_green_spectrum
image.info['blue_spectrum'] = encrypted_blue_spectrum

# Get the colorimetry from the image metadata
encrypted_colorimetry = image.info['colorimetry']
# Decrypt the colorimetry
colorimetry = decrypt_colorimetry(encrypted_colorimetry)
# Get the red, green, and blue spectrums from the image metadata
encrypted_red_spectrum = image.info['red_spectrum']
encrypted_green_spectrum = image.info['green_spectrum']
encrypted_blue_spectrum = image.info['blue_spectrum']
# Decrypt the red, green, and blue spectrums
red_spectrum = decrypt_spectrum(encrypted_red_spectrum)
green_spectrum = decrypt_spectrum(encrypted_green_spectrum)
blue_spectrum = decrypt_spectrum(encrypted_blue_spectrum)

# Assign colors to each shade in the NFT
color_palette = {}
for shade in colorimetry:
    red = red_spectrum[shade]
    green = green_spectrum[shade]
    blue = blue_spectrum[shade]
    color_palette[shade] = (red, green, blue)

# Use the color palette to assign colors to the image pixels
pixels = image.load()
for x in range(image.width):
    for y in range(image.height):
        pixel_color = color_palette[colorimetry[x, y]]
        pixels[x, y] = pixel_color
        # Generate a key for color mapping
        key = {}
        for shade, color in color_palette.items():
            key[color] = shade

        # Save the key as a JPEG file
        key_image = Image.new('RGB', (200, 200))
        key_draw = ImageDraw.Draw(key_image)
        key_font = ImageFont.truetype('arial.ttf', size=20)
        key_text_position = (10, 10)
        for color, shade in key.items():
            key_draw.rectangle([(10, key_text_position[1]), (30, key_text_position[1] + 20)], fill=color)
            key_draw.text((40, key_text_position[1]), shade, font=key_font, fill='black')
            key_text_position = (key_text_position[0], key_text_position[1] + 30)
        key_image.save('color_key.jpeg')
        
        # Save the image as an NFT file without encrypted data
        image.save('mon_nft.png')

        # Create a compressed folder for the encrypted NFT data
        shutil.make_archive('encrypted_nft_data', 'zip', '.', 'encrypted_data')
# Save the image as an NFT file
image.save('mon_nft.png')
# Compare the size of each folder
original_size = shutil.disk_usage('.').used
compressed_size = shutil.disk_usage('encrypted_nft_data.zip').used

# Calculate the reduction in size
reduction_percentage = (original_size - compressed_size) / original_size * 100

# Print the reduction percentage
print(f"The compressed folder is {reduction_percentage:.2f}% smaller than the original folder.")
# Generate a key for color mapping
key = {}
for shade, color in color_palette.items():
    key[color] = shade
    # Calculate the average ping time
    average_ping_time = calculate_average_ping_time()
        # Define the maximum acceptable ping time as a constant
        MAX_PING_TIME = 100  # milliseconds

        # Check if the average ping time exceeds the maximum acceptable ping time
        if average_ping_time > MAX_PING_TIME:
            print("The average ping time exceeds the maximum acceptable ping time.")
        else:
            print("The average ping time is within the acceptable range.")
            # Compress the ping data into a folder
            shutil.make_archive('ping_data', 'zip', '.', 'ping_data')
            # Compare the size of each folder
            original_size = shutil.disk_usage('.').used
            compressed_size = shutil.disk_usage('ping_data.zip').used
            
            # Calculate the reduction in size
            reduction_percentage = (original_size - compressed_size) / original_size * 100
            
            # Print the reduction percentage
            print(f"The compressed folder is {reduction_percentage:.2f}% smaller than the original folder.")
            # Compare the size of each folder
            original_size = shutil.disk_usage('.').used
            compressed_size = shutil.disk_usage('encrypted_nft_data.zip').used
            
            # Calculate the reduction in size
            reduction_percentage = (original_size - compressed_size) / original_size * 100
            
            # Print the reduction percentage
            print(f"The compressed folder is {reduction_percentage:.2f}% smaller than the original folder.")
            # Compare the size of each folder
            original_size = shutil.disk_usage('.').used
            compressed_size = shutil.disk_usage('ping_data.zip').used
            # Integrate the constant pi as the ping recipient without the file folder
            ping_recipient = 3.14159
            # Integrate the constant pi as the ping recipient with the file folder
            ping_recipient = 3.14159
            # Integrate the constant pi as the ping recipient with the file folder
            ping_recipient = 3.14159
            # Send the ping recipient without the compressed folder to the ping stream
            ping_stream.send(ping_recipient)

            # Receive the next ping from the search engine
            next_ping = search_engine.receive_ping()

            # Process the next ping
            process_ping(next_ping)
            # Calculate the latency of 99 pings
            latency = calculate_latency(99)
            # Check if the latency is within the acceptable range
            if latency < MAX_LATENCY:
                # Search for a connection using ping shifting
                connection = search_connection(latency)
                # Open a new tab with the home page
                open_homepage(connection)
            else:ble ping time
                print("The latency exceeds the maximum acceptable latency.")

            # Function to calculate the latency of multiple pings
            def calculate_latency(num_pings):
                # Define the target host
                host = "www.google.com"
                # Create a list to store the ping times
                ping_times = []
                # Send the pings and calculate the round-trip time
                for _ in range(num_pings):
                    try:
                        client_socket.settimeout(1)
                        # Send the ping request
                        client_socket.sendto(b'', (host, 0))
                        # Record the start time
                        start_time = time.time()
                        # Receive the response
                        _, _ = client_socket.recvfrom(1024)
                        # Record the end time
                        end_time = time.time()
                        # Calculate the round-trip time
                        round_trip_time = (end_time - start_time) * 1000
                        # Add the round-trip time to the list
                        ping_times.append(round_trip_time)
                        # Close the socket
                        client_socket.close()
                    except socket.timeout:
                        # Handle the timeout error
                        print("Ping request timed out.")
                # Calculate the average ping time
                average_ping_time = statistics.mean(ping_times)
                return average_ping_time

            # Function to search for a connection using ping shifting
            def search_connection(latency):
                # Perform ping shifting algorithm to find a connection
                # ...
                return connection

            # Function to open a new tab with the home page
                print(f"The compressed folder is {reduction_percentage:.2f}% smaller than the original folder.")
            def open_homepage(connection):
                # Open a new tab with the home page
                # ...
            # ...
            # Open the folder without compression
            shutil.unpack_archive('encrypted_nft_data.zip', 'uncompressed_nft_data')

            # Get the IP address of the recipient
            recipient_ip = "192.168.0.1"  # Replace with the actual recipient IP address

            # Send a notification to the central command about the data usage
            command = f"notify_command {recipient_ip} data_usage"
            os.system(command)
            # Generate a random key
            random_key = random.choice(list(key.keys()))

            # Create a copy of the key image
            key_copy = key_image.copy()

            # Save the key copy as a JPEG file
            key_copy.save('key_copy.jpeg')

            # Define the data center path
            data_center_path = '/path/to/data/center'

            # Move the key copy to the data center
            shutil.move('key_copy.jpeg', os.path.join(data_center_path, 'key_copy.jpeg'))
            
            