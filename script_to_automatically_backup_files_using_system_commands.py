#For Reference https://linuxhint.com/schedule_tasks_with_python/

import os
import datetime
while 1:
    #saving current time
    today = datetime.datetime.today()
    today= str(today)
    current_hour = today[11:13]
    current_minute = today[14:16]
    current_sec = today[17:19]

    # making sure code will run at exact '08:00'
    if current_hour == '08' and current_minute == '00' and current_sec == '00':
        # changing directory to documents
        os.chdir('path_to_documents_directory')
        # saving all file names in a list
        files = os.listdir(os.getcwd())
        # creating 'backup' directory if not exist
        if not os.path.exists('backup'):
            os.mkdir('backup')

            for file in files:

                            # ignoring directories
                            if not os.path.isdir(file):
                                # defining a filename without spaces
                                original_name = file
                                file = file.split(" ")
                                file_name = "".join(file)
                                # defining zip_filename	
                                zip_file_name = file_name+".zip"


                # checking if file already exist in backup directory or not
                if not os.path.exists('backup/'+ zip_file_name):
                  # changing file name without spaces
                  os.rename(original_name, file_name)
                  # creating zip file using system command
                  os.system("zip "+ zip_file_name+" "+file_name)
                    #moving zip file in backup directory using system command
                  os.system("mv "+zip_file_name+" backup")
                    # changing filename to its original name
                  os.rename(file_name, original_name)








