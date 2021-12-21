# For refrence https://codesource.io/collection-of-the-20-useful-python-scripts/#google_vignette

import string
from random import *
characters = string.ascii_letters  + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print (password)