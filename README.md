#![alt tag](http://i.imgur.com/FFLYOQt.png)

**Introduction:**
* Detecting faces and recognising faces, along with speech to text (Google Speech API) and database storing. 

**Contributors:**
* Shazaib Ahmad (sIurps)
* Jack Parsons  (worzel666)

**Instructions:**
* Use entrypoint.py to initialise the system
* Passphrase to microphone: Say "entry" to initialise 
* Runs speech.py - Speak user-registered passphrase
* Takes capture, matches to record in database
* To register user records use Register.py

**Usage:**

	python entrypoint.py
	python Register.py
	

* Records are saved under /usr/letter/lastname_firstname/
* All records are rsynced to web server. 
* Please read terminal outputs when using
	
**Dependencies required:**
* OpenCV
* PyAudio
* FLAC
* MySQLdb (OSX users may need mysql-connector-c also, can be obtained through brew)
* numpy
* Pillow / PIL
* PyQt 
* [Library for Google's Speech Recognition API](https://pypi.python.org/pypi/SpeechRecognition/)

<!-- **To-do:**
* Finish GUI / Polish
* Ensure user exists in the database (as well as being "active") before letting them in
* Test for compatability with administrator portal
* Check user's status is "active" in the system
* Read only for speech.txt(?)
* Program to executables and package files to port dependencies  -->

**Credits:**
* [Pyfaces by omab](https://github.com/omab/faces/tree/master/pyfaces)
* [FaceDetectionCrop by GradyD](https://github.com/GradyD/FaceDetectionCrop)



