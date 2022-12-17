import cv2
import keyboard

# text.xml
face_cascade =cv2.CascadeClassifier('text.xml')
img = cv2.imread('img.jpg')

# convertim imag in alb negru
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detectam fetele

faces = face_cascade.detectMultiScale(gray, 1.1,4)
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
 # afisam imaginea

cv2.imshow('Imagine: ', img)
cv2.waitKey()