from bs4 import BeautifulSoup
import os
import re

def grab_street_name(html):
	s = BeautifulSoup(html, 'html.parser')
	a = s.find_all('a', {'href': re.compile('Streets.aspx\?Name=[A-Z]*')})	
	ret = []
	for i in a:
		ret.append(i.get_text().replace(' ', '+'))
	return ret

if __name__ == '__main__':
	streets = []
	files = os.listdir('street-records')
	numfiles = len(files)
	count = 0
	for f in files:
		count += 1
		print('parsing file {} of {}.  File name: {}'.format(count, numfiles, f))
		with open('street-records/{}'.format(f), 'r') as rfh:
			streets += grab_street_name(rfh.read())
	with open('streets.txt', 'w') as wfh:
		for i in range(0, len(streets)):
			wfh.write('{}\n'.format(streets[i]))
