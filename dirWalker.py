import os
import csv
"""
Stuff that will be tested:
- Creating Regex Objects:
	>>>import re
- The PyInputPlus Module
	>>>import pyinputplus  as pyip
           import random, time 
- READING AND WRITING FILES
>>>from pathlib import Path
 import os
"""
def parseDirectory(Current_path):
   """
   inputParm: Current_path => path that will parsed
   Description: this function will print all folders, subfolders and filenames found in the current path
                excluding the folders, subfolders and filename which start with a dot.
   To conitune, please tape "q".
   """
   csvFileObj = open('/home/hassene/MyWorkspace/02_Dev/01_Scripts/01_Python/newFolder/dirParsers/parserCVS.csv', 'w', newline='')
   csvWriter = csv.writer(csvFileObj)
   #parser = open('parser.txt','a')
   print(f"the directory which it will be parsed is {Current_path}")
   for folderName, subfolders, filenames in os.walk(Current_path):
      if str(os.path.basename(folderName)).startswith('.'):
         continue
      else:
         #print("the current folder is "+ folderName)
         #parser.write("the current folderis " + folderName+ '\n')
         csvWriter.writerow(str(folderName))
         for subfolder in subfolders:
            if str(subfolder).startswith('.'):
               subfolders.remove(subfolder)
            else:
               #print("SUBFOLDER of "+ folderName + ":" + subfolder)
               #parser.write("SUBOLDER of "+ folderName+":"+ subfolder+ '\n')
               csvWriter.writerow(str(subfolder))
         for filename in filenames:
            if str(filename).startswith('.'):
               filenames.remove(filename)
            else: 
               #print("File Inside" + folderName + ":" + filename)
               #parser.write("File Inside "+ folderName+":"+ filename+ '\n')
               csvWriter.writerow(str(filename))
     # print("===================================================================")
     # parser.write("==========================================================================")
   #parser.close()
   csvFileObj.close()

def csvWriter():
   with open('/home/hassene/MyWorkspace/02_Dev/01_Scripts/01_Python/newFolder/dirParsers/parserCVS.csv', 'w', newline='') as csvfile:
      spamwriter = csv.writer(csvfile)
      spamwriter.writerow([1, 2, 3.141592, 4])

def main():
   current_path = os.getcwd()
   print(help(parseDirectory))
   parseDirectory(current_path)
 #  csvWriter()

if __name__ == "__main__":
   main()
