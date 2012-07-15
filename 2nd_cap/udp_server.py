#! /usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udp_ser_s = socket(AF_INET, SOCK_DGRAM)
udp_ser_s.bind(ADDR)



while True:
    print 'Waiting for message ...'
    data, addr = udp_ser_s.recvfrom(BUFSIZ)
    udp_ser_s.sendto('[%s] %s' % (ctime(), data), addr)
    print '... received from and returned to:', addr
    
udp_ser_s.close()
