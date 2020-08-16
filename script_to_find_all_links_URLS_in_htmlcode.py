# For refrence - https://www.pythonforbeginners.com/code-snippets-source-code/regular-expression-re-findall/



#In this script, we are going to use the re module to get all links from any website. 
#One of the most powerful function in the re module is "re.findall()".
#While re.search() is used to find the first match for a pattern, re.findall() finds *all*
#the matches and returns them as a list of strings, with each string representing one match.

# This example will get all the links from any websites HTML code. 

# To find all the links, we will in this example use the urllib2 module together
# with the re.module


import urllib2
import re

#connect to a URL
website = urllib2.urlopen(url)


#read htmlcode

html = website.read()

#use re.findall to get all the links

links = re.findall('"((http | ftp)s?://.*?)"', html)


print links