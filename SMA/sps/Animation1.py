'''
Created on Jul 9, 2017

@author: Survya Pratap Singh
Wright State University
UID: U00803205
email: singh.survya@gmail.com
website: https://survya.com
'''
from tkinter import *
import os
from sps.AppVariables import *
from sps import AppVariables


class Animation1:
    gifBackgroundDirectory="gif2/"
    def __init__(self,Frame,innerframe,x_axis,y_axis):
        self.gifBackgroundImages = list()
        self.atualGifBackgroundImage = 0
        self.background = PhotoImage()
        self.label1 = Label(innerframe,bg='gray99')
        self.label1.place(x=x_axis,y=y_axis)
        self.animate()

        
    
    def animate(self):
        #CHECK IF LIST IS EMPTY
        if sps.AppVariables.launch_status==0:
            if len(self.gifBackgroundImages) == 0:
                #CREATE FILES IN LIST
                for foldername in os.listdir(self.gifBackgroundDirectory):
                    self.gifBackgroundImages.append(foldername)
                #ALPHABETICAL ORDER
                self.gifBackgroundImages.sort(key = lambda x: int(x.split('.')[0].split('-')[1]))
            
            if self.atualGifBackgroundImage == len(self.gifBackgroundImages):
                self.atualGifBackgroundImage = 0
            
            self.background["file"] = self.gifBackgroundDirectory + self.gifBackgroundImages[self.atualGifBackgroundImage]
            self.label1["image"] = self.background
            self.atualGifBackgroundImage += 1
                #MILISECONDS\/ PER FRAME
            app.after(100, lambda: self.animate())
        else:
            self.label1.place_forget()
           

    
    
    