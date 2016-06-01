#assignment_15.1_freddy_sanchez 
import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'


while True:
	location = raw_input('Enter location: ')
	if len(location) < 1 : break

	url = serviceurl+urllib.urlencode({'sensor':'false','address':location})

	print 'Retrieving', url
	urlhandle = urllib.urlopen(url)
	data = urlhandle.read()
	print 'Retrieved', len(data), 'characters'

	try: js = json.loads(str(data))
	except: js = None
	if 'status' not in js or js['status'] != 'OK':
		print 'Faliure to Retrieve'
		print data
		continue

	place = js["results"][0]["place_id"]

	print 'Place ID: ', place