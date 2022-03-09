import requests 
from bs4 import BeautifulSoup
import pandas as pd
from lxml import etree


from selenium import webdriver 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.cnbc.com/funds-and-etfs/"

url2 = "https://www.barchart.com/etfs-funds/volume-leaders/price-leaders?orderBy=priceVolume&orderDir=desc"

driver = webdriver.Chrome('/Users/MichaelBallard/Downloads/chromedriver')

driver.get(url)


html = driver.page_source

# print(html)

# tbl =driver.find_element(By.CLASS_NAME,'BasicTable-tableBody')

# print(tbl)

soup = BeautifulSoup(html, 'html.parser')
dom = etree.HTML(str(soup))
# tbl = dom.xpath('//*[@id="MarketData-MarketsSectionTable-4"]/section/div[1]/div/div/div/div/table/tbody')[0]

# print(dir(dom))
body = dom.getchildren()[1]

tbl = body.findall('//*[@id="MarketData-MarketsSectionTable-4"]/section/div[1]/div/div/div/div/table/tbody/tr[1]/td[1]')

# print(tbl.text)
# tables = soup.find_all('td',class_="BasicTable-symbol")

# print(tables)
# tbodies = soup.find_all("tbody", attrs={"class": "BasicTable-symbol"})
