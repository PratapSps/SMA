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
# appNotebook = ttk.Notebook(app)
# appNotebook.grid(row=0,column=0,columnspan=50,rowspan=49,sticky='NESW')
notebook = CustomNotebook(width=200, height=200)
notebook.pack(side="top", fill="both", expand=True)
username=''
checktab=0
menubar = Menu(app)
filemenu =Menu(menubar)

    
    
