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

mid_Link_dict={} #dictionary for storing linked searched by google
low_Link_dict={} #dictionary for storing linked searched by google
high_Link_dict={}

#store found phone, email and address information in the list
phone_numbers={}
email_id={}
userAddress={}

#Data to search for social media websites
SocialMediaList=["GitHub","LinkedIn","Facebook","Twitter","Instagram photos and videos","Pinterest"]

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







    
