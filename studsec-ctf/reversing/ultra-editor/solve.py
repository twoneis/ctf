#!/usr/bin/env python3

from pwn import *

# Notes
# ---
#  0x0e < uname_len < 0x20
# 0x0d < email_len < 0x21
# email_len + uname_len <= reg_len >> 1 && reg_len >> 1 < 0xc9

# uname_len = 0xf
# email_len = 0xe
# reg_len = 0x3a

HOST = 'challs.studsec.nl'
PORT = 3200
# con = remote(HOST, PORT)
con = process('./activation_service')

print(con.recvuntil('Username').decode('utf-8'))
con.sendline('a' * 32)

con.recvall()
