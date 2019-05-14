import cv2 #import opencv
import numpy

# Creates a classifier object for faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Creates a classifier object for eyes
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Read image
img = cv2.imread('assets/images/stock.jpeg')

# Convert image to gray scale
gray_picture = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Returns the face position in the image
faces = face_cascade.detectMultiScale(gray_picture, 1.3, 5)

# Print a rectangle where there is a face
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255, 255, 0), 2)

# Shows a window with the image
cv2.imshow('my first image', img)
cv2.waitKey(0) # press any key
cv2.destroyAllWindows()
