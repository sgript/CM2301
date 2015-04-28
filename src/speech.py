'''
Users passphrase will be detected here and taken onwards to be matched and their face captured.

Phase I - Detect speech
'''

import speech_recognition as sr
from verification import verification
from audio import Audio

def listenError():
	Audio().aud('../audio/NotUnderstood.wav')
	listen()


def listen():
	r = sr.Recognizer()
	Audio().aud('../audio/Speak.wav')
	print 'Please say your chosen passphrase AFTER the beep.'
	Audio().aud('../audio/now.wav')

	with sr.Microphone() as source:
		#audio = r.adjust_for_ambient_noise(source, duration = 1)
		#audio = r.dynamic_energy_threshold = True
		audio = r.listen(source)	
		if audio:
			print "Audio caught, please wait - Processing."
		else:
			print "No audio caught."
			listenError()

	try:

	    list = r.recognize(audio,True)                  # generate a list of possible transcriptions
	    print("Possible transcriptions:")
	    for prediction in list:
	    	text = prediction["text"]
	    	confidence = prediction["confidence"]*100.0
	    	
	    	if "*" in text:
	    		print "Bad word detected, please retry."
	    		listen()
	    		break

	        print("Detected speech: " + text.upper() + " with confidence level of: %.1f" % (confidence))

	        if confidence > 51:
	        	print "Matched " + text
	        	verification(str(text.lower()))
	        	break
	        	

	        else:
	        	Audio().aud('../audio/Retry.wav')
	        	print 'Retry'
	        	execfile('speech.py')
	        	break


	except LookupError, e: 
		print("Could not understand audio, retry..\n" + str(e))
		listenError()

print "CHECK INTERNET CONNECTION BEFORE BEGINNING."
print "PLEASE SPEAK AFTER THE BEEP."
listen()