#Author: Dhairya Dand
#http://dhairyadand.com

import urllib
from BeautifulSoup import BeautifulSoup

def getSet(q1, q2, q3, q4, q5):
	L = []
	f = urllib.urlopen("http://labs.google.com/sets?hl=en&q1="+q1+"&q2="+q2+"&q3="+q3+"&q4="+q4+"&q5="+q5+"&btn=Large+Set")
	text = f.read()
	f.close()
	
	soup = BeautifulSoup(text)
	
	links = soup.findAll("a")
	
	for link in links:
		if(link['href']!= '/sets' and link.string!= 'Discuss' and link.string!= 'Terms of Use' and link.string!= 'labs.google.com' and link.string!= 'All About Google'):
			L.append(link.string)
	
	return L


