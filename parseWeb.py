import BeautifulSoup
import urllib
import os
import re
#html = urllib.urlopen('http://www.nytimes.com/2009/12/21/us/21storm.html').read()
html=open("web1",'r').read()
soup = BeautifulSoup.BeautifulSoup(html)
texts = soup.findAll(text=True)
remWords=[['&[^ ]*;',''],['[ ]* ',' '],['\t',' ']]
stopList=['===================','<!.*>','<?.*?>','\+{20}']
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    for stop in stopList:
	if re.match(stop,str(element)):
		return False
    return True

visible_texts = filter(visible, texts)
s= visible_texts
st=""
for p in s:
	if '\n' not in p:	#print st
	        st=st+str(p)
	st=st+" "
for rem in remWords:
	st=re.sub(rem[0],rem[1],str(st))
print st	
