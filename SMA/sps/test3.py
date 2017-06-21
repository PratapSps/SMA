'''
Created on Jun 21, 2017

@author: u130796
'''
    
from tkinter import *
from tkinter import ttk

master=Tk()

frame = Frame(master, bd=2, relief=SUNKEN)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=E+W)

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)

text = Text(frame, wrap=NONE, bd=0,
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)

text.grid(row=0, column=0, sticky=N+S+E+W)

xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)

frame.pack()
root.mainloop()