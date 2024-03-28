# Function for encryption
def caesar_cipher_encrypt(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Function for decryption
def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

# Get input from the user
plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift value: "))

encrypted_text = caesar_cipher_encrypt(plaintext, shift)
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

print("Original:   ", plaintext)
print("Encrypted:  ", encrypted_text)
print("Decrypted:  ", decrypted_text)
