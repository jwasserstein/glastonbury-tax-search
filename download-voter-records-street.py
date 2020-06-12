from bs4 import BeautifulSoup
import requests
import time
import re
import os

delay = 3  # delay between downloads in seconds


def save_html(html, name, number):
	print('Writing file {}-{}.html'.format(name, number))
	with open('voter-records-street/{}-{}.html'.format(name, number), 'w') as wfh:
		wfh.write(html)	


if __name__ == '__main__':
	# Begin Loading Streets
	with open('streets.txt', 'r') as rfh:
		streets = set(rfh.read().split('\n')[:-1])  # determine which files are needed
	ls = os.listdir('voter-records-street')
	# End Loading Streets


	# Begin Glastonbury
	r = re.compile('^(.*[^s])g-[0-9]+.html$')
	g_existing_files = []
	for j in ls:
		m = r.match(j)
		if m is None:
			continue
		g_existing_files.append(m.group(1))  # determine which files already exist in Glastonbury
	g_existing_files = set(g_existing_files)
	g_needed_files = streets - g_existing_files  # determine which files must be downloaded from Glastonbury
	print('{} of {} streets still need to be downloaded from Glastonbury'.format(len(g_needed_files), len(streets)))
	for i in g_needed_files:
		print('Attempting to fetch {} in Glastonbury'.format(i))
		url = 'https://voterrecords.com/street/{}-glastonbury-ct/'.format(i)
		response = requests.get(url)	
		if response.status_code == 200:
			save_html(response.text, i+'g', 1)
			s = BeautifulSoup(response.text, 'html.parser')
			p = s.find('label', {'class': 'lead BottomMarginZero pull-left'})
			o = re.search('Page 1 of ([0-9]*)', p.get_text())
			if o is None:
				print("couldn't find page number")
				continue
			print('found {} pages'.format(o.group(1)))
			for j in range(2, int(o.group(1)) + 1):  # start at 2 because first page was already written
				time.sleep(delay)
				page_url = url + str(j)
				response = requests.get(page_url)
				save_html(response.text, i+'g', j)
		else:
			print('HTTP response code was not 200.  Code: {}'.format(response.status_code))
			save_html(response.text, i+'g', response.status_code)
		time.sleep(delay)
	# End Glastonbury

	# Begin South Glastobury
	r = re.compile('^(.*)sg-[0-9]+.html$')
	sg_existing_files = []
	for j in ls:
		m = r.match(j)
		if m is None:
			continue
		sg_existing_files.append(m.group(1))  # determine which files already exist in South Glastonbury
	sg_existing_files = set(sg_existing_files)
	sg_needed_files = streets - sg_existing_files  # determine which files must be downloaded from South Glastonbury
	print('{} of {} streets still need to be downloaded from South Glastonbury'.format(len(sg_needed_files), len(streets)))
	for i in sg_needed_files:
		print('Attempting to fetch {} in South Glastonbury'.format(i))
		url = 'https://voterrecords.com/street/{}-south+glastonbury-ct/'.format(i)
		response = requests.get(url)
		if response.status_code == 200:
			save_html(response.text, i+'sg', 1)
			s = BeautifulSoup(response.text, 'html.parser')
			p = s.find('label', {'class': 'lead BottomMarginZero pull-left'})
			o = re.search('Page 1 of ([0-9]*)', p.get_text())
			if o is None:
				print("couldn't find page number")
				continue
			print('found {} pages'.format(o.group(1)))
			for j in range(2, int(o.group(1)) + 1):  # start at 2 because first page was already written
				time.sleep(delay)
				page_url = url + str(j)
				response = requests.get(page_url)
				save_html(response.text, i+'sg', j)
		else:
			print('HTTP response code was not 200.  Code: {}'.format(response.status_code))
			save_html(response.text, i+'sg', response.status_code)
		time.sleep(delay)
	# End South Glastonbury
