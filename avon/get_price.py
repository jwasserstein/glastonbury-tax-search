from bs4 import BeautifulSoup
import os


def grab_assessed_value(html):
    soup = BeautifulSoup(html, 'html.parser')
    for anchor in soup.find_all('pre'):
        assessed_val = str(anchor).split('Total assessments')  # split by Total assessments
        assessed_val = assessed_val[1].split('|')  # take everything after Total assessments, and split it by |
        assessed_val = assessed_val[0].strip()  # take everything in front of the first |, and strip away whitespace
        if assessed_val is None:
            continue
        return ''.join(assessed_val.split(','))


def grab_address(html):
    soup = BeautifulSoup(html, 'html.parser')
    for anchor in soup.find_all('h3'):
        address = str(anchor).split('Property at')  # split by Property at
        address = address[1].split('Prop ID')  # take everything after Property at, and split it by Prop ID
        address = address[0].strip()  # take everything in front of the first Prop ID, and strip away
        # whitespace
        if address is None:
            continue
        return ' '.join(address.lstrip('0').split())


def grab_owner(html):
    soup = BeautifulSoup(html, 'html.parser')
    for anchor in soup.find_all('pre'):
        owner = str(anchor).split('Owner name:')  # split by Owner name
        owner = owner[1].split('|')  # take everything after Owner name, and split it by |
        owner = owner[0].strip()  # take everything in front of the first |, and strip away whitespace
        if owner is None:
            continue
        return ' '.join(owner.split(','))


if __name__ == '__main__':
    addresses = ['Address']  # initialize storage variable with header
    values = ['Value']  # initialize storage variable with header
    file_names = ['File Names']

    for j in range(65, 91):
        print('processing all {}s'.format(chr(j)))
        os.chdir('html/{}'.format(chr(j)))
        ls = os.listdir()
        for i in ls:
            if i == '.DS_Store':
                continue
            with open(i, 'r') as f:
                file_data = f.read()
                if 'Resident' in file_data:
                    addresses.append(grab_address(file_data))
                    values.append(grab_assessed_value(file_data))
                    owners.append(grab_owner(file_data))
                    file_names.append(i)
        os.chdir('..')
        os.chdir('..')

    with open('output.csv', 'w') as f:
        for i in range(0, len(addresses)-1):
            f.write('{}, {}, ${}, {}\n'.format(str(owners[i]), str(addresses[i]), str(values[i]), str(file_names[i])))
