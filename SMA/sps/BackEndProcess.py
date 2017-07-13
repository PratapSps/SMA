'''
Created on Jul 9, 2017

@author: Survya pratap singh
'''
from sps import AppVariables
import requests
from bs4 import BeautifulSoup
from sps.createAppGui import *
from sps.AppVariables import app
import re


class BackEndProcess():
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    #clear all the stored data and begin new search  
    def clearAllList(self):
        #variables to be cleaned before new search
        sps.AppVariables.phone_numbers={}
        sps.AppVariables.email_id={}
        sps.AppVariables.userAddress={}
        sps.AppVariables.mid_Link_dict={}
        sps.AppVariables.high_Link_dict={}
        sps.AppVariables.low_Link_dict={}
        sps.AppVariables.SocialMeidaIdDict={}
        
        #important method which calls all the method.
        self.googleUrl() 
        newTempDict=sps.AppVariables.high_Link_dict
        newTempDict.update(sps.AppVariables.mid_Link_dict)
        self.getSocialMediaId(newTempDict)
        print(AppVariables.phone_numbers)
        print(AppVariables.email_id)
        print(AppVariables.userAddress)
        print(sps.AppVariables.high_Link_dict)
        print(sps.AppVariables.mid_Link_dict)
        print(sps.AppVariables.low_Link_dict)
        print(sps.AppVariables.SocialMeidaIdDict)
        
        
    
    def googleUrl(self):
        '''
        Method which search google.com based on input provided by the user
        It creates dynamic link based on user input.
        '''
        AppVariables.FirstLast='"'+AppVariables.First_Name_data +'+' +AppVariables.Last_Name_data+'"'+'&nfpr=1'
        if AppVariables.Middle_Name_data != "" :
            AppVariables.FirstMiddleLast='"'+AppVariables.First_Name_data+'+'+AppVariables.Middle_Name_data+'+'+AppVariables.Last_Name_data+'"'+'&nfpr=1'
            
        if AppVariables.Country_data != "" :
            AppVariables.FirstLastCoun='"'+AppVariables.First_Name_data +'+' +AppVariables.Last_Name_data+'"'+'%20'+AppVariables.Country_data+'&nfpr=1'
            if AppVariables.Middle_Name_data != "" :
               AppVariables.FirstMLastCoun='"'+AppVariables.First_Name_data +'+'+AppVariables.Middle_Name_data+'+'+AppVariables.Last_Name_data+'"'+'%20'+AppVariables.Country_data+'&nfpr=1' 
        
        if AppVariables.State_data != "" :
            AppVariables.FirstLastState='"'+AppVariables.First_Name_data +'+' +AppVariables.Last_Name_data+'"'+'%20'+AppVariables.State_data+'&nfpr=1'
            if AppVariables.Middle_Name_data != "" :
                AppVariables.FirstMLastState='"'+AppVariables.First_Name_data +'+' +AppVariables.Middle_Name_data+'+'+AppVariables.Last_Name_data+'"'+'%20'+AppVariables.State_data+'&nfpr=1'
        
        if AppVariables.City_data != "" :
            AppVariables.FirstLastCity='"'+AppVariables.First_Name_data +'+' +AppVariables.Last_Name_data+'"'+'%20'+AppVariables.City_data+'&nfpr=1'
            if AppVariables.Middle_Name_data != "" :
                AppVariables.FirstMLastCity='"'+AppVariables.First_Name_data +'+' +AppVariables.Middle_Name_data+'+'+AppVariables.Last_Name_data+'"'+'%20'+AppVariables.City_data+'&nfpr=1'
            
        if AppVariables.School_Name_data != "" :
            AppVariables.FirstLastSchool='"'+AppVariables.First_Name_data +'+' +AppVariables.Last_Name_data+'"'+'%20'+AppVariables.School_Name_data+'&nfpr=1'
            if AppVariables.Middle_Name_data != "" :
                AppVariables.FirstMLastSchool='"'+AppVariables.First_Name_data +'+'+AppVariables.Middle_Name_data+'+' +AppVariables.Last_Name_data+'"'+'%20'+AppVariables.School_Name_data+'&nfpr=1'
        
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
#                 print ('####################################'+url+'#####################################')
                self.googleParser(url)
#                 print (url)
            else:
               if count==0:
                   count+=1
                   continue
               else:
#                    print ('####################################'+url+'#####################################')
                   self.googleParser(url) 
#                     print (url)
            count+=1
          
        
        
    #crawl google search page
    def googleParser(self,url):
#         print(url)
        app.update()
        r = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
#         sps.createAppGui.Animation(self,sps.createAppGui.innerFrame,500,210)
        app.update()
         
        soup = BeautifulSoup(r.text, "html.parser")
        findG=soup.find_all('div', {'class':"rc"})
        for div in findG:
            title=((div.find('h3', attrs={'class': 'r'}).text).encode(encoding='UTF-8',errors='strict'))
#             print(title)
            key=((div.find('cite').text).encode(encoding='UTF-8',errors='strict'))
#             print(key)
            data=((div.find('span',attrs={'class':"st"}).text).encode(encoding='UTF-8',errors='strict'))
