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
from sps.Animation import Animation
from sps.Animation1 import Animation1
from sps.BackEndProcess import BackEndProcess
import requests
from bs4 import BeautifulSoup
from twisted.words.im.locals import ONLINE
from tkinter.font import BOLD, ITALIC
import tkinter.scrolledtext as tkst

innerFrame=""
class createAppGui:
    global innerFrame
    name=""
    innerFrame=""
    launch_button=""
    #Constructor for initalizing GUI
    def __init__(self):
        icon = PhotoImage(file=appLogo)
        app.tk.call('wm', 'iconphoto', app._w, icon)
        app.wm_title(appTitle)
        app.geometry('1100x620')
        app.maxsize(width=1300, height=700)
        app.wm_state('zoomed')
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
        notebook.add(Home_frame, text=name,image='/images/applogo.png')
        frame=self.createFramedScrollBar(Home_frame,1300,700)
        frame.config(background='white')
        w = Label(frame, image=logo, bg="white", fg="white")
        w.place(x = 400, y = 200)
        w1 = Label(frame, text="SMA", bg="white", fg="black",font=('Tempus Sans ITC', 120, 'bold'))
        w1.place(x = 600, y = 170)
        
        
#create new tab frame with user input.
  
    def createNewTab(self):
        AppVariables.checktab=AppVariables.checktab+1
        filemenu.entryconfig(1, state=DISABLED)
        self.getTabName(app)
        new_frame=Frame(notebook,background='gray')
        new_frame.pack(fill=BOTH, expand=True)
        notebook.add(new_frame,text=AppVariables.username)
        frame=self.createFramedScrollBar(new_frame,1300,700)
        frame.config(background='ivory2')
        self.addElementToFrame(frame)
        
        
    #get the tab name   
    def getTabName(self,parent):
        top = self.top = Toplevel(parent)
        icon = PhotoImage(file=appLogo)
        top.tk.call('wm', 'iconphoto', top._w, icon)
        top.wm_title("Give Search Name")
        top.geometry('300x100')
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
     
     
     #create scrollbar contained frame   
    def createFramedScrollBar(self,container,w,h):
        canvas = Canvas(container,bg='white')
        xscroll = Scrollbar(container, command=canvas.xview,orient = HORIZONTAL)
        yscroll = Scrollbar(container, command=canvas.yview,orient = VERTICAL)
        canvas.config(xscrollcommand=xscroll.set)
        canvas.config(yscrollcommand=yscroll.set,)
        canvas.configure(scrollregion=(0,0,1200,600))
        xscroll.pack(side=BOTTOM, fill=X,expand = FALSE)
        yscroll.pack(side=RIGHT, fill=Y,expand = FALSE)
        canvas.pack(side=LEFT, fill=BOTH, expand=YES)
        frame = Frame(canvas)
        canvas.create_window(0,0, anchor =NW, window = frame, width = w,height=h)
        return frame
    
    
    #create method for adding widget to new frame
    
    def addElementToFrame(self,frame):
        innerFrame = Frame(frame,height=550, width=1000,bd=1,background= 'gray99',relief=GROOVE)
        innerFrame.place(x = 140, y = 70)
        FirstName=Label(innerFrame,text='First Name*',bg='gray99',font=("Helvetica", 16),fg='steel blue')
        FirstName.place(x=100,y=40)
        self.FirstName_Entry=Entry(innerFrame,font=("Helvetica", 16,),fg='firebrick4',relief=GROOVE,takefocus='TAB')
        self.FirstName_Entry.place(x=60,y=90,width=200)
        MiddleName=Label(innerFrame,text='Middle Name',bg='gray99',font=("Helvetica", 16),fg='steel blue')
        MiddleName.place(x=400,y=40,)
        self.MiddleName_Entry=Entry(innerFrame,font=("Helvetica", 16,),fg='firebrick4',relief=GROOVE,takefocus='TAB')
        self.MiddleName_Entry.place(x=360,y=90,width=200)
        LastName=Label(innerFrame,text='Last Name*',bg='gray99',font=("Helvetica", 16),fg='steel blue')
        LastName.place(x=750,y=40)
        self.LastName_Entry=Entry(innerFrame,font=("Helvetica", 16,),fg='firebrick4',relief=GROOVE,takefocus='TAB')
        self.LastName_Entry.place(x=710,y=90,width=200)
        Country=Label(innerFrame,text='Country',bg='gray99',font=("Helvetica", 16),fg='steel blue')
        Country.place(x=100,y=180)
        self.Country_Entry=Entry(innerFrame,font=("Helvetica", 16,),fg='firebrick4',relief=GROOVE,takefocus='TAB')
        self.Country_Entry.place(x=60,y=230,width=200)
        City=Label(innerFrame,text='City',bg='gray99',font=("Helvetica", 16),fg='steel blue')
        City.place(x=400,y=180)
        self.City_Entry=Entry(innerFrame,font=("Helvetica", 16,),fg='firebrick4',relief=GROOVE,takefocus='TAB')
        self.City_Entry.place(x=360,y=230,width=200)
        State=Label(innerFrame,text='State',bg='gray99',font=("Helvetica", 16),fg='steel blue')
        State.place(x=750,y=180)
        self.State_Entry=Entry(innerFrame,font=("Helvetica", 16,),fg='firebrick4',relief=GROOVE,takefocus='TAB')
        self.State_Entry.place(x=710,y=230,width=200)
        Email=Label(innerFrame,text='Email',bg='gray99',font=("Helvetica", 16),fg='steel blue')
        Email.place(x=100,y=320)
        self.Email_Entry=Entry(innerFrame,font=("Helvetica", 16,),fg='firebrick4',relief=GROOVE,takefocus='TAB')
        self.Email_Entry.place(x=60,y=370,width=200)
        Phone=Label(innerFrame,text='Phone',bg='gray99',font=("Helvetica", 16),fg='steel blue')
        Phone.place(x=400,y=320)
        self.Phone_Entry=Entry(innerFrame,font=("Helvetica", 16,),fg='firebrick4',relief=GROOVE,takefocus='TAB')
        self.Phone_Entry.place(x=360,y=370,width=200)
        School_Name=Label(innerFrame,text='School Name',bg='gray99',font=("Helvetica", 16),fg='steel blue')
        School_Name.place(x=750,y=320)
        self.SchoolName_Entry=Entry(innerFrame,font=("Helvetica", 16),fg='firebrick4',relief=GROOVE,takefocus='TAB')
        self.SchoolName_Entry.place(x=710,y=370,width=200)
        self.launch_button=Button(innerFrame,image=AppVariables.button,bg='gray99',bd = 0,height=48,width=150,command=self.initalizeDataInput)
        self.launch_button.place(x=740,y=450)
        
        
        
    #fetch data from form
    def initalizeDataInput(self,*args):
        sps.AppVariables.launch_status=0
        self.disableButton()
        sps.AppVariables.First_Name_data=self.FirstName_Entry.get()
        sps.AppVariables.Middle_Name_data=self.MiddleName_Entry.get()
        sps.AppVariables.Last_Name_data=self.LastName_Entry.get()
        sps.AppVariables.Country_data=self.Country_Entry.get()
        sps.AppVariables.City_data=self.City_Entry.get()
        sps.AppVariables.State_data=self.State_Entry.get()
        sps.AppVariables.Email_data=self.Email_Entry.get()
        sps.AppVariables.Phone_data=self.Phone_Entry.get()
        sps.AppVariables.School_Name_data=self.SchoolName_Entry.get()
