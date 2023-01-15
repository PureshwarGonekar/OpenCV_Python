import cv2

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,7000) # we can use index value instead of CAP_PROP_FRAME_WIDTH 
cap.set(4,700)

print('After set width and height----')
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(cap.isOpened()) :
    ret,frame = cap.read()
    if(ret == True):
        gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame Window', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()