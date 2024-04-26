#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


def encrypt(msg, key):
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(msg.encode('utf-8'), AES.block_size))
    encrypted = base64.b64encode(ciphertext).decode('utf-8')
    return encrypted


# TODO
def decrypt(encrypted, key):
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    text = base64.b64decode(encrypted)
    return cipher.decrypt(text)


key = "SuperSecretKey!!"
message = "CTF{fakeflag}"

encrypted_message = encrypt(message, key)
encrypted_message = "+l9MVyKCcO+EcNKStP/AwdTdr02tBia4coDxlAjaNWs="
print("Encrypted:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted:", decrypted_message)
