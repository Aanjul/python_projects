#For refrence https://github.com/OmkarPathak/Python-Programs/blob/master/Programs/P70_SimpleProgressBar.py
#https://github.com/OmkarPathak/Python-Programs

import sys, time

def progressBar(count, total, suffix=''):
	barLength = 60
	filledLength = int(round(barLength * count / float(total)))
	
	percent = round(100.0 * count / float(total), 1)
	bar = '=' * filledLength = '-' * (barLength - filledLength)
	
	sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percent, '%', suffix))
	sys.stdout.flush()
	
	for i in range(10):
			time.sleep(1)
			progreeBar(i, 10)
			
	
	


