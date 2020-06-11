from bs4 import BeautifulSoup
import requests
import time
import re
import os

delay = 30  # delay between downloads in seconds


def save_html(html, name, number):
	print('Writing file {}-{}.html'.format(name, number))
	with open('voter-records-street/{}-{}.html'.format(name, number), 'w') as wfh:
		wfh.write(html)	


if __name__ == '__main__':
	with open('streets.txt', 'r') as rfh:
		streets = set(rfh.read().split('\n')[:-1])  # determine which files are needed

	ls = os.listdir('voter-records-street')
	r = re.compile('^(.*)-[0-9]+.?.*$')
	existing_files = []
	for j in ls:
		m = r.match(j)
		existing_files.append(m.group(1))  # determine which files already exist
	existing_files = set(existing_files)

	needed_files = streets - existing_files  # determine which files must be downloaded
	print('{} of {} streets still need to be downloaded'.format(len(needed_files), len(streets)))
	for i in needed_files:
		print('Attempting to fetch {}'.format(i))
		url = 'https://voterrecords.com/street/{}-glastonbury-ct/'.format(i)
		response = requests.get(url)	
		if response.status_code != 200:
			print("Glastonbury didn't work, trying South Glastonbury")
			time.sleep(delay)
			url = 'https://voterrecords.com/street/{}-south+glastonbury-ct/'.format(i)
			response = requests.get(url)
			if response.status_code != 200:
				print("Couldn't fetch {}".format(i))
				continue

		save_html(response.text, i, 1)

		s = BeautifulSoup(response.text, 'html.parser')
		p = s.find('label', {'class': 'lead BottomMarginZero pull-left'})
		o = re.search('Page 1 of ([0-9]*)', p.get_text())
		if o is None:
			print("couldn't find page numbers")
			continue
		print('found {} pages'.format(o.group(1)))
		for j in range(2, int(o.group(1)) + 1):  # start at 2 because first page was already written
			time.sleep(delay)
			page_url = url + str(j)
			response = requests.get(page_url)
			save_html(response.text, i, j)
		time.sleep(delay)
