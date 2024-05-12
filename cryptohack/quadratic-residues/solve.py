#!/usr/bin/env python3

import math

p = 29
ints = [14, 6, 11] 

for a in ints:
    for i in range(0, p):
        if pow(i, 2, p) == a:
            print(i)
