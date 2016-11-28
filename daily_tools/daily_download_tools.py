import os
import argparse

from local_config import PORT, PATH


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--filename', help='File to download' )
	parser.add_argument('-d', '--directory', help='directory to download')

	args = parser.parse_args()

	directory = args.directory
	filename = args.filename

	if directory:
		path = PATH + directory
		command = 'scp -r -P %s %s ./' %(PORT, path)
	else:
		path = PATH + filename
		command = 'scp -P %s %s ./' %(PORT, path)
	os.system(command)


if __name__ == '__main__':
	main()