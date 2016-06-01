#Assignment_15.2_freddy_sanchez

import urllib
import json 


url = 'http://python-data.dr-chuck.net/comments_242238.json'
print 'Retrieving', url
handle = urllib.urlopen(url)
data = handle.read()
print 'Retrieved',len(data),'characters'

result = json.loads(data)

print 'count: ', len(result['comments'])

total = sum(num['count'] for num in result['comments'])
print 'Sum:' , total