import cv2 as cv
import numpy as np

img = cv.imread('opencv-4.x\samples\data\gradient.png')

_, th1 = cv.threshold(img, 50,255,cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 127,255,cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127,255,cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127,255,cv.THRESH_BINARY_INV)

cv.imshow('Grediant image originaL',img)
cv.imshow('Threshold Binary',th1)
cv.imshow('Threshold Binary Inverse',th2)
cv.imshow('Threshold Truncate',th3)
cv.imshow('Threshold Truncate Inverse',th4)

cv.waitKey(0)
cv.destroyAllWindows()