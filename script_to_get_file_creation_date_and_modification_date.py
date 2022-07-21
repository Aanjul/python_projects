# For refrence https://www.programiz.com/python-programming/examples/file-modification-date

import datetime
import pathlib


fname = pathlib.Path('abc.py')
# put the file here or file path

print("Last modification time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_mtime))
print("Last metadata change time or path creation time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_ctime))

