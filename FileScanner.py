
import os
import re
class FileScanner():

    def printFileContents(self,path):
        java_file = open(path,'r')
        line = java_file.readline()
        while line!='':
            print(line)
            line = java_file.readline()

        java_file.close()
    

    def __init__(self,java_file_paths):

        for each_java_path in  java_file_paths:
        	
            self.printFileContents(each_java_path)

    def  toString(self,basePath):
        print("FILE SCANNER OBJECT")
        print("*******************")
        print("PATH = " + self.path)



