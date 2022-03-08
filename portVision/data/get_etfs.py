import requests 
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.cnbc.com/funds-and-etfs/"

res = requests.get(url).content

soup = BeautifulSoup(res, 'lxml')

# tables = soup.find_all('tbody',class_="BasicTable-tableBody")
td = soup.find_all("td", attrs={"class": "BasicTable-symbol"})

print(td)
# for table in tables:
#     tds = table.find_all('td',class_="BasicTable-symbol")
#     print(tds)





 