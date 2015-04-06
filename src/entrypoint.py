import speech_recognition as sr

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
			cont = 0;
			execfile('Capture.py')
		else:
			execfile('entrypoint.py')

	except LookupError:                            # speech is unintelligible
	    print("Could not understand audio")
	    execfile('entrypoint.py')