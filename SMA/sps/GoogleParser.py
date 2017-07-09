'''
Created on Jul 6, 2017

@author: Survya pratap Singh
'''
import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=sayali+sheode"
r = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
soup = BeautifulSoup(r.text, "html.parser")
# name=soup.find('h3', attrs={'class': 'r'})
findG=soup.find_all('div', {'class':"rc"})

for div in findG:
    print(div.find('h3', attrs={'class': 'r'}).text)
    print(div.find('cite').text)