# For refrence https://www.pythonforbeginners.com/code-snippets-source-code/tweet-search-with-python/

#!/usr/bin/python

import json
import sys
import urllib2
import os

usage = """

Usage:./tweet_search.py 'keyword'
e.g ./tweet_search.py phythonforbeginners

Use "+" to replace whitespace"
e.g ./tweet_search.py "phython+for+beginners"
"""

# Check that the user puts in an argument, else print the usage variable, then quit.

if len(sys.argv)!=2:
	print (usage)
	sys.exit(0)


# The screen name in Twitter, is the screen name of the user for whom to return results for. 

# Set the screen name to the second argument
screen = sys.argv[1]

# Open the twitter search URL the result will be shown in json format

url = urllib2.urlopen("http://search.twitter.com/search.json?q="+screen)

#convert the data and load it into json

data = json.load(url)

#to print out how many tweets there are
print len(data), "tweets"

#Start parse the tweets from the results

#Get only text

for tweet in data["results"]:
	print tweet["text"]

#Get the status and print out the contents

for status in data['results']:
	print "(%s) %s" % (status["created_at"], status["text"])


