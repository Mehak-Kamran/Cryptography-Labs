from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(data):
    padding_length = AES.block_size - (len(data) % AES.block_size)
    return data + bytes([padding_length] * padding_length)

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.iv + cipher.encrypt(padded_plaintext)
    return ciphertext

def aes_decrypt(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext[AES.block_size:])
    plaintext = unpad(decrypted_data)
    return plaintext

# Example usage
print("AES Algorithm")
key = get_random_bytes(16)  # Generate a random 16-byte (128-bit) key
plaintext = b"Hello, World!"  # Input plaintext to encrypt

# Encrypt the plaintext
ciphertext = aes_encrypt(key, plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_text = aes_decrypt(key, ciphertext)
print("Decrypted Text:", decrypted_text.decode())
