
from tkinter import *
from tkinter.filedialog import askdirectory
# import tkFileDialog
import os
from os import listdir
from os.path import isfile, join
import glob
from FileScanner import FileScanner
class FolderBrowser():
    def findAllJavaFilesInFolder(self,path):
        javaFiles = glob.glob(path + '/**/*.java', recursive=True)
        self.javaFiles = javaFiles
        fileScanner =  FileScanner(self.javaFiles)
        self.master.withdraw()






    def openFolderBrowser(self):
        filename = askdirectory(initialdir="/",title='Please select a directory')
        filename = str(filename)
        self.findAllJavaFilesInFolder(filename)

    def __init__(self,master):
        self.javaFiles =  []
        self.master = master
        master.title("Browse Root of Android  App")



        self.label = Label(master, text="Privacy  Policy Generator Android for Android App")
        self.label.pack()
        pathlabel = Label(root)
        pathlabel.pack()


        b = Button(master, text="SELECT JAVA FOLDER", command=self.openFolderBrowser)
        b.pack()
            

    def getJavaPathList(self):
        return self.javaFiles


root = Tk()

my_gui = FolderBrowser(root)
root.mainloop()

sys.exit(0)