import speech_recognition as sr
from audio import Audio
import time

r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as $
    audio = r.listen(source)                   # listen for the first phrase an$


cont = 1
while(cont):
	try:
		saidWord = r.recognize(audio)
		print("You said " + saidWord)    # recognize speech using Google $

		if saidWord == "entry":
			print("User asked for entry, initialising..")
			time.sleep(0.5)
			Audio().aud('../audio/crtna.wav')
			cont = 0;
			execfile('speech.py')
		else:

			Audio().aud('../audio/Retry.wav')
			print "You did not ask for entry. Retry.."
			execfile('entrypoint.py')

	except LookupError:
		print("Could not understand audio")
		execfile('entrypoint.py')