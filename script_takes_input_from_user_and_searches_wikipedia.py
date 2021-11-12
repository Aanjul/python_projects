#For refrence https://github.com/hastagAB/Awesome-Python-Scripts/tree/master/Wikipedia-Search

# Requirements

# Wikipedia Library (https://pypi.org/project/wikipedia/)


import wikipedia

print("Welcome to the app which find an answer to your question from wikipedia")

while True:
	ques = input("What would you like to ask Wikipedia?")
	wikipedia.set_lang("en") #change "en" to convenient language for example wikipedia.set_lang("es") will set the language to spanish
	print wikipedia.summary(ques, sentences=3)
