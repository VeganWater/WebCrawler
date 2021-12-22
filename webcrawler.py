from bs4 import BeautifulSoup
import requests

def trade_spider(max_page):
    page = 1
    while page <= max_page:
        url = 'http://python.beispiel.programmierenlernen.io/index.php?page='+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'html.parser')
#        for link in soup.find_all(['h4','span']):
#                      print(link.string)
#        page+=1
        for link in soup.findAll('span',{'class':'emoji'}):

           print(link.string)
        page+=1

trade_spider(9)


            



