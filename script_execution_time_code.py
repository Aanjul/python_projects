#For Refrence https://github.com/realpython/python-scripts/blob/master/scripts/06_execution_time.py


"""
ExecutionTime

This class is used for timing execution of code.


For example:

timer = ExecutionTime()
print = 'This is some text'
print 'Finished in {}  seconds.'.format(timer.duration())


"""

import time
import random

class ExecutionTime:

            def__init__(self):
                 self.start_time = time.time()

           def duration(self):
              return time.time()  - self.start_time

#---- run code ----#

timer = ExecutionTime()
sample_list = list()
my_list = [random.randint(1, 888898) for num in
 	range(1, 10000000) if num % 2 == 0 ]
print('Finished in {} seconds.'.format(timer.duration()))


