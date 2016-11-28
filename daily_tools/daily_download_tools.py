import os
import argparse

from local_config import PORT, PATH


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--filename', help='File to download' )
	parser.add_argument('-d', '--directory', help='directory to download')
	parser.add_argument('-s', '--server', help='server', default=None)
	parser.add_argument('-u', '--user', help='user', default=None)
	parser.add_argument('-m', '--method', help='specify the download or upload', default='download')
	args = parser.parse_args()

	directory = args.directory
	filename = args.filename
	method = args.method

	if args.server and args.user:
		PATH= '%s@%s:/home/%s/' %(user, server, user)


	if directory:
		
		if method == 'download':
			path = PATH + directory
			command = 'scp -r -P %s %s ./' %(PORT, path)
		else:
			command = 'scp -r -P %s ./%s  %s' %(PORT, args.directory, PATH)
	else:
		if method == 'download':
			path = PATH + filename
			command = 'scp -P %s %s ./' %(PORT, path)
		else:
			command = 'scp -P %s ./%s  %s' %(PORT, args.filename, PATH)
	os.system(command)


if __name__ == '__main__':
	main()