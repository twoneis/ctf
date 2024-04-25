#!/usr/bin/env python3

import sys
import socket
import threading
import random

HOST = '0.0.0.0'
PORT = 1337

with open('flag.txt', 'r') as f:
	flag = f.read().strip()

# p and g are from https://tools.ietf.org/html/rfc3526#section-3 (2048 bit number)
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
g = 0x2

h = 0xFB5C538D11EB53C2EEFA8503693EBC1D7DD2C00ABB39C5762065117D53D1629B49998D1DEF1146ED1EDC0FF9628586CD8EAC56378D24081DB517FFE89B465462C6AEE93EEDE2E7D59A3AC6284E2D650EE1B74952D052C6CDF54163A795F8D17D2792A320054C61735F258D301E854F89C6A52C16BF2E783782F57B048BEFB4B97A1DC9CF3FBABEF8B745EBAF5FA450F9218D9B1BC72177B8BA17B13140C8F9523AC6C204116B042B4AB3C631A410270698A019E7F83ED8091C42CD3979C17C6BB3542DFE5B00D259AE848AC89570CD84B948761C767200D01F52E118C7185DCEB358E5F5B4B994F1607250C3FB018968564BD05435369842DD454B5FEFDED155

class Instance(threading.Thread):
	def __init__(self, conn):
		self.conn = conn
		super().__init__()

	def run(self):
		self.conn.send(b"Can you show you can authenticate yourself?\n")

		try:
			packet = self.conn.recv(4096).decode('utf-8').strip().split(' ')
			a = int(packet[0], 16)
			c = int(packet[1], 16)
			r = int(packet[2], 16)
		except:
			self.conn.send(b"Wrong format.\n")
			self.conn.close()
			return

		if c == 0:
			self.conn.send(b"We know it messes with the probability distribution, but we do not accept a proof with an all-zero challenge.")
			self.conn.close()
			return

		gr = pow(g, r, p)
		hca = (pow(h, c, p) * a) % p

		if gr == hca:
			self.conn.send("We see that you can authenticate yourself.\nHere is the flag: {}\n".format(flag).encode('utf-8'))
		else:
			self.conn.send(b"This is not a valid authentication. No flag for you.\n")

		self.conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((HOST, PORT))
	sock.listen(1)

	while True:
		conn, addr = sock.accept()
		Instance(conn).start()
