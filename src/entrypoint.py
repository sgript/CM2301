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
        entry.listen()    
        

    def listen(self):
        r = sr.Recognizer()
        print "Please say Entry AFTER the beep."
        Audio().aud('../audio/Speak.wav')
        Audio().aud('../audio/now.wav')
        with sr.Microphone() as source:                # use the default microphone as $
            audio = r.listen(source)                   # listen for the first phrase an$
            if audio:
                print "Audio caught, please wait - Processing."
            else:
                print "No audio caught."
                entry.listenError()


        cont = 1
        while(cont):

            try:
                saidWord = r.recognize(audio)
                if "*" in saidWord:
                    print "Bad word detected, please try."
                    entry.listen()
                    break

                else:
                    print("You said " + saidWord)    # recognize speech using Google $


                if "entry" in saidWord:
                    print("User asked for entry, initialising..")
                    time.sleep(0.5)
                    Audio().aud('../audio/crtna.wav')
                    cont = 0;
                    #execfile('speech.py')
                    Speech().passphrase()
                else:
                    print "You did not ask for entry. Retry.."
                    Audio().aud('../audio/Retry.wav')
                    entry.listen()
                    break

            except LookupError:
                entry.listenError()
                break


if __name__ == '__main__':
    try:
        print "CHECK INTERNET CONNECTION BEFORE BEGINNING.\nPLEASE SPEAK AFTER THE BEEP."       
        entry = Entry()
        entry.listen()
    except (Exception) as err:
        print err
