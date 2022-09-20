#Web scraper for forloop.ai

import sys
import time
from bs4 import BeautifulSoup
import requests
from csv import writer
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#Keep browser window open until closed manually
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Website to scrape data from
url= 'https://www.immowelt.at/'
page = requests.get(url)

#Open browser
PATH = "C:\\Users\\novyp\\Desktop\\Python\\Webdrivers\\chromedriver.exe"
browser = webdriver.Chrome(chrome_options=options, executable_path= PATH)
browser.get(url)
time.sleep(2)

#Click Accept cookies
ok= browser.find_element(by= By.XPATH, value= "//button[@role='button']")
ActionChains(browser).move_to_element(ok).pause(1).click(ok).perform()

#User selects city to search for
city = input("Scrape information for flats in: ")


#Open csv file with header labels.
with open('flats.csv', 'w', encoding='utf8', newline= '') as f:
    thewriter=writer(f)
    header= ['Title', 'Price', 'Area', 'Rooms']
    thewriter.writerow(header)
    
    flats= []
    while len(flats) < 500:
        
        soup= BeautifulSoup(page.content, 'html.parser')
        lists = soup.find_all('div', class_= 'EstateItem-1c115')
    
        for list in lists:
            title= list.find('h2').text
            price= list.find('div', attrs= {'data-test':'price'}).text.replace(' €', '')
            area= list.find('div', attrs= {'data-test':'area'}).text
            rooms= list.find('div', attrs= {'data-test':'rooms'}).text 
            
            info= [title, price, area, rooms]
            thewriter.writerow(info)
            flats.append(info)
        
        next_page = soup.select('a[rel = "prev"]')[0]
            
            
    
print(len(flats))

#print(flats)