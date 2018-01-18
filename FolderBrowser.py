
from tkinter import *
from tkinter.filedialog import askdirectory
# import tkFileDialog
class FolderBrowser():

    def openFolderBrowser(self):
        filename = askdirectory(initialdir="/",title='Please select a directory')
        # pathlabel.config(text=filename)
        print(str(filename))

    def __init__(self,master):
        self.master = master
        master.title("Browse Root of Android  App")
        # SELECT JAVA FOLDER
        self.label = Label(master, text="Privacy  Policy Generator Android for Android App")
        self.label.pack()
        pathlabel = Label(root)
        pathlabel.pack()

        # Open Folder Browser

        b = Button(master, text="OK", command=self.openFolderBrowser)
        b.pack()
        


    

root = Tk()

my_gui = FolderBrowser(root)
root.mainloop()

sys.exit(0)