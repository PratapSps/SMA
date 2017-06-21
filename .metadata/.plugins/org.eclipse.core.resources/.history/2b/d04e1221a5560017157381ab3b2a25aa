from tkinter import *

class TestMenu:
    def __init__(self, master):
        
        self.master = master
        self.menubar = Menu(self.master)

        self.cmdmenu = Menu(self.menubar)
        self.cmdmenu.add_command(label="Undo")
        self.cmdmenu.entryconfig(1, state=DISABLED)

        self.unused = Menu(self.menubar)
        
        self.menubar.add_cascade(label="Button Command", menu=self.cmdmenu)

        self.top = Toplevel(menu=self.menubar, width=500, relief=RAISED,
        borderwidth=2)

def main():
    root = Tk()
    root.withdraw()
    app = TestMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()