
import os
from pyfaces import *
import speech_recognition as sr
from Capture import *
import database

def verification(speech, room):	
    folder = speech[:1]

    #print "speech : " + folder # debug

    direc = "../usr/"+folder
    os.system("rsync c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/usr/%s/ direc" % speech[:1])
    #print direc # debug

    rootdir = direc

    pool = [] # of people with same passphrases
    for dirName, subdirList, fileList in os.walk(rootdir, topdown=True):
    	#print("Directory %s" % dirName) # debug
    	
    	if os.path.isfile(dirName+"/speech.txt"):
    		with open(dirName+"/speech.txt", "r") as speechfile:
    			theirpass = speechfile.readlines()[0]

    			#print theirpass # debug

    			if theirpass == speech:
    				person = os.path.basename(os.path.normpath(dirName))
    				#print person # debug

    				pool.append(person)

    			elif theirpass != speech:
    				print 'No passphrase match found.'
    				execfile('speech.py')
    		
    matchpool(pool, folder, speech, room)
    				


			


def matchpool(pool, folder, speech, room):
        ImageFromCam()
        matchDist = {}
        match = None
	for x in range(0,len(pool)):
		image = '../capturedimg/face1_crop.jpg'
		directory = '../usr/'+folder+"/"+str(pool[x])
		pyf = PyFaces(image, directory)

		dist, match = pyf.match()

		# print 'Matches = ' + str(match) 
		# print 'Distance = ' + str(dist)

		if match is not None:
			print '\nThe image "%s" matches "%s" with a distance of "%s"\n' % \
							(image, match, dist)
                        matchDist[str(pool[x])] = dist

		else:
			print 'No image match.\n'
                        matchDist[str(pool[x])] = 100

		#print pool[x] # debug
        entryPerson =  min(matchDist, key=matchDist.get)
        names = entryPerson.split('_')
        print "chosen is " + names[1],names[0] + match
        cb = database.database()
        cb.verify("../usr/"+str(speech[:1])+"/"+str(entryPerson),speech,room)
        sys.exit()

verification("spock","T2.09") # debug
