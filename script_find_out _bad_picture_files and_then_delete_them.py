# For reference https://github.com/hastagAB/Awesome-Python-Scripts/blob/master/Clean_up_photo_directory/clean_up_photo.py

import os
from os.path import join
for (dirname, dirs, files) in os.walk('.') :
 for filename in files:
 if filename.endswith('.txt'):
    thefile = os.path.join(dirname,filename)
	size = os.path.getsize(thefile)
	if size == 2578 or size == 2565:
	print 'T-Mobile:',thefile
	#os.remove(thefile) Add this when you are sure to delete the file
	continue
	fhand = open(thefile,'r')
	lines = list()
	for line in fhand:
	lines.append(line)
	fhand.close()
	if len(lines) == 3 and lines[2].startswith('Sent from my iPhone'):
	print 'iPhone:', thefile
	#os.remove(thefile) Add this when you are sure to delete the file
	continue

#Description
#This program is used to find out the "bad" picture files and then eventually delete them.

#Usage
#Run the clean_up_photo.py
