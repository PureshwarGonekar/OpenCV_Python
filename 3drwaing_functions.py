import numpy as np
import cv2

# img = cv2.imread('lena_2.png',1)
img = np.zeros((512,512,3),np.uint8)
img = cv2.line(img,(0,0), (150,160), (255,0,0), 5)
img = cv2.arrowedLine(img, (0,400), (160,160),(0,255,255))
img = cv2.rectangle(img, (510,234), (70,45), (0,255,0),3)
img = cv2.circle(img, (300,300), 100,(0,0,255),2)
font = cv2.FONT_HERSHEY_PLAIN
img = cv2.putText(img,"I'm Learning OpenCV", (40,460), font,2,(255,255,255),3 )
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

cv2.imshow('Dwaing on image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 