import cv2
img = cv2.imread('opencv-4.x\samples\data\lena.jpg' ,1)

print(img)  
cv2.imshow('Test Image', img)
k= cv2.waitKey(5000)

if k==27:
    cv2.destroyAllWindows() # cv2.destroyWindow()
elif k== ord('s') :
    cv2.imwrite('lena_2.png',img)
    cv2.destroyAllWindows()