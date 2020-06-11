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
		for j in names:
			formatted_name = j.get_text().split(' ')
			if len(formatted_name) == 3:  # if middle initial/name is present
				formatted_name = '+'.join([formatted_name[2], formatted_name[0]])
			else:
				formatted_name = '+'.join([formatted_name[1], formatted_name[0]])
			wfh.write('{}\n'.format(formatted_name))
