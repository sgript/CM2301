import speech_recognition as sr
from verification import verification

def checkspeech():
	r = sr.Recognizer()
	print 'Speak now.'
	with sr.Microphone() as source:
		audio = r.adjust_for_ambient_noise(source, duration = 1)
		audio = r.dynamic_energy_threshold = True
		audio = r.listen(source)

		#print("You said " + r.recognize(audio))
	

	try:

	    list = r.recognize(audio,True)                  # generate a list of possible transcriptions
	    print("Possible transcriptions:")
	    for prediction in list:
	    	text = prediction["text"]
	    	confidence = prediction["confidence"]*100
	        print(" " + text + " (" + str(confidence) + "%)")

	        if confidence > 80:
	        	print "matched " + text
	        	verification(str(text.lower()))
	        	break
	        	

	        else:
	        	print 'Retry'
	        	execfile('speech.py')
	        	break


	except LookupError, e:                                 # speech is unintelligible
	    print("Could not understand audio, retry.." + str(e))
	    execfile('speech.py')


checkspeech()
	 

