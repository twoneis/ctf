#!/usr/bin/env python3

def ispow2(n):
    if n == 0x1:
        return True
    if (n & 0x1) == 0x0:
        return(ispow2(n >> 1))
    return False

for i in range(1, 1024):
    if ispow2(i):
        print(i)
