'''This script will be take in an image.It will allow for file searching. It will take an image and look for a smile.
If a smile is found 'smile' will be returned. Else, it will look for a natural expression and return 'natural.'Finally, if no expression is found, the script will return 'no expression.' 'No expression' will be returned if there is face in image.''' 

import numpy as np
import cv2
from tkFileDialog import askopenfilename
import Tkinter as tk
from PIL import Image

#cascades for facial recognition
face_cascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
neutral_cascade = cv2.CascadeClassifier("cascades/neutralCas6.xml")
smile_cascade = cv2.CascadeClassifier("cascades/haarcascade_smile.xml")

def faceDetect():
	
	#will serve as flags on wheter any face, smile, or neutral face is found
	faceFound = False
	smileFound = False
	neutralFound = False

	root = tk.Tk()
	root.withdraw()

	filePic = askopenfilename() #gets filename from user. Function returns a string
	pic = cv2.imread(filePic)

	gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(
		gray,
		scaleFactor = 1.05,
		minNeighbors = 8,
		minSize = (55,55),
		flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)

	for (x, y, w, h) in faces: #will run if there is a face detected
		if (len(faces) > 1):#if more than one face the program exits
			exit()
		faceFound = True
		
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = pic[y:y+h, x:x+w]

	neutral = neutral_cascade.detectMultiScale(
		pic,
		scaleFactor = 1.1,
		minNeighbors = 5,
		minSize = (55, 55),
		flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)

	if (len(neutral) == 1):#will run if there is a neutral face detected
		neutralFound = True
	elif (len(neutral) > 1):
		exit() #more than one face, the program will exit
		
	smile = smile_cascade.detectMultiScale(
		roi_gray,
		scaleFactor = 1.7,
		minNeighbors = 22,
		minSize = (25,25),
		flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)

	if (len(smile) == 1):#will run if there is a smile detected
		smileFound = True
	elif (len(smile) > 1):#if more than one smiles is detected the program exits
		exit()
	

	#method to find if a face, neutral, or smile was found. Returns result as string
	if ((faceFound is False) and (neutralFound is False) and (smileFound is False)):
		return "no face"
	elif((faceFound is True) and (neutralFound is False) and (smileFound is False)):
		return "face"
	elif((faceFound is True) and (neutralFound is True) and (smileFound is False)):
		return "neutral"
	else:
		return "smile"


	



	
	
	
