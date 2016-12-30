import urllib2, os, json
from time import sleep
import argparse
import yaml 


def send_query(host, path, port, data, method='POST'):

  query_data = json.dumps(data)
  print ':'.join([host, port])
  print path
  url = os.path.join(':'.join([host, port]), path)
  r = urllib2.Request(url, query_data)
  resp = urllib2.urlopen(r)


  print 'generate %s request to %s with %s' %(method, url, data)
  print resp
  res = json.loads(resp.read().strip())
  print 'RESPOSNE: %s' %(res)
  print '*'*30
  return res


def run_test_according_to_config_file(file):
  config = yaml.load(file(file))
  host = config['host']
  path = config['path']
  port = config['port']
  data = config['data']
  url = config['url']
  paths = config['paths']

  for each in paths:
    print 'Run the query to the %s' %(each)
    d = send_query(host, each, port, data)
    data.update(d)



def main():
  parser = argparser.ArgumentParser()
  parser.add_argumeent('-c', '--config_file', help='configure file for the test information')

  args = parser.parse_args()
  run_test_according_to_config_file(args.config_file)


if __name__ == '__main__':
  main()

