from bs4 import BeautifulSoup
import os


def grab_names(html):
	soup = BeautifulSoup(html, 'html.parser')
	ret = []  # initialize return array
	for n in soup.find_all('span', itemprop='name'):
		name = n.get_text().strip()
		if name not in ret:  # avoid duplicates
			ret.append(name)
	return ret
	

if __name__ == '__main__':
	names = []  # initialize name array
	files = os.listdir('voter-records/')  # list files
	num_files = len(files)
	count = 0
	for f in files:  # loop over files
		count += 1
		print('parsing file {} of {}'.format(count, num_files))
		with open('voter-records/{}'.format(f), 'r') as rfh:  # rfh = read file handle
			names = names + grab_names(rfh.read())  # add names to name list
	with open('names.txt', 'w') as fh:
		for i in names:
			fh.write('{}\n'.format(i))  # store output in text file
