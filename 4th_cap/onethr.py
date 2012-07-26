#! /usr/bin/env python

from time import sleep, ctime

def loop(time, name):
	print 'start loop %s at:' % name, ctime()
	sleep(time)
	print 'loop %s done at:' % name, ctime()

def main():
	print 'starting at:', ctime()
	loop(4, '4s')
	loop(2, '2s')
	print 'all DONE at:', ctime()

if __name__ == '__main__':
	main()
