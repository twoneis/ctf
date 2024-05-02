#!/usr/bin/env python3

import sys
import socket
import threading
import random

HOST = '0.0.0.0'
PORT = 1337

with open('flag.txt', 'r') as f:
	flag = f.read().strip()

# I got p and g at https://tools.ietf.org/html/rfc3526#section-3 (2048 bit number)
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
g = 0x2

h1 = 0x3FF363EA5EC971A7B822275A2310F118BF4FED60148A78531A9155A95F321D772F7DFACD829786691B88565F63BD8DE509560A017CABF1BE6681E377359AFD106C8975674FBC90F5A4FDF66B3E318DBC308884F173FDB74634D6D55DC6EA9F7B87AB68F8B18FAABB62FB88E855AEB5520175BD377E53809EFF85C313E17D589E4C576A7AE6EF551D8DF6C18AF77F262C8A8564B5B68124ECD96D7252CA32FACB00FD6A830088C679427B709590D9B4C87389CBFB9DD8EFE47270A5089A847B9ED51C22283DA29CFA9342E202BBB84D88EF5226EAC5C13B60310BF33D7A5B5BCEE669A65BB6B4AC6E93F2558649824F55D67FB8A2557BACAAD7DAC5E166EDB5B4
h2 = 0xBA5CD124D4888B527D71943EC26A18E293BC3A902355142848136CF10E968A6E3672C381FC03C5E2C5D01794FA66E119BC706E9115D58A8B300B1CFD84B239FC87FBB91E15526A7E2CA64BE5083BE27F9F2966B73D76079069B19D76046FD502AB5E34F573A528D97A4891491A2569A14D4D2959457D5DED46901095394B6BED344E86CF0812954C3B65F3DF03E483324E9D5EE58C887A6D82C19F76BAB1F0EA2AAE1EA1492A7DB43FE34EB14FE778DEF2EE8C6B6595AB8CA3D1E9F28B360FBE52506A70C1B0BB21EE2D2220021F82DD1ECEF5430B648B38247E5840A62B54169B24D7912EC59BB7E791060AE31CE7BD03806FD4C21CC462FCBD112052E37F16

class Instance(threading.Thread):
	def __init__(self, conn):
		self.conn = conn
		super().__init__()

	def run(self):
		a = self.conn.recv(2048).decode('utf-8').strip().split(' ')
		a1 = int(a[0], 16)
		a2 = int(a[1], 16)

		c = random.randint(0, p-1)
		self.conn.sendall(hex(c).encode('utf-8'))

		cr = self.conn.recv(4096).decode('utf-8').strip().split(' ')
		c1 = int(cr[0], 16)
		c2 = int(cr[1], 16)
		r1 = int(cr[2], 16)
		r2 = int(cr[3], 16)

		gr1 = pow(g, r1, p)
		gr2 = pow(g, r2, p)
		ahc1 = (a1 * pow(h1, c1, p)) % p
		ahc2 = (a2 * pow(h2, c2, p)) % p

		if gr1 == ahc1 and gr2 == ahc2:
			self.conn.send("Success: {}".format(flag).encode('utf-8'))
		else:
			self.conn.send(b"Wrong.")

		self.conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((HOST, PORT))
	sock.listen(1)

	while True:
		conn, addr = sock.accept()
		Instance(conn).start()
