 # For refrence https://github.com/Logan1x/Python-Scripts/blob/master/bin/youtube-bot-linux.py
 
 # For refrence https://github.com/Logan1x/Python-Scripts
 
 # Step to run - This is a simple python script that increases your video count/ views. Log out from all google accounts and run this.

# For Linux Users
#python youtube-bot-linux.py

# For Windows Users
# python youtube-bot-windows.py
 
 import time
 import webbrowser
 import os
 
 url = str(input("Enter your video url in ->\"url here \"<- : "))
 n = input("Enter refresh rate(seconds) : ")
 brow = input("Enter your default browser in ->\"browser here \"<-  : ")
 while (1):
	os.system(" killall -9 " + brow)
	time.sleep(int(n))
	webbrowser.open(url)
	print('Successfully Viewd')