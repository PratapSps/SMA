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

#URL link
googleBaseUrl="https://www.google.com/search?q="



    
