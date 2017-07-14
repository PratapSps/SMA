'''
Created on Jul 12, 2017

@author: Survya Pratap Singh
Wright State University
UID: U00803205
email: singh.survya@gmail.com
website: https://survya.com
'''

import requests
from bs4 import BeautifulSoup
import json

query='"survya singh"'+'+'+'Linkedin'

url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch&nfpr=1"



r = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
soup = BeautifulSoup(r.text, "html.parser")
findG=soup.find_all('div', {'class':'rg_meta'})
for a in findG:
    webLeakageSrc=json.loads(a.text)["isu"]
    Imagelink=json.loads(a.text)["ou"]
    ImageHeading=json.loads(a.text)["pt"]
    Imagedata=json.loads(a.text)["s"]
    print(webLeakageSrc)
    print(Imagelink)
    print(ImageHeading)
    print(Imagedata)