#         print(sps.AppVariables.First_Name_data)
        Animation(self,innerFrame,500,210)
        Animation1(self,innerFrame,150,550) # show loading gif
        BackEndProcess().clearAllList()
        self.enableButton()
        self.presentationLayer(app)
    
    #disable form button   
    def disableButton(self):
        self.launch_button.config(state='disabled')
        
        
    #enable form button  
    def enableButton(self):
        self.launch_button.config(state='normal')
        sps.AppVariables.launch_status=1
        
    
                
    def presentationLayer(self,parent):
        top = self.top = Toplevel(parent)
        icon = PhotoImage(file=appLogo)
        top.tk.call('wm', 'iconphoto', top._w, icon)
        top.wm_title(sps.AppVariables.First_Name_data.upper()+" - "+"Cyber Presence")
        top.geometry('1100x620')
#         top.maxsize(width=1300, height=700)
        top.wm_state('zoomed')
        new_frame=Frame(top,background='gray')
        new_frame.pack(fill=BOTH, expand=True)
        canvas = Canvas(new_frame,bg='white')
        xscroll = Scrollbar(new_frame, command=canvas.xview,orient = HORIZONTAL)
        yscroll = Scrollbar(new_frame, command=canvas.yview,orient = VERTICAL)
        canvas.config(xscrollcommand=xscroll.set)
        canvas.config(yscrollcommand=yscroll.set,)
