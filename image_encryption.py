from PIL import Image

# Function to encrypt the image using XOR
def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure image is in RGB mode

    # Get pixel data
    pixels = list(img.getdata())
    width, height = img.size

    # Apply XOR encryption to each pixel
    encrypted_pixels = [(r ^ key, g ^ key, b ^ key) for r, g, b in pixels]

    # Create new encrypted image
    encrypted_img = Image.new("RGB", (width, height))
    encrypted_img.putdata(encrypted_pixels)
    
    # Save encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Encryption completed. Image saved as encrypted_image.png")

# Function to decrypt the image using XOR
def decrypt_image(image_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    img = img.convert("RGB")

    # Get pixel data
    pixels = list(img.getdata())
    width, height = img.size

    # Apply XOR decryption to each pixel (same as encryption because XOR is reversible)
    decrypted_pixels = [(r ^ key, g ^ key, b ^ key) for r, g, b in pixels]

    # Create new decrypted image
    decrypted_img = Image.new("RGB", (width, height))
    decrypted_img.putdata(decrypted_pixels)
    
    # Save decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Decryption completed. Image saved as decrypted_image.png")

# Usage
key = 123  # Example encryption key (must be the same for both encryption and decryption)

# Encrypt an image
encrypt_image("input_image.png", key)

# Decrypt the image
decrypt_image("encrypted_image.png", key)
