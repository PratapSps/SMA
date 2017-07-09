'''
Created on Jul 6, 2017

@author: Survya Pratap Singh
Wright State University
UID: U00803205
email: singh.survya@gmail.com
website: https://survya.com
'''
import requests
from bs4 import BeautifulSoup
 
url = "https://www.peoplesmart.com/default-name-results?Find=Vance%20Saunders&FirstName=Vance&LastName=Saunders&Near=Ohio&State=OH"
r = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
print (r)
soup = BeautifulSoup(r.text, "lxml")
data=(soup.find('body').text)
print(data)