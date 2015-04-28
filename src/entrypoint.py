'''
Programs starting point, once entry is requested, user is let through.

START PHASE
'''

import speech_recognition as sr
from audio import Audio
import time

def listenError():
	Audio().aud('../audio/NotUnderstood.wav')
	listen()	
	

def listen():
	r = sr.Recognizer()
	Audio().aud('../audio/Speak.wav')
	print "Please say Entry AFTER the beep."
	Audio().aud('../audio/now.wav')
	with sr.Microphone() as source:                # use the default microphone as $
	    audio = r.listen(source)                   # listen for the first phrase an$
	    if audio:
	    	print "Audio caught, please wait - Processing."
	    else:
			print "No audio caught."
			listenError()


	cont = 1
	while(cont):

		try:
			saidWord = r.recognize(audio)
			if "*" in saidWord:
				print "Bad word detected, please try."
				listen()
				break

			else:
				print("You said " + saidWord)    # recognize speech using Google $


			if "entry" in saidWord:
				print("User asked for entry, initialising..")
				time.sleep(0.5)
				Audio().aud('../audio/crtna.wav')
				cont = 0;
				execfile('speech.py')
			else:
				print "You did not ask for entry. Retry.."
				Audio().aud('../audio/Retry.wav')
				listen()
				break

		except LookupError:
			listenError()
			break

print "CHECK INTERNET CONNECTION BEFORE BEGINNING."
print "PLEASE SPEAK AFTER THE BEEP."
listen()