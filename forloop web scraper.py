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
    header= ['Price', 'Area', 'Rooms']
    thewriter.writerow(header)

    flats= []
    
    for list in lists:
        #title= list.find('div', 'h2').text
        price= list.find('div', attrs= {'data-test':'price'}).text
        area= list.find('div', attrs= {'data-test':'area'}).text
        rooms= list.find('div', attrs= {'data-test':'rooms'}).text
        info= [price, area, rooms]
        thewriter.writerow(info)
        flats.append(info)

print(flats)