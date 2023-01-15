import numpy as np
import cv2

drawing = False
ix,iy =-1,-1

def nothing(pos) :
    return pos

def event_check(event,x,y,flags,param):
    global ix,iy,drawing
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')
    m =cv2.getTrackbarPos(mode,'image')
    if s==1 :
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix,iy = x,y
        elif event == cv2.EVENT_MOUSEMOVE and drawing == True:
            if m == 0:
                cv2.rectangle(img,(ix,iy),(x,y),(r,g,b),1)
            elif m==1:
                cv2.circle(img,(x,y),5,(r,g,b),1)
            else :
                cv2.circle(img,(x,y),5,(r,g,b),-1)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False

            
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.setMouseCallback('image',event_check)

# create switch for ON/OFF functionality
switch = '0:OFF 1:ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)
mode= '0:R 1:C 2:Br'
cv2.createTrackbar(mode, 'image',0,2,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
    
cv2.destroyAllWindows()