#         canvas.configure(scrollregion=(0,0,1200,600))
        xscroll.pack(side=BOTTOM, fill=X,expand = FALSE)
        yscroll.pack(side=RIGHT, fill=Y,expand = FALSE)
        canvas.pack(side=LEFT, fill=BOTH, expand=YES)
        frame = Frame(canvas)
        frame.pack(fill=BOTH)
        canvas.create_window(0,0, anchor =NW, window = frame,height=1200,width=1200)
        frame.config(background='ivory2')
        self.PresentationLayerElementData(frame)
        top.update()
        canvas.config(scrollregion=canvas.bbox("all"))
        
        
        
    
    def PresentationLayerElementData(self,parentFrame):
        innerFrame_present=Frame(parentFrame,height=1000, width=800,bd=1,background= 'gray99')
        innerFrame_present.configure(highlightbackground="Medium Aquamarine", highlightcolor="Maroon", highlightthickness=2,bd=0)
        innerFrame_present.place(x = 230, y = 140)
        personalDetails_l=Label(innerFrame_present,text="Personal Details:",bg='gray99',font=("Helvetica", 16, UNDERLINE,BOLD),fg='steel blue')
        personalDetails_l.place(x=4,y=10)
        
        #first name data presentation
        FirstName_l=Label(innerFrame_present,text="First Name",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        FirstName_l.place(x=10,y=45)
        FirstName_P_E=Entry(innerFrame_present,bg='gray99',bd=0,disabledbackground='gray99',font=("Times", 14,BOLD),fg='Cadet Blue')
        FirstName_P_E.insert(END,sps.AppVariables.First_Name_data.upper())
        FirstName_P_E.configure(state=DISABLED)
        FirstName_P_E.place(x=10,y=70)
        
        #Middle name data presentation
        MiddleName_l=Label(innerFrame_present,text="Middle Name",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        MiddleName_l.place(x=290,y=45)
        MiddleName_P_E=Entry(innerFrame_present,bg='gray99',bd=0,disabledbackground='gray99',font=("Times", 14,BOLD),fg='Cadet Blue')
        if sps.AppVariables.Middle_Name_data !="":
            MiddleName_P_E.insert(END,sps.AppVariables.Middle_Name_data.upper())
        else:
            MiddleName_P_E.insert(END,"N/A")
        
        MiddleName_P_E.configure(state=DISABLED)
        MiddleName_P_E.place(x=290,y=70)

        #Last Name data presentation
        LastName_l=Label(innerFrame_present,text="Last Name",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        LastName_l.place(x=580,y=45)
        LastName_P_E=Entry(innerFrame_present,bg='gray99',bd=0,disabledbackground='gray99',font=("Times", 14,BOLD),fg='Cadet Blue')
        if sps.AppVariables.Last_Name_data!="":
            LastName_P_E.insert(END,sps.AppVariables.Last_Name_data.upper())
        else:
            LastName_P_E.insert(END,"N/A")
        LastName_P_E.configure(state=DISABLED)
        LastName_P_E.place(x=580,y=70)
        
        
        #Phone Number presentation
        phoneData=""
        phone_counter=1
        for data,value in sps.AppVariables.phone_numbers.items():
            if data!="" and phone_counter<len(sps.AppVariables.phone_numbers):
                phoneData=phoneData+"-  "+data+'\n'
            elif phone_counter == len(sps.AppVariables.phone_numbers):
                phoneData=phoneData+"-  "+data
            phone_counter+=1
                
                
        if len(sps.AppVariables.phone_numbers)==0:
            phoneData="N/A"
        print (phoneData)
        if phoneData !="N/A":
            phone_p_l=Label(innerFrame_present,text="Phone Numbers*",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Indian Red')
        else:
            phone_p_l=Label(innerFrame_present,text="Phone Numbers",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        phone_p_l.place(x=10,y=125)
        
        edit_phone = tkst.ScrolledText(
        master = innerFrame_present,
        wrap   = 'word',  # wrap text at full words only
        width  = 15,      # characters
        height = 5,      # text lines
        bg='gray99',
        fg='Dark Slate Gray',    # background color of edit area
        font=("Times", 12)
        )
        edit_phone.place(x=10,y=160)
        edit_phone.insert('insert', phoneData)
        edit_phone.configure(state=DISABLED)
        
    
        #Email Presentation
        
        
        
        #Address Presentation
        
        #Social Media Link Presentation
        
        #Link criticality
        
        #online random data
        
        #Image Presentation
        
        #top Image leaking websites
        
        
        
        
        
        
        
        
        
        

        
    
    
