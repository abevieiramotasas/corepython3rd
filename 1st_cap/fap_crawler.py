import urllib2
import os


BASE = 'http://uploads.lolhehehe.com/wp-content/uploads/2012/07/fap-%s.jpg'
FAP = 'fap-%s.jpg'

os.mkdir('fap')
for i in range(5):
    try:
        p = urllib2.urlopen(BASE % str(i))
        fp = open(os.path.join('fap',FAP % str(i)), 'w')
        fp.write(p.read())
        fp.close()
        p.close()
    except urllib2.HTTPError:
        continue
