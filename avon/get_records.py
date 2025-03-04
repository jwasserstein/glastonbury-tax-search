from bs4 import BeautifulSoup
import os


os.chdir('html/')

for j in range(90, 91):
    print('Downloading letter: ', chr(j))
    os.system('mkdir ' + chr(j))
    os.chdir(chr(j) + '/')
    os.system('wget http://www.avonassessor.com/propcards/' + chr(j) + 'owner.html')

    with open(chr(j) + 'owner.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        a = soup.find_all('a')
        for i in a:
            ihref = i.get('href')
            if ihref is None or ihref == '/index.html':
                continue
            print('running: ' + 'wget http://www.avonassessor.com' + ihref)
            os.system('wget http://www.avonassessor.com' + ihref)

    os.chdir('..')