
from tkinter import *
from tkinter.filedialog import askdirectory
# import tkFileDialog
import os
from os import listdir
from os.path import isfile, join
import glob

class FolderBrowser():
    def findAllJavaFilesInFolder(self,path):
        print("PATH\t\t\t"+path)
        javaFiles = glob.glob(path + '/**/*.java', recursive=True)
        for javafile  in javaFiles:
            print(javafile)
        sys.exit(0)


    def openFolderBrowser(self):
        filename = askdirectory(initialdir="/",title='Please select a directory')
        filename = str(filename)
        self.findAllJavaFilesInFolder(filename)

    def __init__(self,master):
        self.master = master
        master.title("Browse Root of Android  App")
        # SELECT JAVA FOLDER
        self.label = Label(master, text="Privacy  Policy Generator Android for Android App")
        self.label.pack()
        pathlabel = Label(root)
        pathlabel.pack()

        # Open Folder Browser

        b = Button(master, text="SELECT JAVA FOLDER", command=self.openFolderBrowser)
        b.pack()
        


    

root = Tk()

my_gui = FolderBrowser(root)
root.mainloop()

sys.exit(0)