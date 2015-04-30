
import os

def alphFolder():
	path = "../usr/" # path to create on
	letter = "a" # starts from the letter "a"
	for x in range(0,26): 
		if not os.path.exists(path+letter): 
			os.makedirs(path+letter) # make directory for each letter
			letter = chr(ord(letter) + 1) 
			
		
	print "Folder structure in place.\nContinuing.."

