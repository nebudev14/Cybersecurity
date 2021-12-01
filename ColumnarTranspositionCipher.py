# Columnar Transposition Cipher in Python
import math

key = "HACK"

def encrypt(message, key):
    encrypted = ""

    key_index = 0
    message_len = float(len(message))
    message_list = list(message)
    key_list = sorted(list(key))

    cols = len(key)
    row = int(math.ceil(message_len/cols))