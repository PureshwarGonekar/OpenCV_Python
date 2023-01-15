import numpy as np
import cv2

def nothing(x) :
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)

cv2.createTrackbar("HH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("HS", "Tracking", 255, 255, nothing)
cv2.createTrackbar("HV", "Tracking", 255, 255, nothing)

while(True) :
    img = cv2.imread('opencv-4.x\samples\data\smarties.png')

    hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    h_h = cv2.getTrackbarPos("HH", "Tracking")
    h_s = cv2.getTrackbarPos("HS", "Tracking")
    h_v = cv2.getTrackbarPos("HV", "Tracking")

    low= np.array([l_h, l_s, l_v])
    high= np.array([h_h, h_s, h_v])

    mask = cv2.inRange(hsv,low,high)

    res= cv2.bitwise_and(img,img, mask=mask)

    cv2.imshow("img",img)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    k= cv2.waitKey(1)
    if k== 27:
        break

cv2.destroyAllWindows()