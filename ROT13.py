# ROT13 in Python

abc = "abcdefghijklmnopqrstuvwxyz"
uppercase = abc.upper()

def encrypt(message):
    """Encrypts a message using ROT13.

    Iterates through each letter in message,
    and replaces it with the corresponding
    letter 13 places away from its index.

    Parameters
    ----------
    message : str
        The message you want to encrypt
    """

    encrypted = ""
    for letter in message:
        if letter.islower():
            encrypted += abc[(abc.find(letter)+13)%26]
        else:
            encrypted += uppercase[(uppercase.find(letter)+13)%26]
    return encrypted

def decrypt(message):
    """Decrypts a message using ROT13.

    Parameters
    ----------
    message : str
        The message you want to decrypt
    """

    decrypted = ""
    for letter in message:
        if (letter.lower() not in abc):
            decrypted += letter
        else:
            if letter.islower():
                decrypted += abc[(abc.find(letter)-13)%26]
            else:
                decrypted += uppercase[(uppercase.find(letter)-13)%26]
    return decrypted 
    
print(encrypt("hELLo"))
print(decrypt("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}"))
