import numpy as np
import cv2
from matplotlib import pyplot as plt

#read image from file
image_bgr = cv2.imread('meatball.jpg',1)

#changing color space from BGR to HSV
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

#changing color space from BGR to RGB
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

#show BGR image
#cv2.imshow('BGR',image_bgr)

#show HSV image
#cv2.imshow('HSV',image_hsv)

#show RGB image
#cv2.imshow('RGB',image_rgb)


#color histogram
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([image_bgr], [i], None, [256], [0, 256])
    cv2.imshow('meatball',image_bgr)
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()


#cv2.waitKey(0)
#cv2.destroyAllWindows()