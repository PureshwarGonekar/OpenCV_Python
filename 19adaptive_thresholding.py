import cv2 as cv
import numpy as np

img = cv.imread('opencv-4.x\samples\data\sudoku.png')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
# adaptiveThreshold function require gray scale image that its must to convert color img to grayscale

_, th1 = cv.threshold(img, 127,255,cv.THRESH_BINARY,0)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)

cv.imshow('Grediant image originaL',img)
cv.imshow('Threshold Binary',th1)
cv.imshow('Adaptive Threshold Mean C',th2)
cv.imshow('Adaptive Threshold Gaussian',th3)

cv.waitKey(0)
cv.destroyAllWindows()