from pyfaces import PyFaces
import FaceDetection

test = PyFaces(FaceDetection.main(),"/home/jack/Programming/Group")

if test.match() == 0:
    print "NO MATCH"
else:
    print "MATCH"

#if __name__ == '__main__':
    
