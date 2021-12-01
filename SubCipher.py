# Substitution Cipher in Python
key = 'fcpevqkzgmtrayonujdlwhbxsi'

def encrypt(message, key):
    """Encrypts a message using Substitution Cipher.
    
    Itereates through each letter in message, and 
    replaces it with the letter with the corresponding
    index in key.

    Parameters
    ----------
    message : str
        The message you want to encrypt
    key : str
        The key you want to use to encrypt your 
        message with
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ""
    for letter in message:
        if letter.lower() in alphabet:
            encrypted += key[alphabet.find(letter.lower())]
    return encrypted

def decrypt(message, key):
    """Decrypts a mesasge using Substitution Cipher

    Parameters
    ----------
    message : str
        The message you want to decrypt
    key : str
        The key you want to use to decrypt your message with
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = ""
    for letter in message:
        if letter.lower() in key:
            decrypted += alphabet[key.find(letter.lower())]
    return decrypted

print(encrypt("AAHHHHHHHHHHHHHHHHHHH", key))
print(decrypt(encrypt("hello", key), key))