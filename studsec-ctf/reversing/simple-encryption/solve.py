#!/usr/bin/env python3

from pwn import *

io = process('./simple_encryption')

password = b'CTF{G3t_Th4t_m4n_A_terraCe!}'

print(io.recvline())
print(password)
io.sendline(password)
print(io.recvline())

