#!/usr/bin/env python3

from pwn import *

argv1 = 0x0a002320
io = process(['./mazegen', hex(argv1)], env={'DEBUG': ''})

print(io.recvall())