#             print(data)
            self.ParseFirstHandInfo(key.decode("utf-8"),title.decode("utf-8"),data.decode("utf-8"))
        app.update()
        
                 
        
    
    #Search for user first and last name in the header and links
    def ParseFirstHandInfo(self,key,title,urlData):
        '''
        Method which search the content for email,phone and address and decide the criticality of links found in google search
        create method to check name in data
        if data has email phone address
        make it high
        else 
        check heading contains name
        put it in mid
        else low
        '''
        
        
        if self.checkNamesInData(urlData):
            if self.ParsePhoneNum(urlData) or self.ParseEmail(urlData) or self.ParseAddress(urlData):
                self.ParsePhoneNum(urlData)
                self.ParseEmail(urlData)
                self.ParseAddress(urlData)
                tempdict={key:[title,urlData]}
                sps.AppVariables.high_Link_dict.update(tempdict)
            elif self.checkNamesInData(title):
                tempdict1={key:[title,urlData]}
                sps.AppVariables.mid_Link_dict.update(tempdict1)
            else:
                tempdict2={key:[title]}
                sps.AppVariables.low_Link_dict.update(tempdict2)
        else:
            if self.checkNamesInData(title):
                tempdict1={key:[title,urlData]}
                sps.AppVariables.mid_Link_dict.update(tempdict1)
            else:
                tempdict2={key:[title]}
                sps.AppVariables.low_Link_dict.update(tempdict2)
            
                
                
            
        
    
    
    #parse phone number from the link
    def ParsePhoneNum(self,data):
        phoneRegrex=re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
        result = re.search(phoneRegrex, data)
        if result:
            temp={result.group(0):""}
            sps.AppVariables.phone_numbers.update(temp)
            return True
        else:
            return False
    
    #parse email id from the link
    def ParseEmail(self,data):
        emailRegex = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}", re.IGNORECASE)
        result = re.search(emailRegex, data)
        if result:
            temp={result.group(0):""}
            AppVariables.email_id.update(temp)
            return True
        else:
            return False
        
    #method for find various combination of first name last name and middle name
    def checkNamesInData(self,AnyData):
        self.initalizedSearchData()
        regrex=""
        if AppVariables.Middle_Name_data != "":
            regrex=AppVariables.data_FL+'|'\
            +AppVariables.data_FML+'|'\
            +AppVariables.data_F_M+'|'\
            +AppVariables.data_M_F+'|'\
            +AppVariables.data_L_M+'|'\
            +AppVariables.data_M_L+'|'\
            +AppVariables.data_F_sM_L+'|'\
            +AppVariables.data_F_M_L_+'|'\
            +AppVariables.data_LF+'|'\
            +AppVariables.data_F_L+'|'\
            +AppVariables.data_L_F+'|'\
            +AppVariables.data_FL_
        else:
            regrex=AppVariables.data_FL+'|'\
            +AppVariables.data_LF+'|'\
            +AppVariables.data_F_L+'|'\
            +AppVariables.data_L_F+'|'\
            +AppVariables.data_FL_
#         print(regrex)
        NameRegex = re.compile(regrex, re.IGNORECASE)
        result = re.search(NameRegex, AnyData)
        if result:
            return True
        else:
            return False
        
    #parse address from the link
    def ParseAddress(self,data):
        addressRegex = re.compile(r'(\d{1,10}( \w+){1,10}( ( \w+){1,10})?( \w+){1,10}[,](( \w+){1,10}(,)? [A-Z]{2}( [0-9]{5})?)?)', re.IGNORECASE)
        result = re.search(addressRegex, data)
        if result:
            temp={result.group(0):""}
            AppVariables.userAddress.update(temp)
            return True
        else:
            return False
        
  
      
    def initalizedSearchData(self):
        AppVariables.data_FL=AppVariables.First_Name_data+" "+AppVariables.Last_Name_data
        if AppVariables.Middle_Name_data !="":
            AppVariables.data_FML=AppVariables.First_Name_data+" "+AppVariables.Middle_Name_data+" "+AppVariables.Last_Name_data
            AppVariables.data_F_M=AppVariables.First_Name_data+"."+AppVariables.Middle_Name_data
            AppVariables.data_M_F=AppVariables.Middle_Name_data+"."+AppVariables.First_Name_data
            AppVariables.data_L_M=AppVariables.Last_Name_data+"."+AppVariables.Middle_Name_data
            AppVariables.data_M_L=AppVariables.Middle_Name_data+"."+AppVariables.Last_Name_data
            S_M=AppVariables.Middle_Name_data[0:1]
            AppVariables.data_F_sM_L=AppVariables.First_Name_data+" "+S_M+" "+AppVariables.Last_Name_data
            AppVariables.data_F_M_L_ = AppVariables.First_Name_data+AppVariables.Middle_Name_data+AppVariables.Last_Name_data              
        
        AppVariables.data_LF=AppVariables.Last_Name_data+" "+AppVariables.First_Name_data
        AppVariables.data_F_L=AppVariables.First_Name_data+"."+AppVariables.Last_Name_data
        AppVariables.data_L_F=AppVariables.Last_Name_data+"."+AppVariables.First_Name_data
        AppVariables.data_FL_ = AppVariables.First_Name_data+AppVariables.Last_Name_data
        
    #method for fetching the pre defined social media id from the google search link 
    def getSocialMediaId(self,dict):
        '''
        Check if header has name first
        Get the url from  high_link and mid_link dictionay
        iterate social meida url on this link to search for social media keyword
        if found use rsplit to grab the information from the link 
        store the information in the seprate dictionary in the form of key:value
        '''
        listLength=len(sps.AppVariables.SocialMediaList)
        count=0
        regrex=""
        for socialTag in sps.AppVariables.SocialMediaList:
            if count==0:
                regrex+=socialTag+'|'+""
            elif count<listLength-1 and count>0:
                regrex+=socialTag+'|'+""
            else:
                regrex+=socialTag
            count+=1
        for key,title in dict.items():
            if self.checkNamesInData(title[0]):
                socialReg=re.compile(regrex,re.IGNORECASE)
                result=re.search(socialReg,title[0])
                if result:
                    tag=result.group(0)
                    getId=key.rsplit('/', 1)
                    temp={key:[tag,getId[1]]}
                    sps.AppVariables.SocialMeidaIdDict.update(temp)
                
                
            
        
        
        
        
        