import numpy as np
import cv2 as cv
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE and drawing == True:
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        mode=False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv.destroyAllWindows()



# import numpy as np
# import cv2

# drawing = False
# mode= True # true-> to draw the circle and false-> to draw the rectangle
# ix,iy = -1,-1

# def click_event(event,x, y, flags, param) :
#     global ix,iy,drawing,mode
#     if event == cv2.EVENT_LBUTTONDOWN :
#         drawing= True
#         ix,iy= x,y
#     elif event == cv2.EVENT_MOUSEMOVE :
#         if drawing == True:
#             if mode == True:
#                 cv2.circle(img, (x,y), 5, (0,255,255),-1)
#             else :
#                 cv2.rectangle(img,(ix,iy), (x,y), (255,255,0),-1)
#     elif event == cv2.EVENT_LBUTTONUP :
#         drawing == False
#         mode == False
#         if mode == False:
#             cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#         else:
#             cv2.circle(img,(x,y),5,(0,0,255),-1)

# img= np.zeros((512,512,3),np.uint8)
# # img = cv2.imread('lena_2.png')
# cv2.imshow('image',img)
# cv2.setMouseCallback('image',click_event)
# while(1):
#     cv2.imshow('image',img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27:
#         break
# cv2.destroyAllWindows()