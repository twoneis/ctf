#!/usr/bin/env python3

import math
from pwn import *

# Given from challenge
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
g = 0x2
h = 0xFB5C538D11EB53C2EEFA8503693EBC1D7DD2C00ABB39C5762065117D53D1629B49998D1DEF1146ED1EDC0FF9628586CD8EAC56378D24081DB517FFE89B465462C6AEE93EEDE2E7D59A3AC6284E2D650EE1B74952D052C6CDF54163A795F8D17D2792A320054C61735F258D301E854F89C6A52C16BF2E783782F57B048BEFB4B97A1DC9CF3FBABEF8B745EBAF5FA450F9218D9B1BC72177B8BA17B13140C8F9523AC6C204116B042B4AB3C631A410270698A019E7F83ED8091C42CD3979C17C6BB3542DFE5B00D259AE848AC89570CD84B948761C767200D01F52E118C7185DCEB358E5F5B4B994F1607250C3FB018968564BD05435369842DD454B5FEFDED155

# con = remote('challs.studsec.nl', 7300)

c = 1
u = 1
r = 1

# given from protocol
a = pow(g, u)
# r is given but depends on x which we don't know
# r = x * c + u

# other stuff known
# h = g ** x
# c != 0

# if we could get g ** (c * x) to be a multiple of p we could have r = u, however we can only change c (g ** x is given by h), it would be possible to set it through that, but i don't know how to solve pow(h, c, p) == 0 for c

# if we find a multiple of p that is a power of 2, we can get gr == 0 (since g ** r == n * p then)

hc = pow(h, c, p)
a = p + 2
gr = pow(g, r, p)
hca = (hc * a) % p

ans = f'{hex(a)} {hex(c)} {hex(r)}'
print(ans)
print(f'gr = {hex(gr)}')
print(f'hca = {hex(hca)}')

if gr == hca and c != 0:
    print("\n\nSolved!!!\n\n")

# print(con.recvline())
# print(ans)
# con.sendline(ans.encode('utf-8'))

# print(con.recvall())
