# https://stackoverflow.com/questions/13211745/detect-face-then-autocrop-pictures

'''
This file will open the webcam up, then extract the image, this image then will be cropped
so that it only shows the face of the person, which can then later be compared.

Phase II - Crop face out
'''

import cv 
from PIL import Image
import glob
import os,re

global count

def Detect_Face(Img, faceCascade, Give_Image = False):
    # Detects face with haarcascade -- http://www.lucaamore.com/?p=638

    # Set haarcascade object options    
    HaarScale = 1.1
    HaarFlags = 0
    MinSize = (20, 20)
    MinNeighbouring = 3

    # Equalize the histogram
    cv.EqualizeHist(Img, Img)

    # Detection of the user's face
    Faces = cv.HaarDetectObjects(
            Img, faceCascade, cv.CreateMemStorage(0),
            HaarScale, MinNeighbouring, HaarFlags, MinSize)

    # Draw rectangles when found 
    if Faces and Give_Image:
        for ((x, y, w, h), n) in Faces:
            # Set two CV Points in order to draw the rectangular box.
            Point1 = (int(x), int(y))
            Point2 = (int(x + w), int(y + h))
            cv.Rectangle(Img, Point1, Point2, cv.RGB(255, 0, 0), 5, 8, 0)


    if Give_Image:
        return Img
    else:
        return Faces

def Grey_Scale(PIL_Image):
    # Turn into a greyscale image - http://pythonpath.wordpress.com/2012/05/08/pil-to-opencv-image/
    PIL_Image = PIL_Image.convert('L')
    OpenCV_Image = cv.CreateImageHeader(PIL_Image.size, cv.IPL_DEPTH_8U, 1)
    cv.SetData(OpenCV_Image, PIL_Image.tostring(), PIL_Image.size[0])
    return OpenCV_Image

def PIL_Scale(Img, Crop_Box, Box_Scale = 1):
    # Cut down a PIL Image using the box scale provided, using x,y deltas.
    
    # Scale x,y
    x_Delta = max(Crop_Box[2] * (Box_Scale - 1), 0)
    y_Delta = max(Crop_Box[3] * (Box_Scale - 1), 0)

    # Using x,y convert to PIL Box from CV
    PIL_Box = [Crop_Box[0] - x_Delta, Crop_Box[1] - y_Delta, Crop_Box[0] + Crop_Box[2] + x_Delta, Crop_Box[1] + Crop_Box[3] + y_Delta]

    return Img.crop(PIL_Box)

def Crop_Face(Img_Pattern, Box_Scale = 1):
    faceCascade = cv.Load('../cv/haarcascade_frontalface_alt.xml') # Used frontalface_alt instead of _default

    Images = glob.glob(Img_Pattern)
    if len(Images) <= -1:
        print 'No Images Found'
        return

    for Img in Images:
        PIL_Image = Image.open(Img)
        OpenCV_Image = Grey_Scale(PIL_Image)
        Faces = Detect_Face(OpenCV_Image,faceCascade)
        if Faces:
            n=1
            for Face in Faces:
                Cropped_Image = PIL_Scale(PIL_Image, Face[0], Box_Scale)
                fname, ext = os.path.splitext(Img)
                max = 128, 128
                Cropped_Image.thumbnail(max, Image.ANTIALIAS)
                Cropped_Image.save(fname+'_crop'+ext)
                ++n

        else:
            print 'No faces found: ', Img

# Crop all jpegs in a folder. Note: the code uses glob which follows unix shell rules.
# Use the boxScale to scale the cropping area. 1=opencv box, 2=2x the width and height
def Start_Crop(folder, picnum):
    #Crop_Face(folder+"/face.jpg", Box_Scale = 1)

    # print folder+'/face'+str(picnum)+'.jpg'
    Crop_Face(folder+'/face'+str(picnum)+'.jpg', Box_Scale = 1)


def clean(folder):    
    print "Cleaning up user folder..."
    for f in os.listdir(folder+"/"):
        reg = "face0|[1-9]\d{0,2}?[^_]jpg"
        if re.search(str(reg),f):
            os.remove(os.path.join(folder,f))   
