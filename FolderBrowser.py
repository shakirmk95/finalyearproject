
from tkinter import *
from tkinter.filedialog import askopenfilename
class FolderBrowser():
    def __init__(self,master):
        self.master = master
        master.title("Browse Root of Android  App")
        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()
        pathlabel = Label(root)
        pathlabel.pack()
        filename = askopenfilename()
        pathlabel.config(text=filename)


    def openFolderBrowser(self):
        print("Wait")

root = Tk()

my_gui = FolderBrowser(root)
root.mainloop()