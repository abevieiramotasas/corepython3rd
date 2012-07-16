#! /usr/bin/env python 

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print 'Erro: conexao com %s falhou' % HOST
        return
    try:
        f.login()
    except ftplib.error_perm:
        print 'Erro: nao pode conectar anonimamente'
        f.quit()
        return
    
    print 'Logado como anonimo'
    
    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'Erro: nao conseguiu mudar o diretorio para %s' % DIRN
        f.quit()
        return
    
    print 'Diretorio mudado para %s' % DIRN
    
    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
    except ftplib.error_perm:
        print 'Erro: nao conseguiu abrir o arquivo %s' % FILE
        os.unlink(FILE)
    print 'Download concluido'
    f.quit()
    return
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
