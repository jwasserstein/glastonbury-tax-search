from bs4 import BeautifulSoup
import requests
import time
import re

if __name__ == '__main__':
	with open('streets.txt', 'r') as rfh:
		streets = rfh.read().split('\n')[:-1]
	for i in streets:
		print('Attempting to fetch {}'.format(i))
		url = 'https://voterrecords.com/street/{}-glastonbury-ct/'.format(i)
		response = requests.get(url)	
		if response.status_code != 200:
			print("Glastonbury didn't work, trying South Glastonbury")
			time.sleep(20)
			url = 'https://voterrecords.com/street/{}-south+glastonbury-ct/'.format(i)
			response = requests.get(url)
			if response.status_code != 200:
				print("Couldn't fetch {}".format(i))
				continue

		print('Writing file {}-{}'.format(i, 1))
		with open('voter-records-street/{}-{}'.format(i, 1), 'w') as wfh:
			wfh.write(response.text)	

		s = BeautifulSoup(response.text, 'html.parser')
		p = s.find('label', {'class': 'lead BottomMarginZero pull-left'})
		o = re.search('Page 1 of ([0-9]*)', p.get_text())
		if o is None:
			print("couldn't find page numbers")
			continue
		for j in range(2, int(o.group(1))):  # start at 2 because first page was already written
			time.sleep(20)
			page_url = url + str(j)
			response = requests.get(page_url)
			print('Writing file {}-{}'.format(i, j))
			with open('voter-records-street/{}-{}'.format(i, j), 'w') as wfh:
				wfh.write(response.text)	
		time.sleep(20)
