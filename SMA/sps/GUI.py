'''
Created on Jun 3, 2017

@author: Survya Pratap Singh
'''
from tkinter import *
from _ctypes import alignment
from sps.AppVariables import *
from tkinter import font
from sps.CustomNotebook import *
from tkinter import ttk
import numbers
from sps import AppVariables



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
    
#create home tab frame        
    def createHomeTab(self,name):
        Home_frame = Frame(notebook,background='white')
        Home_frame.pack(fill=BOTH, expand=True)
        notebook.add(Home_frame, text=name)
        frame=self.createFramedScrollBar(Home_frame)
        w = Label(frame, image=logo, bg="white", fg="white")
        w.place(x = 500, y = 240)
        w1 = Label(frame, text="SMA", bg="white", fg="black",font=('Tempus Sans ITC', 120, 'bold'))
        w1.place(x = 700, y = 200)
        
        
        
#create new tab frame with user input
  
    def createNewTab(self):
        self.getTabName(app)
        new_frame=Frame(notebook,background='white')
        new_frame.pack(fill=BOTH, expand=True)
        notebook.add(new_frame,text=AppVariables.username)
        AppVariables.checktab=1
        filemenu.entryconfig(1, state=DISABLED)
        frame=self.createFramedScrollBar(new_frame)
        
        
        
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
        
    def createFramedScrollBar(self,container):
        canvas = Canvas(container,bg='white')
        xscroll = Scrollbar(container, command=canvas.xview,orient = HORIZONTAL)
        yscroll = Scrollbar(container, command=canvas.yview,orient = VERTICAL)
        canvas.config(xscrollcommand=xscroll.set)
        canvas.config(yscrollcommand=yscroll.set,)
        canvas.configure(scrollregion=(0,0,1000,900))
        xscroll.pack(side=BOTTOM, fill=X,expand = FALSE)
        yscroll.pack(side=RIGHT, fill=Y,expand = FALSE)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        frame = Frame(canvas, background='white',)
        canvas.create_window(0,0, anchor =NW, window = frame, width = 2000, height = 1000)
        return frame
                


        
    
    
