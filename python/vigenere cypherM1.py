def vigenere_encrypt_math(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper()
    key_length = len(key)
    encrypted_text = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
    return encrypted_text

def vigenere_decrypt_math(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")
    key = key.upper()
    key_length = len(key)
    decrypted_text = ""
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            decrypted_text += decrypted_char
    return decrypted_text

# Example usage:
print("\nVigenere Cipher Using Mathematical Calculations")
plaintext = input("\nEnter plaintext: ")
key = input("Enter key: ")

encrypted_text = vigenere_encrypt_math(plaintext, key)
decrypted_text = vigenere_decrypt_math(encrypted_text, key)

print("\nPlaintext:", plaintext)
print("Key:", key)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
