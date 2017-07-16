'''
Created on Jun 3, 2017

@author: Survya Pratap Singh
'''
from tkinter import *
from sps.CustomNotebook import *

app=Tk()

appLogo='images/applogo.png'
appTitle='SMA'
logo = PhotoImage(file=appLogo)
button=PhotoImage(file='Images/button.png')
saveButton=PhotoImage(file='Images/save1.png')
closeButton=PhotoImage(file='Images/close.png')
bar_1=PhotoImage(file='Images/bar_1.PNG')
bar_2=PhotoImage(file='Images/bar_2.PNG')
bar_3=PhotoImage(file='Images/bar_3.PNG')
bar_4=PhotoImage(file='Images/bar_4.PNG')
bar_5=PhotoImage(file='Images/bar_5.PNG')
# appNotebook = ttk.Notebook(app)
# appNotebook.grid(row=0,column=0,columnspan=50,rowspan=49,sticky='NESW')
notebook = CustomNotebook(width=200, height=200)
notebook.pack(side="top", fill="both", expand=True)
username=''
checktab=0
menubar = Menu(app)
filemenu =Menu(menubar)

#Data from the user input
First_Name_data=""
Middle_Name_data=""
Last_Name_data=""
Country_data=""
City_data=""
State_data=""
Email_data=""
Phone_data=""
School_Name_data=""
launch_status=0


#Gui Form variables
FirstLast=""
FirstMiddleLast=""
FirstLastCoun=""
FirstLastState=""
FirstLastCity=""
FirstLastSchool=""
FirstMLastCoun=""
FirstMLastState=""
FirstMLastCity=""
FirstMLastSchool=""
UserEmailID=""


#URL link
googleBaseUrl="https://www.google.com/search?q="
googleBaseUrl_1='&nfpr=1'
googleImgUrl_1="https://www.google.co.in/search?q="
googleImgUrl_2="&source=lnms&tbm=isch&nfpr=1"


mid_Link_dict={} #dictionary for storing linked searched by google
low_Link_dict={} #dictionary for storing linked searched by google
high_Link_dict={}

#store found phone, email and address information in the list
phone_numbers={}
email_id={}
userAddress={}

#Data to search for social media websites
SocialMediaList=["GitHub","LinkedIn","Facebook","Twitter","Instagram photos and videos","Pinterest","Vizualize.me","Google+"]
SocialMeidaIdDict={}

#Variables for looking into googlesearched link
#Name with space
data_FL=""
data_FML=""
data_LF=""

#name with .
data_F_L=""
data_L_F=""
data_F_M=""
data_M_F=""
data_L_M=""
data_M_L=""

#no space
data_FL_=""
data_F_M_L_=""

#single characther of middle name
data_F_sM_L=""


#image dictionay  for storing unique images
image_dict={}
image_bs64Image={}



    
