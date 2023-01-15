import numpy as np
import cv2 as cv
img = cv.imread('messi5.jpg')
px = img[100,100]
print( px )
# accessing only blue pixel
blue = img[100,100,0]
print( blue )
img[100,100] = [255,255,255]
print( img[100,100] )

# accessing RED value
img.item(10,10,2)
# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

# Accessing Image Properties
print( img.shape )
print( img.size )
print( img.dtype )


# Image ROI
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
b,g,r = cv.split(img)
img = cv.merge((b,g,r))

# Splitting and Merging Image Channel
b,g,r = cv.split(img)
img = cv.merge((b,g,r)) 

# cv.split() is a costly operation (in terms of time). So do it only if you need it. Otherwise go for Numpy indexing.