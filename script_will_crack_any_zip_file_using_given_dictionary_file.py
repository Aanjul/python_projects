# For Refrence https://github.com/hastagAB/Awesome-Python-Scripts/blob/master/zip_password_cracker/setup.py




#!/usr/bin/python
#-*- coding: utf-8 -*-

print '''
Free anyZipcrack-dictionary created by:
pyc0d3r: http://www.umarbrowser.co.vu/
'''

#imports
import zipfile
import optparse
from threading import Thread
#Try extract if found password
def extractFile(zFile, password):
 try:
     zFile.extractall(pwd=password)
     print '[+] Found password ' + password + '\n'
 except:
      pass
# main thats gives an interface using optparse
def main():
    parser = optparse.OptionParser("usage %prog "+\
    "-f <zipfile> -d <dictionary>")
parser.add_option('-f', dest='zname', type='string',\
help='specify zip file')
parser.add_option('-d', dest='dname', type='string',\
help='specify dictionary file')
(options, args) = parser.parse_args()
if (options.zname == None ) | (options.dname == None):
    print parser.usage
    exit(0)
else:
    zname = options.zname
    dname = options.dname

zFile = zipfile.ZipFile(zname)
passFile = open(dname)

for line in passFile.readlines():
password = line.strip('\n')
t = Thread(target=extractFile, args=(zFile, password))
t.start

if___name__=='__main__':
main()






#anyZipcrack-dictionary
#This python script will crack any zip file using given dictionary file

#Requipment
#python 3.++ or 2.++

#Usage
#try using the given zip file and dictionary file

#For windows
#$ python zipCrack.py -f evil.zip -d dictionary.txt
#For unix/mac/linux
#$ ./zipCrack.py -f evil.zip -d dictionary.txt
#or that way

#$ python zipCrack.py -f evil.zip -d dictionary.txt
