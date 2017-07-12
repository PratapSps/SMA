'''
Created on Jul 9, 2017

@author: Survya pratap singh
'''
from sps import AppVariables
import requests
from bs4 import BeautifulSoup
from sps.createAppGui import *
from sps.AppVariables import app


class BackEndProcess():
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
    
    
    def googleUrl(self):
        '''
        Method which search google.com based on input provided by the user
        It creates dynamic link based on user input.
        '''
        AppVariables.FirstLast='"'+AppVariables.First_Name_data +'+' +AppVariables.Last_Name_data+'"&nfpr=1'
        if AppVariables.Middle_Name_data != "" :
            AppVariables.FirstMiddleLast='"'+AppVariables.First_Name_data+'+'+AppVariables.Middle_Name_data+'+'+AppVariables.Last_Name_data+'"&nfpr=1'
            
        if AppVariables.Country_data != "" :
            AppVariables.FirstLastCoun='"'+AppVariables.First_Name_data +'+' +AppVariables.Last_Name_data+'"+'+AppVariables.Country_data+'"&nfpr=1'
            if AppVariables.Middle_Name_data != "" :
               AppVariables.FirstMLastCoun='"'+AppVariables.First_Name_data +'+'+AppVariables.Middle_Name_data+'+'+AppVariables.Last_Name_data+'"+'+AppVariables.Country_data+'"&nfpr=1' 
        
        if AppVariables.State_data != "" :
            AppVariables.FirstLastState='"'+AppVariables.First_Name_data +'+' +AppVariables.Last_Name_data+'"+'+AppVariables.State_data+'"&nfpr=1'
            if AppVariables.Middle_Name_data != "" :
                AppVariables.FirstMLastState='"'+AppVariables.First_Name_data +'+' +AppVariables.Middle_Name_data+'+'+AppVariables.Last_Name_data+'"+'+AppVariables.State_data+'"&nfpr=1'
        
        if AppVariables.City_data != "" :
            AppVariables.FirstLastCity='"'+AppVariables.First_Name_data +'+' +AppVariables.Last_Name_data+'"+'+AppVariables.City_data+'"&nfpr=1'
            if AppVariables.Middle_Name_data != "" :
                AppVariables.FirstMLastCity='"'+AppVariables.First_Name_data +'+' +AppVariables.Middle_Name_data+'+'+AppVariables.Last_Name_data+'"+'+AppVariables.City_data+'"&nfpr=1'
            
        if AppVariables.School_Name_data != "" :
            AppVariables.FirstLastSchool='"'+AppVariables.First_Name_data +'+' +AppVariables.Last_Name_data+'"+'+AppVariables.School_Name_data+'"&nfpr=1'
            if AppVariables.Middle_Name_data != "" :
                AppVariables.FirstMLastSchool='"'+AppVariables.First_Name_data +'+'+AppVariables.Middle_Name_data+'+' +AppVariables.Last_Name_data+'"+'+AppVariables.School_Name_data+'"&nfpr=1'
        
        if AppVariables.Email_data != "" :
            AppVariables.UserEmailID='"'+AppVariables.Email_data+'"'+'&nfpr=1'
        
        UniqueSearchURl=[]
        url1=""
        url2=""
        url3=""
        url4=""
        url5=""
        url6=""
        url7=""
        url8=""
        url9=""
        url10=""
        url11=""
        
        
        url1=AppVariables.googleBaseUrl+AppVariables.FirstLast
        if AppVariables.FirstMiddleLast!="":
            url2=AppVariables.googleBaseUrl+AppVariables.FirstMiddleLast
            if AppVariables.googleBaseUrl+AppVariables.FirstMLastCoun != AppVariables.googleBaseUrl+"" :
                url7=AppVariables.googleBaseUrl+AppVariables.FirstMLastCoun
            if AppVariables.googleBaseUrl+AppVariables.FirstMLastState != AppVariables.googleBaseUrl+"" :
                url8=AppVariables.googleBaseUrl+AppVariables.FirstMLastState
            if AppVariables.googleBaseUrl+AppVariables.FirstMLastCity != AppVariables.googleBaseUrl+"" :
                url9=AppVariables.googleBaseUrl+AppVariables.FirstMLastCity
            if AppVariables.googleBaseUrl+AppVariables.FirstMLastSchool != AppVariables.googleBaseUrl+"" :
                url10=AppVariables.googleBaseUrl+AppVariables.FirstMLastSchool
            
        if AppVariables.FirstLastCoun!="":
            url3=AppVariables.googleBaseUrl+AppVariables.FirstLastCoun  
            
        if AppVariables.FirstLastState!="":
            url4=AppVariables.googleBaseUrl+AppVariables.FirstLastState
            
        if AppVariables.FirstLastCity!="":
            url5=AppVariables.googleBaseUrl+AppVariables.FirstLastCity

        if AppVariables.FirstLastSchool!="":
            url6=AppVariables.googleBaseUrl+AppVariables.FirstLastSchool

        if AppVariables.UserEmailID !="":
            url11=AppVariables.googleBaseUrl+AppVariables.UserEmailID
        
        UniqueSearchURl.append(url1)
        if url2 != "":
          UniqueSearchURl.append(url2)
          
        if url3 != "":
          UniqueSearchURl.append(url3)

        if url4 != "":
          UniqueSearchURl.append(url4)
          
        if url5 != "":
          UniqueSearchURl.append(url5)
          
        if url6 != "":
          UniqueSearchURl.append(url6)  
        
        if url7 != "":
          UniqueSearchURl.append(url7)
        
        if url8 != "":
          UniqueSearchURl.append(url8)
          
        if url9 != "":
          UniqueSearchURl.append(url9)
        
        if url10 != "":
          UniqueSearchURl.append(url10)
        
        if url11 != "":
          UniqueSearchURl.append(url11)
        
        BackEndProcess().findUniqueGoogleSearch(UniqueSearchURl)
