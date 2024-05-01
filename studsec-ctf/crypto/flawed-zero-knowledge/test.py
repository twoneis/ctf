#!/usr/bin/env python3

for i in range(16, 2000):
    p = pow(2, i)
    p = p >> max(8, p.bit_length()) - 8
    print(hex(p))
