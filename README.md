# FaceTen 


**Introduction:**

	+ Detecting faces and recognising faces, along with speech to text (Google Speech API) and database storing. 

**Contributors:**

	* Shazaib Ahmad (sIurps)
	* Jack Parsons  (worzel666)

**Instructions:**

	* Use entrypoint.py to initialise the system
	* Passphrase to microphone: Entry to initialise 
	* Runs speech.py - Speak user-registered passphrase
	* Takes capture, matches to record in database
	* To register use Register.py

	Usage:
	python entrypoint.py
	python Register.py

	Records are saved under /usr/letter/lastname_firstname/
	All records are rsynced to web server. 
	

**To-do:**

	* Check user's status is "active" in the system
	* Finish off voiceovers using audio class
	* Finish GUI / Polish
	* Read only for speech.txt(?)
	* Ensure user exists in the database (as well as being "active") before letting them in
	* Testing - test cases, compatibility with administrator portal
	* Program to executables and package files to port dependencies



