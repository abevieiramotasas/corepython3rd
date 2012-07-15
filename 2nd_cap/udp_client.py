#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udp_cli_s = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udp_cli_s.sendto(data, ADDR)
    data, addr = udp_cli_s.recvfrom(BUFSIZ)
    if not data:
        break
    print data
udp_cli_s.close()

