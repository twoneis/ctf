#!/usr/bin/env python3

from pwn import *

password = b'CTF{W3lc0me_t0_The_WoRld_0ff_Rev3rse_Eng1neering}'

io = process('./basic_check')

print("\n")

io.sendline(password + b'0x00')

print(io.recvline())

# io.interactive();

print("\n")
