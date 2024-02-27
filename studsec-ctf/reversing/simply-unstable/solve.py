#!/usr/bin/env python3

from pwn import *

sysconf_num = 127961
flag_ciphertex = 4963047724820499585
target_ciphertext = -443987883

input = target_ciphertext ^ flag_ciphertex

print("Calling with " + str(input))

io = process(['./challenge', str(input)])

print(io.recvall())
