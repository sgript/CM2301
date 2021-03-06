'''
Programs starting point, once entry is requested, user is let through.

START PHASE
'''

import speech_recognition as sr
from audio import Audio
import time
from speech import Speech

class Entry:
    def listenError(self):
        Audio().aud('../audio/NotUnderstood.wav')
        Entry().listen()    
        

    def listen(self):

        r = sr.Recognizer()
        print "Please say Entry AFTER the beep." 
        Audio().aud('../audio/Speak.wav')
        Audio().aud('../audio/now.wav') # beep sound
        with sr.Microphone() as source:                # use microphone
            audio = r.listen(source)                   # listen 
            if audio: # messages if audio was heard or not
                print "Audio caught, please wait - Processing." 
            else:
                print "No audio caught."
                # entry.listenError()

        active = 1
        while(active): # runs continously, so system hands back to entrypoint when finished
            
            try:
                
                saidWord = r.recognize(audio) # gets recognised word/sentence
                if "*" in saidWord: # extra censoring of bad words
                    print "Bad word detected, please try."
                    Entry().listen()
                    break

                else:
                    print("You said " + saidWord)    # output of word


                if "entry" in saidWord: # if entry/entry please etc is asked, system is initiated 
                    print("User asked for entry, initialising..")
                    time.sleep(0.5)
                    Audio().aud('../audio/crtna.wav') # voiceover of system
                    active = 0
                    Speech().passphrase() # passphrase of user is asked
                    break
                else:
                    print "You did not ask for entry. Retry.." # otherwise retry
                    # Audio().aud('../audio/Retry.wav')
                    Entry().listen()
                    break

            except LookupError:
                print "Input not understood."
                Entry().listen()

print "ENTRY PROGRAM STARTED TO LISTEN FOR ACCESS REQUESTS."       
print "CHECK INTERNET CONNECTION BEFORE BEGINNING.\nPLEASE SPEAK AFTER THE BEEP."   
Entry().listen()