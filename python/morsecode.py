# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', 
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', 
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
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

# Example usage
text_to_encode =input("Enter text to convert: ") 
#"I love to code.Python is my favorite programming language.I also have interest in webdevelopment.I have learned HTML CSS Javascript and Nodejs Now I am learning Reactjs.Soon I will be a web developer."

encoded_text = encode_to_morse(text_to_encode)
print("\nEncoded:", encoded_text)

decoded_text = decode_from_morse(encoded_text)
print("\nDecoded:", decoded_text)
