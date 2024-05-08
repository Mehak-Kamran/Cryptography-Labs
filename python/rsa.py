from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

def generate_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(public_key, plaintext):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def rsa_decrypt(private_key, ciphertext):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Example usage
print("RSA Algorithm")
private_key, public_key = generate_keypair()
plaintext = b"Hello, World!"  # Input plaintext to encrypt

# Encrypt the plaintext
ciphertext = rsa_encrypt(public_key, plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_text = rsa_decrypt(private_key, ciphertext)
print("Decrypted Text:", decrypted_text.decode())
