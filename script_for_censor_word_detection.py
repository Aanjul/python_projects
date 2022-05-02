# For refrence https://github.com/avinashkranjan/Amazing-Python-Scripts/blob/master/Censor%20word%20detection/censor_word_detection.py

from better_profanity import profanity

def detect(data):
	try:
		output = profanity.censor(data, '#')
		print(output)
	except Exception as e:
		print(e)
		

profanity.load_censor_words()

data = input("enter your msg:")
detect(data)