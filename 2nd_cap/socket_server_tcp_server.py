#! /usr/bin/env python


from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    # metodo utilizado para tratar a chegada de mensagem
    # StreamRequestHandler trata a entrada e saida de dados como objetos file
    def handle(self):
        print '... connected from:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))
        
tcp_serv = TCP(ADDR, MyRequestHandler)

print 'Waiting for connection ...'

tcp_serv.serve_forever()
