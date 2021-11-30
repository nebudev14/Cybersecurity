# Substitution Cipher in Python

def encrypt(message):
    encrypted = ""
    for letter in message:
        if ord(letter)-95 <= 13:
            encrypted += chr(ord(letter)+13)

        elif ord(letter)-95 >= 13:
            encrypted += chr(ord(letter)-13)
    return encrypted

print(encrypt("hello")) # returns URYYB