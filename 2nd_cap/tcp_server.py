#! /usr/bin/env python

# sockets
from socket import *
from time import ctime


HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcp_ser_s = socket(AF_INET, SOCK_STREAM)

tcp_ser_s.bind(ADDR)
# maximo numero de conexoes aceitas(fila de espera)
tcp_ser_s.listen(5)
setdefaulttimeout(2)

while True:
    print 'waiting for connection ...'
    tcp_cli_s, addr = tcp_ser_s.accept()
    print '... connected from:', addr
    
    # tcp_cli_s.send("Testando")
    while True:
        try:
            data = tcp_cli_s.recv(BUFSIZ)
            if not data:
                break
            tcp_cli_s.send('[%s] %s' % (ctime(), data))
            print ">>>>", data
        except timeout:
            # deu timeout, morreu conexao
            break
    tcp_cli_s.close()
tcp_ser_s.close()
