#For reference https://linuxhint.com/schedule_tasks_with_python/

import os
import shutil
import datetime
while 1:

    #calculating current hour, minute and second

    today = datetime.datetime.today()
    today = str(today)
    current_hour = today[11:13]
    current_minute = today[14:16]
    current_sec = today[17:19]

    # making sure that system will arange files at 08:00
    if current_hour == '08' and current_minute == '00' and current_sec == '00':

        #changing directory to download
        os.chdir("path_to_Download_directory")
        #saving all files names in a list
        files = os.listdir(os.getcwd())

        for filename in files:
            #ignoring directories
            if not os.path.isdir(filename):

                # selecting mp3 files
                if '.mp3' in filename:
                    #creating 'Audio' directory if not exist
                    if not os.path.exists('Audio'):
                        os.mkdir('Audio')
                        #moving file in 'Audio' directory
                        shutil.move(filename, 'Audio')

                    # selecting mp4 files
                    elif '.mp4' in filename:
                        # creating 'Video' directory if not exist
                        if not os.path.exists('Video'):
                            os.mkdir('Video')
                          # moving file in 'Video' directory
                          shutil.move(filename, 'Video')

                          #selecting pdf files 
                          elif '.pdf' in filename:
                              # creating 'PDF' directory if not exist
                              if not os.path.exists('PDF'):
                                  os.mkdir('PDF')
                                  # moving file in PDF directory
                                  shutil.move(filename, 'PDF')
                         # selecting jpg and png file
                         elif '.jpg' in filename or '.png' in filename :
                                      # creating 'Pictures' directory if not exist
                                      if not os.path.exist('Pictures')
                                      os.mkdir('Pictures')
                                      # moving file in 'Pictures' directory
                                      shutil.move(filename, 'Pictures')

                        # selecting excel files
                        elif '.xls' in filename:
                            # creating 'Excel' directory if not exist
                            if not os.path.exist('Excel'):
                            os.mkdir('Excel')
                            # moving file in 'Excel' directory
                            shutil.move(filename, 'Excel')

                        # selecting '.ppt' files
                        elif '.ppt' in filename:
                            # creating 'Power Point' directory if not exists
                            if not os.path.exist('Power Point')
                               os.mkdir('Power Point')
                               # moving file in 'Power Point' directory
                                 shutil.move(filename, 'Power Point')

                        # selecting '.docs' files
                        elif '.docx' in filename:
                            #creating 'Word File' directory if not exists
                            if not os.path.exists('Word File'):
                                os.mkdir('Word File')
                            # moving file in 'Word File' directory     
                            shutil.move(filename, 'Word File')







