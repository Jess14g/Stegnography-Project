import cv2

# Load the encrypted image
img = cv2.imread("")  # Replace with the correct image path

# Get the passcode for decryption
password = input("Enter passcode for Decryption: ")

# Store the original passcode (set this same passcode during encryption)
original_passcode = "your_passcode"  # Replace with the actual passcode used during encryption

# Create the dictionaries for encoding and decoding
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Initialize counters for iterating through the image
n = 0
m = 0
z = 0

# Check if the passcode is correct
if password == original_passcode:
    message = ""
    max_length = 1000  # Adjust max message length to prevent overflow

    # Loop through the pixels to extract the hidden message
    for i in range(max_length):  # Loop over the max possible characters
        # Extract the least significant bit (LSB) of each pixel (RGB channels)
        # Using the LSB to decode the message
        pixel_value = img[n, m, z]
        message += c[pixel_value]  # Map pixel value back to the character

        # Move to the next pixel
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through RGB channels

        # If we reach the end of the row, move to the next row
        if m >= img.shape[1]:
            m = 0
            n += 1

        # If the message is too long, you can break the loop here
        if len(message) > max_length:
            break

    print("Decrypted message:", message)  # Print the decrypted message
else:
    print("YOU ARE NOT AUTHORIZED")
