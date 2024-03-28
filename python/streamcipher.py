def stream_cipher_encrypt_binary(plaintext_binary, key_binary):
    encrypted_binary = ""
    key_length = len(key_binary)
    
    for i, bit in enumerate(plaintext_binary):
        key_bit = key_binary[i % key_length]
        encrypted_bit = str(int(bit) ^ int(key_bit))
        encrypted_binary += encrypted_bit
    
    return encrypted_binary

def stream_cipher_decrypt_binary(ciphertext_binary, key_binary):
    return stream_cipher_encrypt_binary(ciphertext_binary, key_binary)  # Since XOR is its own inverse

# Example usage
plaintext_binary = "0110100001100101011011000110110001101111"  # Binary representation of "hello"
key_binary = "101010101010101010101010"  # Binary key
encrypted_binary = stream_cipher_encrypt_binary(plaintext_binary, key_binary)
print("Encrypted binary:", encrypted_binary)

decrypted_binary = stream_cipher_decrypt_binary(encrypted_binary, key_binary)
print("Decrypted binary:", decrypted_binary)
