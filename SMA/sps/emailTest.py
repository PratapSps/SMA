from io import BytesIO
import urllib
import urllib.request
import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
url = "https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAEAAQAAAAAAAA3IAAAAJDAwNGM0NmY0LWFmMWItNDc2OS04ZTRkLTU2NDRkYjY3MzdhOQ.jpg"
req = urllib.request.Request(url)
header={'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}
with urllib.request.urlopen(url) as u:
    raw_data = u.read()
image = Image.open(BytesIO(raw_data))

image = image.resize((100,100), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(image)

label = tk.Label(image=image1)
label.pack()
root.mainloop()