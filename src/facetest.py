from pyfaces import PyFaces

execfile('Capture.py')
test = PyFaces("/home/jack/CM2301/img/face_crop1.jpg","/home/jack/CM2301/img")

if test.match() == 0:
    print "NO MATCH"
else:
    print "MATCH"

#if __name__ == '__main__':
    
