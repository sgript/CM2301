
import os

def alphFolder():
	path = "../usr/"
	letter = "a"
	for x in range(0,26):
		if not os.path.exists(path+letter):
			os.makedirs(path+letter)
			letter = chr(ord(letter) + 1)
			
		
	print "Folder structure in place.\nContinuing.."

