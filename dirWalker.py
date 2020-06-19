import os
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
   parser = open('parser.txt','a')
   print(f"the directory which it will be parsed is {Current_path}")
   for folderName, subfolders, filenames in os.walk(Current_path):
      if str(os.path.basename(folderName)).startswith('.'):
         continue
      else:
         #print("the current folder is "+ folderName)
         parser.write("the current folderis " + folderName+ '\n')
         for subfolder in subfolders:
            if str(subfolder).startswith('.'):
               subfolders.remove(subfolder)
            else:
               #print("SUBFOLDER of "+ folderName + ":" + subfolder)
               parser.write("SUBOLDER of "+ folderName+":"+ subfolder+ '\n')
         for filename in filenames:
            if str(filename).startswith('.'):
               filenames.remove(filename)
            else: 
               #print("File Inside" + folderName + ":" + filename)
               parser.write("File Inside "+ folderName+":"+ filename+ '\n')
     # print("===================================================================")
      parser.write("==========================================================================")
   parser.close()
def main():
   current_path = os.getcwd()
   print(help(parseDirectory))
   parseDirectory(current_path)

if __name__ == "__main__":
   main()
