from bs4 import BeautifulSoup
from urllib.request import urlopen

cfpp_transcription_url = 'http://cfpp2000.univ-paris3.fr/Corpus.html#transcriptionTEI'

# create response object
html = urlopen(cfpp_transcription_url)
# create beautiful-soup object
soup = BeautifulSoup(html,'html.parser')

for ol in soup.find_all('ol'):
    for li in ol.find_all('li'):
        a = li.find('a')
        try:
            link = a['href']
            content = urlopen(link).read()
            file_name = link.split('/')[-1].split('.')[0]
            with open(file_name, 'w') as f:
                f.write(content.decode('utf-8'))
        except:
            pass
