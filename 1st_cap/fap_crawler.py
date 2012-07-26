#! /usr/bin/env python
import urllib2
import os
import sys
import time

if (len(sys.argv) != 2 or not sys.argv[1].isdigit()):
    print("Entre com o maior valor de fap-images")
    sys.exit()


BASE = 'http://uploads.lolhehehe.com/wp-content/uploads/2012/07/fap-%d.jpg'
FAP = 'fap-%d.jpg'
if (not os.path.exists('fap')):
    os.mkdir('fap')



for i in range(int(sys.argv[1])):
    fap_name = FAP % i
    if (os.path.exists(os.path.join('fap', fap_name))):
        continue
    try:
        ini = time.time()
        print("---------------------------")
        print("Download do fap %f" % i)
        p = urllib2.urlopen(BASE % i)
        fp = open(os.path.join('fap',fap_name), 'w')
        fp.write(p.read())
        fp.close()
        p.close()
        print("Fap downloadado, tempo total = %f" % (time.time() - ini))
    except urllib2.HTTPError:
        print("Este fap nao existe :(")
    finally:
        print("---------------------------")
