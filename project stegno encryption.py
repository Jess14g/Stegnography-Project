import cv2
import os

# Load the image
img = cv2.imread("mypic.jpg")  # Replace with the correct image path

# Get the secret message and passcode from the user
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Dictionary for encoding and decoding
d = {}
c = {}

# Create the dictionaries for encoding and decoding
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Initialize counters for iterating through the image
m = 0
n = 0
z = 0

# Hide the secret message in the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]  # Store the message in the pixels
    n = n + 1
    m = m + 1
    z = (z + 1) % 3  # Cycle through the RGB channels

# Save the image with the hidden message
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open the image on Windows

print("Message has been hidden in the image.")
