import zipfile, os
def backup(folder)
  folder = os.path.abspath(folder)
  offset=1
  while True:
      zip_name=os.path.basename(folder)+'_'+str(offset)+'.zip'
      if not os.path.exists(zip_name):
          break
          offset+=1
          print("Successfully created file " %s" %(zip_name))
          backupzip=zipfile.ZipFile(zip_name, 'w')
          for foldername,subfolders,filenames in os.walk(folder):
              backupzip.write(foldername)
          backupzip.close()
          print("done")