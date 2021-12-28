# For refrence https://towardsdatascience.com/5-python-tricks-to-make-your-life-more-productive-974ebeb54a53

import speech_recognition as sr
from pydub import AudioSegment

sound = AudioSegment.from_mp3("output.mp3")
sound.export("transcript.wav", format="wav")

AUDIO_FILE = "transcript.wav"
r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
	audio = r.record(source)
	
print(r.recognize_google(audio))