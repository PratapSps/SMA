'''
Created on Jun 3, 2017

@author: Survya Pratap Singh
'''
from tkinter import *
from _ctypes import alignment
from sps.AppVariables import *
from tkinter import font
from sps.CustomNotebook import *
import ttk
import numbers
from sps import AppVariables
from faulthandler import disable


class createAppGui:
    name=""
    #Constructor for initalizing GUI
    def __init__(self):
        icon = PhotoImage(file=appLogo)
        app.tk.call('wm', 'iconphoto', app._w, icon)
        app.wm_title(appTitle)
        app.geometry('500x500')
        
        rows=0
        while rows<50:
            app.rowconfigure(rows, weight=1)
            app.columnconfigure(rows, weight=1)
            rows+=1
            
        app.configure(background='white')
     
     #Method for creating menubar   
    def createMenuBar(self):
        filemenu.add_command(label="New",command=self.createNewTab)
        filemenu.add_command(label="Open", command='')
        filemenu.add_command(label="Save", command='')
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=app.quit)
        #filemenu.entryconfig(1, state=DISABLED)
        menubar.add_cascade(label="File", menu=filemenu)
        app.config(menu=menubar)
    
        
    def createHomeTab(self,name):
        Home_frame = Frame(notebook,background='white')
        w = Label(Home_frame, image=logo, bg="white", fg="white")
        w.place(x = 200, y = 100)
        w1 = Label(Home_frame, text="SMA", bg="white", fg="black",font=('Tempus Sans ITC', 120, 'bold'))
        w1.place(x = 400, y = 90)
        notebook.add(Home_frame, text=name)
        
        
#     def createHomeTab(self):
#         homeframe = Frame(appNotebook,background='white')   # first page, which would get widgets gridded into it
#         appNotebook.add(homeframe, text='Home')
#         w = Label(homeframe, image=logo, bg="white", fg="white")
#         w.place(x = 200, y = 100)
#         w1 = Label(homeframe, text="SMA", bg="white", fg="black",font=('Tempus Sans ITC', 120, 'bold'))
#         w1.place(x = 400, y = 90)
    
    def createNewTab(self):
        self.getTabName(app)
        new_frame=Frame(notebook,background='white')
        notebook.add(new_frame,text=AppVariables.username)
        AppVariables.checktab=1
        filemenu.entryconfig(1, state=DISABLED)
        
        
        
        
    def getTabName(self,parent):
        top = self.top = Toplevel(parent)
        self.myLabel = Label(top, text='Enter name for your Search: ')
        self.myLabel.pack()
        self.myEntryBox = Entry(top)
        self.myEntryBox.pack()
        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()
        app.wait_window(top)
        
    def send(self):
        AppVariables.username=self.myEntryBox.get()
        self.top.destroy()

    
