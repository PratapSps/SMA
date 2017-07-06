import requests
from bs4 import BeautifulSoup

goog_search = "https://www.google.com/search?q=sayali+sheode+linkedin"


r = requests.get(goog_search)

soup = BeautifulSoup(r.text, "lxml")
name=soup.find('h3', attrs={'class': 'r'})
name_soup=BeautifulSoup(name.text,"lxml")
print(name_soup)
