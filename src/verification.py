
import os

def verification(speech):
    folder = speech[:1]

    print "speech : " + folder

    direc = "../usr/"+folder
    print direc 

    rootdir = direc

    pool = [] # of people with same passphrases
    for dirName, subdirList, fileList in os.walk(rootdir, topdown=True):
    	print("Directory %s" % dirName)
    	
    	if os.path.isfile(dirName+"/speech.txt"):
			with open(dirName+"/speech.txt", "r") as speechfile:
				theirpass = speechfile.readlines()[0]	
				print theirpass # debug

				if theirpass == speech:
					person = os.path.basename(os.path.normpath(dirName))
					print person 

					pool.append(person)
					print "pool : " + str(pool) # debug

					for x in range(0,len(pool)):
						print pool[x] # debug

						'''
						Here you would now run Pyfaces

						Closest hit in distance wins, is determined the entrant.

						- Fill this area in soon -

						'''
						

verification("spock")