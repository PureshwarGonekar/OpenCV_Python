import numpy
import cv2

img = cv2.imread('opencv-4.x\samples\data\messi5.jpg')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)

print(img)
print('Different channels of img---')
print(b)
print(g)
print(r)
img = cv2.merge((b,g,r))

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()