
import os
class FileScanner():

    temporary_paths = []
    java_file_paths = []
    path =  ""

    def __init__(self):
        self.path = "ASNIM";


    def  toString(self,basePath):
        print("FILE SCANNER OBJECT")
        print("*******************")
        print("PATH = " + self.path)
        
        
        

fileScanner = FileScanner()
fileScanner.toString()