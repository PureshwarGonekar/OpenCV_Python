import cv2
# '''
# showing recorded vedio file
cap =cv2.VideoCapture('steve_harvey.mp4')
if cap.isOpened() :
    print(cap.isOpened())
    w= cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h= cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print('Resolution : ',w,'x',h)
    fr= cap.get(cv2.CAP_PROP_FPS)
    print('Frame Rate : ',fr)
    print('No of Frame in the video : ',cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # video properties
    print('Video Properties ---')
    print('Brightness : ',cap.get(cv2.CAP_PROP_BRIGHTNESS))
    print('SATURATION : ',cap.get(cv2.CAP_PROP_SATURATION))

while(cap.isOpened()):
    ret, frame =cap.read() # ret contains true or false to tell that from is available

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    cv2.imshow('Frame',gray)
    if cv2.waitKey(25) & 0xFF == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()

# '''
# recording the vedio from camera
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # frame = cv2.flip(frame,0)
        # write the flipped frame

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        out.write(frame)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
