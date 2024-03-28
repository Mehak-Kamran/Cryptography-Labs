import string

def vernam_encrypt(plaintext, key):
    encrypted_text = ""
    for i in range(len(plaintext)):
        # Calculate the shift value based on the key
        shift = ord(key[i]) - ord('a')
        
        # Shift the character of plaintext by the calculated shift value
        encrypted_char = chr((ord(plaintext[i]) - ord('a') + shift) % 26 + ord('a'))
        
        encrypted_text += encrypted_char
    
    return encrypted_text

def vernam_decrypt(ciphertext, key):
    decrypted_text = ""
    for i in range(len(ciphertext)):
        # Calculate the shift value based on the key
        shift = ord(key[i]) - ord('a')
        
        # Shift the character of ciphertext by the negative of the calculated shift value
        decrypted_char = chr((ord(ciphertext[i]) - ord('a') - shift) % 26 + ord('a'))
        
        decrypted_text += decrypted_char
    
    return decrypted_text

# User input
print("\n\tVernam Cipher")
plaintext = input("Enter the plaintext: ").lower()  # Convert to lowercase for consistency
key = input("Enter the key (must be the same length as plaintext): ").lower()  # Convert to lowercase for consistency

# Check if the input strings are empty
if not plaintext or not key:
    print("Both plaintext and key must not be empty.")
else:
    # Check if the lengths of plaintext and key are the same
    if len(plaintext) != len(key):
        print("Plaintext and key must have the same length.")
    else:
        # Encryption
        encrypted_text = vernam_encrypt(plaintext, key)
        print("Encrypted text:", encrypted_text)

        # Decryption
        decrypted_text = vernam_decrypt(encrypted_text, key)
        print("Decrypted text:", decrypted_text)
