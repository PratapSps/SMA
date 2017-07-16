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
from PIL import Image, ImageTk
import urllib
from io import BytesIO



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
        canvas.config(yscrollcommand=yscroll.set)
#         canvas.configure(scrollregion=(0,0,1200,600))
        xscroll.pack(side=BOTTOM, fill=X,expand = FALSE)
        yscroll.pack(side=RIGHT, fill=Y,expand = FALSE)
        canvas.pack(side=LEFT, fill=BOTH, expand=YES)
        frame = Frame(canvas)
        frame.pack(fill=BOTH)
        canvas.create_window(0,0, anchor =NW, window = frame,height=3000,width=1200)
        frame.config(background='ivory2')
        self.PresentationLayerElementData(frame,top)
        top.update()
        canvas.config(scrollregion=canvas.bbox("all"))
        
        
        
    
    def PresentationLayerElementData(self,parentFrame,top):
        innerFrame_present=Frame(parentFrame,height=2800, width=800,bd=1,background= 'gray99')
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
                phoneData=phoneData+data+'\n'
            elif phone_counter == len(sps.AppVariables.phone_numbers):
                phoneData=phoneData+data
            phone_counter+=1
                
                
        if len(sps.AppVariables.phone_numbers)==0:
            phoneData="N/A"
        
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
        font=("Times", 12,BOLD)
        )
        if phoneData !="N/A":
            edit_phone.configure(fg='Dark Slate Blue')
        edit_phone.configure(highlightbackground="White Smoke", highlightthickness=2,bd=0)
        edit_phone.place(x=10,y=160)
        edit_phone.insert('insert', phoneData)
        edit_phone.configure(state=DISABLED)
        phone_dataCount=len(sps.AppVariables.phone_numbers)
        if phone_dataCount > 0:
            totalCount_p="Count: "+str(phone_dataCount)
            p_count_l=Label(innerFrame_present,text=totalCount_p,bg='gray99',font=("Courier", 11),fg='Medium Orchid')
            p_count_l.place(x=10,y=265)
        
    
        #Email Presentation
        emailData=""
        email_counter=1
        for data,value in sps.AppVariables.email_id.items():
            if data!="" and email_counter<len(sps.AppVariables.email_id):
                emailData=emailData+data+'\n'
            elif email_counter == len(sps.AppVariables.email_id):
                emailData=emailData+data
            email_counter+=1
                
                
        if len(sps.AppVariables.email_id)==0:
            emailData="N/A"
        
        if emailData !="N/A":
            email_p_l=Label(innerFrame_present,text="Email ID's*",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Indian Red')
        else:
            email_p_l=Label(innerFrame_present,text="Email ID's",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        email_p_l.place(x=290,y=125)
        
        edit_email = tkst.ScrolledText(
        master = innerFrame_present,
        wrap   = 'word',  # wrap text at full words only
        width  = 22,      # characters
        height = 5,      # text lines
        bg='gray99',
        fg='Dark Slate Gray',    # background color of edit area
        font=("Times", 12,BOLD)
        )
        if emailData !="N/A":
            edit_email.configure(fg='Dark Slate Blue')
        edit_email.configure(highlightbackground="White Smoke", highlightthickness=2,bd=0)
        edit_email.place(x=290,y=160)
        edit_email.insert('insert', emailData)
        edit_email.configure(state=DISABLED)
        email_dataCount=len(sps.AppVariables.email_id)
        if email_dataCount > 0:
            totalCount_e="Count: "+str(email_dataCount)
            e_count_l=Label(innerFrame_present,text=totalCount_e,bg='gray99',font=("Courier", 11),fg='Medium Orchid')
            e_count_l.place(x=290,y=265)
        
        
        #Social Media Link Presentation
        SMData=""
        SM_counter=1
        for data,value in sps.AppVariables.SocialMeidaIdDict.items():
            if  SM_counter<len(sps.AppVariables.SocialMeidaIdDict):
                type=value[0]+" : "+value[1]
                SMData=SMData+type+'\n'
            if SM_counter == len(sps.AppVariables.SocialMeidaIdDict):
                type=value[0]+" : "+value[1]
                SMData=SMData+type
            SM_counter+=1
                 
                 
        if len(sps.AppVariables.SocialMeidaIdDict)==0:
            SMData="N/A"
        
        if SMData !="N/A":
            SM_p_l=Label(innerFrame_present,text="Social Media ID's*",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Indian Red')
        else:
            SM_p_l=Label(innerFrame_present,text="Email ID's",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        SM_p_l.place(x=580,y=125)
         
        edit_SM = tkst.ScrolledText(
        master = innerFrame_present,
        wrap   = 'word',  # wrap text at full words only
        width  = 22,      # characters
        height = 5,      # text lines
        bg='gray99',
        fg='Dark Slate Gray',    # background color of edit area
        font=("Times", 12,BOLD)
        )
        edit_SM.configure(highlightbackground="White Smoke", highlightthickness=2,bd=0)
        if SMData !="N/A":
            edit_SM.configure(fg='Dark Slate Blue')
        edit_SM.place(x=580,y=160)
        edit_SM.insert('insert', SMData)
        edit_SM.configure(state=DISABLED)
        SM_dataCount=len(sps.AppVariables.SocialMeidaIdDict)
        if SM_dataCount > 0:
            totalCount_SM="Count: "+str(SM_dataCount)
            SM_count_l=Label(innerFrame_present,text=totalCount_SM,bg='gray99',font=("Courier", 11),fg='Medium Orchid')
            SM_count_l.place(x=580,y=265)
        
        
        #Address Presentation
        
        AddData=""
        Add_counter=1
        for data,value in sps.AppVariables.userAddress.items():
            if data!="" and Add_counter<len(sps.AppVariables.userAddress):
                AddData=AddData+data+'\n'
            elif Add_counter == len(sps.AppVariables.userAddress):
                AddData=AddData+data
            Add_counter+=1
                
                
        if len(sps.AppVariables.userAddress)==0:
            AddData="N/A"
        
        if AddData !="N/A":
            Add_p_l=Label(innerFrame_present,text="Address*",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Indian Red')
        else:
            Add_p_l=Label(innerFrame_present,text="Address",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        Add_p_l.place(x=10,y=320)
        
        edit_Add = tkst.ScrolledText(
        master = innerFrame_present,
        wrap   = 'word',  # wrap text at full words only
        width  = 40,      # characters
        height = 5,      # text lines
        bg='gray99',
        fg='Dark Slate Gray',    # background color of edit area
        font=("Times", 12,BOLD)
        )
        if AddData !="N/A":
            edit_Add.configure(fg='Dark Slate Blue')
        edit_Add.configure(highlightbackground="White Smoke", highlightthickness=2,bd=0)
        edit_Add.place(x=10,y=355)
        edit_Add.insert('insert', AddData)
        edit_Add.configure(state=DISABLED)
        Add_dataCount=len(sps.AppVariables.userAddress)
        if Add_dataCount > 0:
            totalCount_e="Count: "+str(Add_dataCount)
            add_count_l=Label(innerFrame_present,text=totalCount_e,bg='gray99',font=("Courier", 11),fg='Medium Orchid')
            add_count_l.place(x=10,y=460)
        
        
        Online_Content_l=Label(innerFrame_present,text="Online-Content:",bg='gray99',font=("Helvetica", 16, UNDERLINE,BOLD),fg='steel blue')
        Online_Content_l.place(x=4,y=500)
        
        #Link criticality
        Link_Criticality_l=Label(innerFrame_present,text="Link Severity",bg='gray99',font=("Helvetica", 14,BOLD),fg='Light Steel Blue')
        Link_Criticality_l.place(x=335,y=540)
        
        Link_Data=""
        
        #High Critical Link
        HL_Data=""
        HL_counter=1
        for data,value in sps.AppVariables.high_Link_dict.items():
            if  HL_counter<len(sps.AppVariables.high_Link_dict):
                HL_Data=HL_Data+data+'\n'
                Link_Data=Link_Data+"- "+value[0]+": "+value[1]+'\n'
            if HL_counter == len(sps.AppVariables.high_Link_dict):
                HL_Data=HL_Data+data
                Link_Data=Link_Data+"- "+value[0]+": "+value[1]+'\n'
            HL_counter+=1
                 
                 
        if len(sps.AppVariables.high_Link_dict)==0:
            HL_Data="N/A"
        
        if HL_Data !="N/A":
            HL_p_l=Label(innerFrame_present,text="High Severity*",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Indian Red')
        else:
            HL_p_l=Label(innerFrame_present,text="High Severity",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        HL_p_l.place(x=10,y=580)
         
        edit_HL = tkst.ScrolledText(
        master = innerFrame_present,
        wrap   = 'word',  # wrap text at full words only
        width  = 80,      # characters
        height = 6,      # text lines
        bg='gray99',
        fg='Dark Slate Gray',    # background color of edit area
        font=("Times", 12,BOLD)
        )
        edit_HL.configure(highlightbackground="White Smoke", highlightthickness=2,bd=0)
        if HL_Data !="N/A":
            edit_HL.configure(fg='Dark Slate Blue')
        edit_HL.place(x=10,y=610)
        edit_HL.insert('insert', HL_Data)
        edit_HL.configure(state=DISABLED)
        HL_dataCount=len(sps.AppVariables.high_Link_dict)
        if HL_dataCount > 0:
            totalCount_HL=" - Count: "+str(HL_dataCount)
            HL_count_l=Label(innerFrame_present,text=totalCount_HL,bg='gray99',font=("Courier", 11),fg='Medium Orchid')
            HL_count_l.place(x=130,y=580)
        
        
        
        
        #mid link
        
        ML_Data=""
        ML_counter=1
        for data,value in sps.AppVariables.mid_Link_dict.items():
            if  ML_counter<len(sps.AppVariables.mid_Link_dict):
                ML_Data=ML_Data+data+'\n'
                Link_Data=Link_Data+"- "+value[0]+": "+value[1]+'\n'
            if ML_counter == len(sps.AppVariables.mid_Link_dict):
                ML_Data=ML_Data+data
                Link_Data=Link_Data+"- "+value[0]+": "+value[1]
            ML_counter+=1
                 
                 
        if len(sps.AppVariables.mid_Link_dict)==0:
            ML_Data="N/A"
        
        if ML_Data !="N/A":
            ML_p_l=Label(innerFrame_present,text="Medium Severity*",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Indian Red')
        else:
            ML_p_l=Label(innerFrame_present,text="Medium Severity",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        ML_p_l.place(x=10,y=760)
         
        edit_ML = tkst.ScrolledText(
        master = innerFrame_present,
        wrap   = 'word',  # wrap text at full words only
        width  = 80,      # characters
        height = 6,      # text lines
        bg='gray99',
        fg='Dark Slate Gray',    # background color of edit area
        font=("Times", 12,BOLD)
        )
        edit_ML.configure(highlightbackground="White Smoke", highlightthickness=2,bd=0)
        if ML_Data !="N/A":
            edit_ML.configure(fg='Dark Slate Blue')
        edit_ML.place(x=10,y=790)
        edit_ML.insert('insert', ML_Data)
        edit_ML.configure(state=DISABLED)
        ML_dataCount=len(sps.AppVariables.mid_Link_dict)
        if ML_dataCount > 0:
            totalCount_ML=" - Count: "+str(ML_dataCount)
            ML_count_l=Label(innerFrame_present,text=totalCount_ML,bg='gray99',font=("Courier", 11),fg='Medium Orchid')
            ML_count_l.place(x=150,y=760)
        
        
        
        #low link 
        LL_Data=""
        LL_counter=1
        for data,value in sps.AppVariables.low_Link_dict.items():
            if  LL_counter<len(sps.AppVariables.mid_Link_dict):
                LL_Data=LL_Data+data+'\n'
                
            if LL_counter == len(sps.AppVariables.low_Link_dict):
                LL_Data=LL_Data+data
                
            LL_counter+=1
                 
                 
        if len(sps.AppVariables.low_Link_dict)==0:
            LL_Data="N/A"
        
        if LL_Data !="N/A":
            LL_p_l=Label(innerFrame_present,text="Low Severity*",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Indian Red')
        else:
            LL_p_l=Label(innerFrame_present,text="Low Severity",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        LL_p_l.place(x=10,y=940)
         
        edit_LL = tkst.ScrolledText(
        master = innerFrame_present,
        wrap   = 'word',  # wrap text at full words only
        width  = 80,      # characters
        height = 6,      # text lines
        bg='gray99',
        fg='Dark Slate Gray',    # background color of edit area
        font=("Times", 12,BOLD)
        )
        edit_LL.configure(highlightbackground="White Smoke", highlightthickness=2,bd=0)
        if LL_Data !="N/A":
            edit_LL.configure(fg='Dark Slate Blue')
        edit_LL.place(x=10,y=970)
        edit_LL.insert('insert', LL_Data)
        edit_LL.configure(state=DISABLED)
        LL_dataCount=len(sps.AppVariables.low_Link_dict)
        if LL_dataCount > 0:
            totalCount_LL=" - Count: "+str(LL_dataCount)
            LL_count_l=Label(innerFrame_present,text=totalCount_LL,bg='gray99',font=("Courier", 11),fg='Medium Orchid')
            LL_count_l.place(x=120,y=940)   
        
        
        
        
        #online random data
        
        if Link_Data=="":
            Link_Data="N/A"
        
        if Link_Data !="N/A":
            CL_p_l=Label(innerFrame_present,text="Web Content*",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Indian Red')
        else:
            CL_p_l=Label(innerFrame_present,text="Web Content",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        CL_p_l.place(x=10,y=1120)
         
        edit_CL = tkst.ScrolledText(
        master = innerFrame_present,
        wrap   = 'word',  # wrap text at full words only
        width  = 90,      # characters
        height = 15,      # text lines
        bg='gray99',
        fg='Dark Slate Gray',    # background color of edit area
        font=("Times", 12,BOLD)
        )
        edit_CL.configure(highlightbackground="White Smoke", highlightthickness=2,bd=0)
        if Link_Data !="N/A":
            edit_CL.configure(fg='Dark Slate Blue')
        edit_CL.place(x=10,y=1150)
        edit_CL.insert('insert', Link_Data)
        edit_CL.configure(state=DISABLED)

        
        #Image Presentation
        imageDictLen=len(sps.AppVariables.image_bs64Image)
        if imageDictLen >0:
            I_p_l=Label(innerFrame_present,text="Web Images*",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Indian Red')
        else:
            I_p_l=Label(innerFrame_present,text="Web Images",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        I_p_l.place(x=10,y=1500)
        ImageFrame=Frame(innerFrame_present,highlightbackground="White Smoke", highlightthickness=2,bd=0,bg='gray99',height=680,width=750)
        ImageFrame.place(x=10,y=1530)
        img_count=1
        x=30
        y=15
        ImageData_URL=""
        ImageSource={}
        if imageDictLen==0:
            l1=Label(ImageFrame,text="N/A",bg='gray99',font=("Times", 36,ITALIC),fg='Dark Slate Blue')
            l1.place(x=300,y=280)
        for data,value in sps.AppVariables.image_bs64Image.items():
            if img_count<=16:
                L_count=Label(ImageFrame,image=value[1]).place(x=x,y=y)
                x=x+150+30
                if img_count%4==0:
                    y=y+150+15
                    x=30  
#                 top.update()
            if img_count<imageDictLen:
                ImageData_URL=ImageData_URL+data+'\n'
            else:
                ImageData_URL=ImageData_URL+data
            tempdict={value[0]:""}
            ImageSource.update(tempdict)
            img_count+=1
        print(ImageData_URL)
        print(ImageSource)
        
        
        #Images link
        
        if ImageData_URL=="":
            ImageData_URL="N/A"
        
        if ImageData_URL !="N/A":
            ImageL_p_l=Label(innerFrame_present,text="Images URL*",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Indian Red')
        else:
            ImageL_p_l=Label(innerFrame_present,text="Images URL",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        ImageL_p_l.place(x=10,y=2250)
         
        edit_ImageL = tkst.ScrolledText(
        master = innerFrame_present,
        wrap   = 'word',  # wrap text at full words only
        width  = 90,      # characters
        height = 10,      # text lines
        bg='gray99',
        fg='Dark Slate Gray',    # background color of edit area
        font=("Times", 12,BOLD)
        )
        edit_ImageL.configure(highlightbackground="White Smoke", highlightthickness=2,bd=0)
        if ImageData_URL !="N/A":
            edit_ImageL.configure(fg='Dark Slate Blue')
        edit_ImageL.place(x=10,y=2280)
        edit_ImageL.insert('insert', ImageData_URL)
        edit_ImageL.configure(state=DISABLED)
        if imageDictLen > 0:
            totalCount_ImageL=" - Count: "+str(imageDictLen)
            ImageL_count_l=Label(innerFrame_present,text=totalCount_ImageL,bg='gray99',font=("Courier", 11),fg='Medium Orchid')
            ImageL_count_l.place(x=120,y=2250) 
            
            
        #Website Leaking images
        LeakageI_Data=""
        LLL_counter=1
        for data,value in ImageSource.items():
            if  LLL_counter<len(ImageSource):
                LeakageI_Data=LeakageI_Data+data+'\n'
                
            if LLL_counter == len(ImageSource):
                LeakageI_Data=LeakageI_Data+data
                
            LLL_counter+=1
                 
                 
        if len(ImageSource)==0:
            LeakageI_Data="N/A"
        
        if LeakageI_Data !="N/A":
            LLL_p_l=Label(innerFrame_present,text="Websites Leaking Images*",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Indian Red')
        else:
            LLL_p_l=Label(innerFrame_present,text="Websites Leaking Images",bg='gray99',font=("Times", 14,ITALIC,UNDERLINE),fg='Light Steel Blue')
        LLL_p_l.place(x=10,y=2520)
         
        edit_LLL = tkst.ScrolledText(
        master = innerFrame_present,
        wrap   = 'word',  # wrap text at full words only
        width  = 50,      # characters
        height = 5,      # text lines
        bg='gray99',
        fg='Dark Slate Gray',    # background color of edit area
        font=("Times", 12,BOLD)
        )
        edit_LLL.configure(highlightbackground="White Smoke", highlightthickness=2,bd=0)
        if LeakageI_Data !="N/A":
            edit_LLL.configure(fg='Dark Slate Blue')
        edit_LLL.place(x=10,y=2550)
        edit_LLL.insert('insert', LeakageI_Data)
        edit_LLL.configure(state=DISABLED)
        LLL_dataCount=len(ImageSource)
        if LLL_dataCount > 0:
            totalCount_LLL=" - Count: "+str(LLL_dataCount)
            LLL_count_l=Label(innerFrame_present,text=totalCount_LLL,bg='gray99',font=("Courier", 11),fg='Medium Orchid')
            LLL_count_l.place(x=220,y=2520)
        
        #Animation
        
        #Save Button 
        
        #Close button