import urllib2
import sys

def test_proxy_work(proxy, url=None):

	px = urllib2.ProxyHandler({'http': proxy})
	op = urllib2.build_opener(px)
	urllib2.install_opener(op)

	if not url:
		url = 'http://www.zhihu.com'

	try:
		a = urllib2.urlopen(url)
		content = a.read()
		print content
	except:
		return "NOT WORK"

	return "WORK"


def main():

	if len(sys.argv) != 2:
		print 'please provide the file contain proxy'
		exit()

	file = sys.argv[1]
	with open(file, 'r') as f:
		for each in f.readline():
			print  '%s: %s' %(each, test_proxy_work(each))



if __name__ == '__main__':
	main()

    
