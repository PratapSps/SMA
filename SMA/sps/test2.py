from tkinter import *
root=Tk()


f1=Frame(root,bg='yellow')
f1.pack(fill=BOTH)
f2=Frame(f1,bg='red')
f2.pack(side=BOTTOM)
canvas=Canvas(f2,height=400,width=900,bg='blue')
yscroll = Scrollbar(f2, command=canvas.yview,orient = VERTICAL)
canvas.config(yscrollcommand=yscroll.set)
canvas.configure(scrollregion=(0,0,0,1200))
yscroll.pack(side=RIGHT, fill=Y,expand = FALSE)
canvas.pack(side=LEFT, fill=BOTH, expand=YES)
frame = Frame(canvas,bg='green')
frame.pack(fill=BOTH)
canvas.create_window(0,0, anchor =NW, window = frame,height=1200,width=900)
root.mainloop()