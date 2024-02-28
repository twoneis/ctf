#!/usr/bin/env python3

from pwn import *

io = process('./basic_check')

io.sendline(b'CTF{W3lc0me_t0_The_WoRld_0ff_Rev3rse_Eng1neering}')
print(io.recvall())
