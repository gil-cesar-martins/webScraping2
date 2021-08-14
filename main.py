from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, "html.parser")
imagens = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})

for imagem in imagens:
    print(imagem['src'])