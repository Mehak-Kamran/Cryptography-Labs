import numpy as np

def generate_vigenere_table():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table = []
    for i in range(26):
        row = alphabet[i:] + alphabet[:i]
        table.append(list(row))
    return np.array(table)

def vigenere_encrypt(plaintext, key):
    table = generate_vigenere_table()
    key_indices = [ord(char.upper()) - ord('A') for char in key]
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ""
    key_length = len(key_indices)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            row_index = ord(char) - ord('A')
            col_index = key_indices[i % key_length]
            ciphertext += table[row_index, col_index]
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    table = generate_vigenere_table()
    key_indices = [ord(char.upper()) - ord('A') for char in key]
    ciphertext = ciphertext.upper().replace(" ", "")
    plaintext = ""
    key_length = len(key_indices)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            col_index = key_indices[i % key_length]
            row_index = np.where(table[:, col_index] == char)[0][0]
            plaintext += chr(row_index + ord('A'))
    return plaintext

# Example usage:
print("Vegenere Cipher using Table")
plaintext = input("Enter plaintext: ")
key = input("Enter key: ")
encrypted_text = vigenere_encrypt(plaintext, key)
decrypted_text = vigenere_decrypt(encrypted_text, key)

print("\nVigenere Table:")
print(generate_vigenere_table())
print("\nPlaintext:", plaintext)
print("Key:", key)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)

