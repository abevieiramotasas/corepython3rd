#! /usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcp_cli_s = socket(AF_INET, SOCK_STREAM)
    tcp_cli_s.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcp_cli_s.send('%s\r\n' % data)
    data = tcp_cli_s.recv(BUFSIZ)
    if not data:
        break
    print data
    tcp_cli_s.close()   
