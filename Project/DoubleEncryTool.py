import tkinter as tk
from tkinter import ttk, messagebox

# Morse code dictionary
morse_code_dict = {
  'A': '.-α',
    'B': '-...β',
    'C': '-.-.γ',
    'D': '-..δ',
    'E': '.ε',
    'F': '..-.ζ',
    'G': '--.η',
    'H': '....θ',
    'I': '..ι',
    'J': '.---κ',
    'K': '-.-λ',
    'L': '.-..μ',
    'M': '--ν',
    'N': '-.ξ',
    'O': '---ο',
    'P': '.--.π',
    'Q': '--.-ρ',
    'R': '.-.σ',
    'S': '...τ',
    'T': '-υ',
    'U': '..-φ',
    'V': '...-χ',
    'W': '.--ψ',
    'X': '-..-ω',
    'Y': '-.--ϕ',
    'Z': '--..Ω',
    '0': 'κ-----',
    '1': 'α.----',
    '2': 'β..---',
    '3': 'γ...--',
    '4': 'δ....-',
    '5': 'ε.....',
    '6': 'ζ-....',
    '7': 'η--...',
    '8': 'θ---..',
    '9': 'ι----.'

}

# Function to encode text to Morse code
def encode_to_morse(text):
    morse_code = ''
    for char in text:
        if char.upper() in morse_code_dict:
            morse_code += morse_code_dict[char.upper()] + '/'
        else:
            morse_code += char + '/'
    return morse_code.strip('/')

# Function to decode Morse code to text
def decode_from_morse(code):
    text = ''
    morse_code_reversed = {v: k for k, v in morse_code_dict.items()}  # Reverse the dictionary
    for code_segment in code.split('/'):
        if code_segment in morse_code_reversed:
            text += morse_code_reversed[code_segment]
        else:
            text += code_segment
    return text

# Function for encryption using Vigenère cipher
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

# Function for decryption using Vigenère cipher
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

# Function for double encryption
def double_encrypt(plaintext, vigenere_key):
    # Encrypt with Vigenère cipher
    vigenere_encrypted = vigenere_encrypt_math(plaintext, vigenere_key)
    # Encode the Vigenère encrypted text to Morse code
    morse_encoded = encode_to_morse(vigenere_encrypted)
    return morse_encoded

# Function for double decryption
def double_decrypt(ciphertext, vigenere_key):
    # Decode Morse code to text
    morse_decoded = decode_from_morse(ciphertext)
    # Decrypt the Morse decoded text with Vigenère cipher
    vigenere_decrypted = vigenere_decrypt_math(morse_decoded, vigenere_key)
    return vigenere_decrypted


# Function to handle button click
def encrypt_decrypt():
    plaintext = plaintext_entry.get()
    vigenere_key = shift_entry.get()

    # Double encryption
    double_encrypted_text = double_encrypt(plaintext, vigenere_key)
    encrypted_text.set(double_encrypted_text)

    # Double decryption
    double_decrypted_text = double_decrypt(double_encrypted_text, vigenere_key)
    decrypted_text.set(double_decrypted_text)


# Create the main window
window = tk.Tk()
window.title("Double Encryption Tool")

# Set bluish background color
window.configure(bg='#ddeeff')

# Add some padding around widgets
window.configure(padx=10, pady=10)

# Create and place widgets with ttk style
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), background='#ddeeff')  # Set background color of labels
style.configure('TEntry', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12), foreground='#ffffff', background='#000080')  # Set background color of buttons

ttk.Label(window, text="Enter the plaintext:", style='TLabel').grid(row=0, column=0, sticky="w")
plaintext_entry = ttk.Entry(window, style='TEntry')
plaintext_entry.grid(row=0, column=1, padx=5)

ttk.Label(window, text="Enter the Vigener cipher key:", style='TLabel').grid(row=1, column=0, sticky="w")
shift_entry = ttk.Entry(window, style='TEntry')
shift_entry.grid(row=1, column=1, padx=5)

encrypt_decrypt_button = ttk.Button(window, text="Encrypt/Decrypt", command=encrypt_decrypt, style='TButton')
encrypt_decrypt_button.grid(row=2, column=0, columnspan=2, pady=10)

ttk.Label(window, text="Double Encrypted:", style='TLabel').grid(row=3, column=0, sticky="w")
encrypted_text = tk.StringVar()
encrypted_label = ttk.Label(window, textvariable=encrypted_text, style='TLabel')
encrypted_label.grid(row=3, column=1, padx=5)

ttk.Label(window, text="Double Decrypted:", style='TLabel').grid(row=4, column=0, sticky="w")
decrypted_text = tk.StringVar()
decrypted_label = ttk.Label(window, textvariable=decrypted_text, style='TLabel')
decrypted_label.grid(row=4, column=1, padx=5)

# Start the GUI event loop
window.mainloop()