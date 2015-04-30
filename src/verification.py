'''
Central file to handle matching using pyfaces, folder directories and syncing to database module

'''

import os
from pyfaces import *
import speech_recognition as sr
from Capture import *
import database
from audio import Audio
import subprocess

class Verify:
    def verification(self, speech):	
        folder = speech[:1]


        #print "speech : " + folder # debug

        direc = "../usr/"+folder
        subprocess.call('rsync -chavzP --stats c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/usr/%s ../usr/' % (speech[:1]), shell=True)            
        print direc # debug

        rootdir = direc

        pool = [] # of people with same passphrases
        for dirName, subdirList, fileList in os.walk(rootdir, topdown=True):
        	print("Directory %s" % dirName) # debug
        	
        	if os.path.isfile(dirName+"/speech.txt"): # if the file with passphrase in it exists 
                    with open(dirName+"/speech.txt", "r") as speechfile: # open it
        			theirpass = speechfile.readlines()[0] 

                    if theirpass == speech: # if it matches the passphrase user spoke
                        person = os.path.basename(os.path.normpath(dirName)) 
                        pool.append(person) # add them to pool of people that could possibly match

                    else:
                        print "No passphrase match found." 
                        Audio().aud('../audio/NoMatch.wav')
                        execfile('speech.py')


        Verify().matchpool(pool, folder, speech) 


    def matchpool(self, pool, folder, speech): 
        room = raw_input("Enter name of ROOM (e.g T2.09): ") # Simple input to see which room they're accessing

        print "Capturing image of your face.. PLEASE KEEP STILL!"
        Capture().ImageFromCam() # Capturing their face begins
        matchDist = {}
        match = None
	    
        for x in range(0,len(pool)): 
            image = '../capturedimg/face1_crop.jpg'
            directory = '../usr/'+folder+"/"+str(pool[x])
            pyf = PyFaces(image, directory) 

            dist, match = pyf.match() # get a match

    		# print 'Matches = ' + str(match) 
    		# print 'Distance = ' + str(dist)

            if match is not None:
                print '\nThe image "%s" matches "%s" with a distance of "%s"\n' % (image, match, dist)
                matchDist[str(pool[x])] = dist

            else:
                print 'No image match.\n'
                matchDist[str(pool[x])] = 100
                Audio().aud('../audio/NoMatch.wav')

		#print pool[x] # debug
        if bool(matchDist) != False: # If person was found in the pool
            entryPerson =  min(matchDist, key=matchDist.get)
            names = entryPerson.split('_')
            print "\nMATCHED PERSON: " + names[1],names[0] + match # show who matched
            cb = database.database()
            cb.verify("../usr/"+str(speech[:1])+"/"+str(entryPerson),speech,room) # verify they're allowed access
        else: # Else if no one was found, goes back to entrypoint.
            print "ERROR - MATCH FAILED: Folder is empty."            
        print '\nFinishing by syncing local capture to remote..' 
        # subprocess.call('rsync ../capturedimg/face1_crop.jpg c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/capturedimg', shell=True) # sync with remote
        print 'FINISHED.'
        execfile('entrypoint.py')

