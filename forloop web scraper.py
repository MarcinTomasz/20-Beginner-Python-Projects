#Web scraper for forloop.ai

from bs4 import BeautifulSoup
import requests
from csv import writer

url= 'https://www.immowelt.at/liste/wien/wohnungen/mieten?sort=relevanz'
page = requests.get(url)

soup= BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_= 'EstateItem-1c115')

with open('flats.csv', 'w', encoding='utf8', newline= '') as f:
    thewriter=writer(f)
    header= ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)
    
for list in lists:
    price = list.find('div', class= 'KeyFacts-efbce')
    
