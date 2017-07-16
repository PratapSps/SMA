from io import BytesIO
import urllib
import urllib.request
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
url = "https://media.licdn.com/mpr/mpr/shrink_100_100/p/3/000/267/0fa/2d74f5d.jpg"
req = urllib.request.Request(url)
#header={'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')
data=urllib.request.urlopen(req)
raw_data = data.read()
image = Image.open(BytesIO(raw_data))

image = image.resize((100,100), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(image)

label = Label(image=image1)
label.pack()
root.mainloop()