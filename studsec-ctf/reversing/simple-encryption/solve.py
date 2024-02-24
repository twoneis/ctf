#!/usr/bin/env python3

from pwn import *

io = process('./simple_encryption')

password = b'I_want_a_terrace_from_the_vu'
magic = b'\x3e\x2b\x47\x29\x1a\x31\x0b\x0a\xb5\x70\xc2\xd0\x65\x11\xc0\xb0\x1b\x2d\x27\x00\x08\x57\x3a\x26\x09\x06\x2d\x08'
magic = b'\x3e\x2b\x47\x29\x1a\x31\x0b\x0a\x06\x51\x1c\x0b\x0b\x57\x0c\x2d\x1b\x2d\x27\x00\x08\x57\x3a\x26\x09\x06\x2d\x08'
password_buf = bytearray()

for i in range(0, 0x1c):
    password_buf.append(password[i] ^ magic[i])

print(io.recvline())
password = bytes(password_buf)
print(password)
io.sendline(password)
print(io.recvline())

