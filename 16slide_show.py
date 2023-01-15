import cv2
import numpy as np

images=["lena_2.png",
"D:\Redmi 5a\millionaire.mindset\Instagram(37).jpg",
"D:\Redmi 5a\millionaire.mindset\Instagram(31).jpg",
"D:\Redmi 5a\millionaire.mindset\Instagram(32).jpg",
"D:\Redmi 5a\millionaire.mindset\Instagram(33).jpg",
"D:\Redmi 5a\millionaire.mindset\Instagram(34).jpg",
"D:\Redmi 5a\millionaire.mindset\Instagram(35).jpg",
"D:\Redmi 5a\millionaire.mindset\Instagram(36).jpg"]

i=0
while(True) :
    img1= cv2.imread(images[i%8])
    img2=cv2.imread(images[(i+1)%8])
    img1= cv2.resize(img1, (512,512))
    img2= cv2.resize(img2, (512,512))

    cv2.imshow('frame',img1)
    res1 = cv2.addWeighted(img1, 0.3,img2,0.7,0)
    res2= cv2.addWeighted(img1, 0.1,img2,0.9,0)

    k= cv2.waitKey(5000)
    # if k== ord('n'):
    cv2.imshow('frame',res1)
    cv2.waitKey(200)
    cv2.imshow('frame',res2)
    cv2.waitKey(200)
    #cv2.imshow('frame',img2)

    if k== 27:
        break
    i=i+1

    cv2.waitKey(1)



cv2.destroyAllWindows()