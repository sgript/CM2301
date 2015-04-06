import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as $
    audio = r.listen(source)                   # listen for the first phrase an$

try:
    print("You said " + r.recognize(audio))    # recognize speech using Google $
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")