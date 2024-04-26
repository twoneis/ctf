#!/usr/bin/env python3
alphabet = "abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}"

pwd = alphabet[28] + alphabet[45] + alphabet[31] + \
      alphabet[63] + alphabet[48] + alphabet[55] + \
      alphabet[11] + alphabet[2] + alphabet[52] + \
      alphabet[12] + alphabet[3] + alphabet[62] + \
      alphabet[45] + alphabet[14] + alphabet[62] + \
      alphabet[43] + alphabet[55] + alphabet[21] + \
      alphabet[30] + alphabet[17] + alphabet[18] + \
      alphabet[8] + alphabet[13] + alphabet[6] + alphabet[64]

print(pwd)

while True:
    login = input("Enter your password>")
    if login == pwd:
        print("Login successful")
        exit()
    else:
        print("Login failed")
