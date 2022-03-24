# For refrence https://github.com/OmkarPathak/Python-Programs/blob/master/Scripts/P14_ScriptToPlaySongs.py

# https://github.com/OmkarPathak/Python-Programs

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speech recognition
import os
import datetime
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #voices[1].id for female assistant

#speak function to speak the string passed to it.
def speak(audio):
	engine.say(audio)
	engine.runAndWait()
#function to listen your command and process them
def takedata():
	r= sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		audio = r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio,language='en-in') #language set is Indian English
		print("The user said ",query)
	except Exception :
		print("Sorry i was unable to catch that. Please try speaking that again.")
		return 'None'
	return query
	
def wishme():
	hours = datetime.datetime.now().hour
	
	if hours>=0 and hours <12:
		speak("good morning")
	elif hours>=12 and hours <18:
		speak("good afternoon")
	else:
		speak("good evening")
	speak("sir i am your personal assistant. tell me how can i help you ")
	
	wishme()
	query = takedata()
	if 'play music' or 'play songs' in query:
		music_dir = "F:\\Songs" #put the location of the folder where you store your songs
		songs = os.listdir(music_dir)
		1 = len(songs)
		num = random.randrange(0,1,1)
		os.startfile(os.path.join(music_dir,songs[num]))
		speak("Thank you for using my services. All improvements on my github repository are welcome.")
		print("www.github.com")
		exit()
	else:
			speak("Query type not supported")			
		


