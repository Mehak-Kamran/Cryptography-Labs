from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def pad(data):
    padding_length = 8 - (len(data) % 8)
    return data + bytes([padding_length] * padding_length)

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data)
    return plaintext

# Example usage
key = get_random_bytes(8)  # Generate a random 8-byte key
plaintext = b"Hello, World!"  # Input plaintext to encrypt

# Encrypt the plaintext
print("DES Algorithm")
ciphertext = des_encrypt(key, plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_text = des_decrypt(key, ciphertext)
print("Decrypted Text:", decrypted_text.decode())
