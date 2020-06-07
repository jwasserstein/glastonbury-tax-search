from bs4 import BeautifulSoup
import os


def grab_data(html):
	s = BeautifulSoup(html, 'html.parser')  
	ci = s.find('div', {'class': 'cart-info'}) 
	if ci is None:
		return [], [], []
	rows = ci.find_all('tr', {'class': ['odd', 'even']})
	if rows is None:
		return [], [], []
	n = []
	v = []
	t = []
	for i in rows:
		if "MOTOR VEHICLE" not in str(i):  # pass this row if it's not a vehicle
			continue
		if "2018" not in str(i.find('td').find('span')):  # pass this row if it's not from 2018
			continue
		cols = i.find_all('td')
		if cols is None:
			continue
		n += [cols[1].find('b').get_text().strip()]
		v += [' '.join(cols[2].get_text().split())]
		t += [cols[3].get_text().strip()[1:]]
	return n, v, t
		

if __name__ == '__main__':
	names = []
	vehicles = []
	taxes = []
	files = os.listdir('tax-records/')  # list files
	num_files = len(files)
	count = 0
	for f in files:  # loop over files
		count += 1
		print('parsing file {} of {}.  File name: {}'.format(count, num_files, f))
		with open('tax-records/{}'.format(f), 'r') as rfh:  # rfh = read file handle
			try:
				html = rfh.read()
			except:
				print('failed reading file {}'.format(f))
				continue
			n, v, t = grab_data(html)  # vehicles is a list of tuples, where each tuple is a vehicle-tax pair
			names += n
			vehicles += v
			taxes += t
	with open('vehicles.txt', 'w') as fh:
		for i in range(0, len(names)):
			fh.write('{}, {}, {}\n'.format(taxes[i], vehicles[i], names[i]))  
