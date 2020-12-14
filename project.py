#https://medium.com/better-programming/write-better-python-scripts-ce58c1ebf690

import sys
import logging
from logging import critical, error, info, warning, debug




logging.basicConfig(format='%(message)s', level=logging.DEBUG, stream=sys.stdout)



def main():
    info("Running the main program.")


try:
    a = 'string' + 10
    except Exception as e:
        error(str(e))