#         print (UniqueSearchURl)
#         
    #find unique link from each url that is being search in google
    def findUniqueGoogleSearch(self,searchUrl):
#         print (searchUrl)
        count=0
        for url in searchUrl:
            
            if len(searchUrl)==1:
                print ('####################################'+url+'#####################################')
                self.googleParser(url)
#                 print (url)
            else:
               if count==0:
                   count+=1
                   continue
               else:
                   print ('####################################'+url+'#####################################')
                   self.googleParser(url) 
#                     print (url)
            count+=1
          
        
        
    #crawl google search page
    def googleParser(self,url):
#         print(url)
        app.update()
        r = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
        sps.createAppGui.Animation(self,sps.createAppGui.innerFrame,500,210)
        app.update()
         
        soup = BeautifulSoup(r.text, "html.parser")
        findG=soup.find_all('div', {'class':"rc"})
        for div in findG:
            print((div.find('h3', attrs={'class': 'r'}).text).encode(encoding='UTF-8',errors='strict'))
            print((div.find('cite').text).encode(encoding='UTF-8',errors='strict'))
            print((div.find('span',attrs={'class':"st"}).text).encode(encoding='UTF-8',errors='strict'))
        app.update()
        
                 
        
    
    #Search for user first and last name in the header and links
    def NormalizeGoogleSearchedURL(self,header,data,key):
        '''
        
        '''
        
        
    def initalizedSearchData(self):
        AppVariables.data_FL=AppVariables.First_Name_data+" "+AppVariables.Last_Name_data
        if AppVariables.Middle_Name_data !="":
            AppVariables.data_FLM=AppVariables.First_Name_data+" "+AppVariables.Middle_Name_data+" "+AppVariables.Last_Name_data
            AppVariables.data_F_M=AppVariables.First_Name_data+"."+AppVariables.Middle_Name_data
            AppVariables.data_M_F=AppVariables.Middle_Name_data+"."+AppVariables.First_Name_data
            AppVariables.data_L_M=AppVariables.Last_Name_data+"."+AppVariables.Middle_Name_data
            AppVariables.data_M_L=AppVariables.Middle_Name_data+"."+AppVariables.Last_Name_data
                        
        AppVariables.data_LF=AppVariables.Last_Name_data+" "+AppVariables.First_Name_data
        AppVariables.data_F_L=AppVariables.First_Name_data+"."+AppVariables.Last_Name_data
        AppVariables.data_L_F=AppVariables.Last_Name_data+"."+AppVariables.First_Name_data
        
        
        
        
        
        
        
        
        