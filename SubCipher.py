import base64
import hashlib

# Substitution Cipher in Python
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'fcpevqkzgmtrayonujdlwhbxsi'

def encrypt(message):
    encrypted = ""
    for letter in message:
        if letter.lower() in alphabet:
            encrypted += key[alphabet.find(letter.lower())]
    return encrypted

def decrypt(message):
    decrypted = ""
    for letter in message:
        if letter.lower() in key:
            decrypted += alphabet[key.find(letter.lower())]
    return decrypted

print(encrypt("AAHHHHHHHHHHHHHHHHHHH"))
print(decrypt(encrypt("hello")))