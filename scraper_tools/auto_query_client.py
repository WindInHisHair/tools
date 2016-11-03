import urllib2, os, json
from time import sleep

def send_query(host, path, port, data, method='POST'):

  query_data = json.dumps(data)
  print ':'.join([host, port])
  print path
  url = os.path.join(':'.join([host, port]), path)
  r = urllib2.Request(url, query_data)
  resp = urllib2.urlopen(r)


  print 'generate %s request to %s' %(method, url)
  print resp
  res = json.loads(resp.read().strip())
  print 'RESPOSNE: %s' %(res)
  print '*'*30
  return res

