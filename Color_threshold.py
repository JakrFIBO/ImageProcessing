import cv2
import numpy as np

def nothing(x):
    pass

# Create windows
cv2.namedWindow('trackbar_HSV')
cv2.namedWindow('image_original')
cv2.namedWindow('mask_image')
# Create trackbars for HSV threshold
cv2.createTrackbar('H_min','trackbar_HSV',0,255,nothing)
cv2.createTrackbar('H_max','trackbar_HSV',255,255,nothing)
cv2.createTrackbar('S_min','trackbar_HSV',0,255,nothing)
cv2.createTrackbar('S_max','trackbar_HSV',255,255,nothing)
cv2.createTrackbar('V_min','trackbar_HSV',0,255,nothing)
cv2.createTrackbar('V_max','trackbar_HSV',255,255,nothing)

image_bgr = cv2.imread('included.jpg',1)
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

while(1):

    H_min = cv2.getTrackbarPos('H_min', 'trackbar_HSV')
    H_max = cv2.getTrackbarPos('H_max', 'trackbar_HSV')
    S_min = cv2.getTrackbarPos('S_min', 'trackbar_HSV')
    S_max = cv2.getTrackbarPos('S_max', 'trackbar_HSV')
    V_min = cv2.getTrackbarPos('V_min', 'trackbar_HSV')
    V_max = cv2.getTrackbarPos('V_max', 'trackbar_HSV')

    HSV_min = np.array([H_min, S_min, V_min])
    HSV_max = np.array([H_max,S_max,V_max])

    mask = cv2.inRange(image_hsv,HSV_min,HSV_max)

    cv2.imshow('image_original',image_bgr)
    cv2.imshow('mask_image',mask)


    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break







cv2.destroyAllWindows()