import cv2
import numpy as np

img1= np.zeros((250,500,3),np.uint8)
img1= cv2.rectangle(img1,(200,0),(300,100),(2555,255), -1)
img2= cv2.imread('lena_2.png')

img1= cv2.resize(img1, (512,512))
img2= cv2.resize(img2, (512,512))

bitAnd = cv2.bitwise_and(img1,img2)
bitOr = cv2.bitwise_or(img1,img2)
bitXor = cv2.bitwise_xor(img1,img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.imshow('bitNot1',bitAnd)
# cv2.imshow('bitNot2',bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()