#!/bin/python
import sys
import json

def main():
	if len(sys.argv) != 3:
		print 'provide PROXY FILE NAME and START PORT'
		exit()


	file = sys.argv[1]
	port = int(sys.argv[2])

	proxy_to_port = {}
	with open(file, 'r') as f:
		for each in f.readlines():
			proxy_to_port.update({each.strip(): str(port)})
			port += 1

	print proxy_to_port

	with open('_'.join([file.split('.')[0], 'to_port.txt']), 'w') as f:
		f.write(json.dumps(proxy_to_port))

if __name__ == '__main__':
	main()