
## For Refrence https://www.pythonforbeginners.com/code-snippets-source-code/os-walk-and-fnmatch-in-python


#script uses ‘os.walk’ and ‘fnmatch’ with filters to search the hard-drive for all image files

import fnmatch
import os

images = ['*.jpg', '*.jpeg', '*.png', '*.tig', '*.tiff']
matches = []

for root, dirnames, filenames in os.walk("C:\"):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))


            