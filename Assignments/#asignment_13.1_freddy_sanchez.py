#asignment_13.1_freddy_sanchez

import urllib
from BeautifulSoup import * 

url = 'http://python-data.dr-chuck.net/comments_242234.xml'

lst = [] 
	lst.append(int(tag.contents[0]))
print sum(lst)