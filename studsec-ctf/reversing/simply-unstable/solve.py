#!/usr/bin/env python3

from pwn import *

sysconf_num = 0x1000
flag_ciphertex = 0x413C8C81
target_ciphertext = -0x1a76b7ab

input = target_ciphertext ^ flag_ciphertex

print("Calling with " + hex(input))

io = process(['./challenge', hex(input)])

print(io.recvall())
