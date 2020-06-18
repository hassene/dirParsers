import os

for folderName, subfolders, filenames in os.walk(os.getcwd()):
   print("The current folder is "+folderName)
   if '.git' in subfolders:
      subfolders.remove('.git')
   for subfolder in subfolders:
      #folder = str(subfolder)
      #if not folder.startwith('.'):
      print("SUBFOLDER of "+ folderName + ":" + subfolder)

   for filename in filenames:
       print("File Inside" + folderName + ":" + filename)

   print("")

