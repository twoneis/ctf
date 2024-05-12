#!/usr/bin/env python3

from pwn import *
import json

con = remote('socket.cryptohack.org', 11112)

print(con.recvline())
print(con.recvline())
con.sendline(json.dumps({'buy': 'flag'}).encode())
print(con.recvall())
