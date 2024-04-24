#!/usr/bin/env python3

from pwn import *

con = remote('challs.studsec.nl', 8120)

while True:
    rec_str = con.recvline().decode('utf-8')
    result = eval(rec_str)
    con.send(f'{result}')
    print(f'{rec_str} = {result}')
