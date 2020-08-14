# For Refrence https://www.pythonforbeginners.com/code-snippets-source-code/os-walk-and-fnmatch-in-python

import fnmatch
import os

routhPath = '/'
pattern = '*.mp3'

for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))