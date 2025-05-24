from PIL import Image
import random

def encrypt(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    width, height = image.size

    # Simple XOR encryption
    key = 42
    encrypted_pixels = [(r ^ key, g ^ key, b ^ key) for (r, g, b) in pixels]

    encrypted_img = Image.new("RGB", (width, height))
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("encrypted.jpg")
    print("Encrypted image saved as encrypted.jpg")

def decrypt(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    width, height = image.size

    # XOR decrypt (same as encryption)
    key = 42
    decrypted_pixels = [(r ^ key, g ^ key, b ^ key) for (r, g, b) in pixels]

    decrypted_img = Image.new("RGB", (width, height))
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save("decrypted.jpg")
    print("Decrypted image saved as decrypted.jpg")

# Run
encrypt("input.jpg")      # make sure input.jpg is in the same folder
decrypt("encrypted.jpg")
