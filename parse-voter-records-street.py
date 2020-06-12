from bs4 import BeautifulSoup
import os


if __name__ == '__main__':
	files = os.listdir('voter-records-street')
	names = []
	for i in range(0, len(files)):
		print('Reading file {} of {}'.format(i + 1, len(files)))
		with open('voter-records-street/{}'.format(files[i]), 'r') as rfh:
			s = BeautifulSoup(rfh.read(), 'html.parser')
			names += s.find_all('span', {'itemprop': 'name'})

	with open('names-street.txt', 'w') as wfh:
		fnames = []
		for j in names:  # format names before saving them
			n = j.get_text().split(' ')
			if len(n) == 3:  # if middle initial/name is present
				n = '+'.join([n[2], n[0]])
			else:
				n = '+'.join([n[1], n[0]])
			n = n.replace("'", "")
			fnames.append(n)

		fnames = list(set(fnames))  # remove duplicates	
		fnames.sort()
		for k in fnames:
			wfh.write('{}\n'.format(k))
