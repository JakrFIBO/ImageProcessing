import numpy as np
import cv2
from matplotlib import pyplot as plt

#minimum object area
min_object_area = 50*50
#read image from file
image_bgr = cv2.imread('included.jpg',1)

#changing color space from BGR to HSV
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

#define HSV_threshold of object
#mama hsv completed
mama_hmin = 22
mama_hmax = 28
mama_smin = 83
mama_smax = 192
mama_vmin = 123
mama_vmax = 204

#meatball hsv completed
meatball_hmin = 0
meatball_hmax = 53
meatball_smin = 22
meatball_smax = 255
meatball_vmin = 47
meatball_vmax = 255


#mincepork hsv completed
mincepork_hmin = 0
mincepork_hmax = 49
mincepork_smin = 18
mincepork_smax = 255
mincepork_vmin = 45
mincepork_vmax = 255

#Ipomoea
Ipomoea_hmin = 0
Ipomoea_hmax = 14
Ipomoea_smin = 36
Ipomoea_smax = 255
Ipomoea_vmin = 144
Ipomoea_vmax = 255



#declare HSV
#mama
mama_HSV_min = np.array([mama_hmin, mama_smin, mama_vmin])
mama_HSV_max = np.array([mama_hmax,mama_smax,mama_vmax])

#meatball
meatball_HSV_min = np.array([meatball_hmin, meatball_smin, meatball_vmin])
meatball_HSV_max = np.array([meatball_hmax,meatball_smax,meatball_vmax])

#mincepork
mincepork_HSV_min = np.array([mincepork_hmin, mincepork_smin, mincepork_vmin])
mincepork_HSV_max = np.array([mincepork_hmax,mincepork_smax,mincepork_vmax])

#Ipomoea
Ipomoea_HSV_min = np.array([Ipomoea_hmin, Ipomoea_smin, Ipomoea_vmin])
Ipomoea_HSV_max = np.array([Ipomoea_hmax,Ipomoea_smax,Ipomoea_vmax])

mama_mask = cv2.inRange(image_hsv,mama_HSV_min,mama_HSV_max)
meatball_mask = cv2.inRange(image_hsv,meatball_HSV_min,meatball_HSV_max)
mincepork_mask = cv2.inRange(image_hsv,mincepork_HSV_min,mincepork_HSV_max)
Ipomoea_mask = cv2.inRange(image_hsv,Ipomoea_HSV_min,Ipomoea_HSV_max)

mama_kernel = np.ones((20,20),np.uint8)
kernel = np.ones((10,10),np.uint8)


#erosion = cv2.erode(mama_mask,kernel,iterations = 1)
de_mama = cv2.dilate(mama_mask,mama_kernel,iterations = 1)
de_meatball = cv2.dilate(meatball_mask,kernel,iterations = 1)
de_mincepork = cv2.dilate(mincepork_mask,kernel,iterations = 1)
de_Ipomoea = cv2.dilate(Ipomoea_mask,kernel,iterations = 1)

contours_mama,hierarchy_mama = cv2.findContours(de_mama.copy(), 1, 2)

contours_meatball,hierarchy_meatball = cv2.findContours(meatball_mask.copy(), 1, 2)

contours_mincepork,hierarchy_mincepork = cv2.findContours(mincepork_mask.copy(), 1, 2)

contours_Ipomoea,hierarchy_Ipomoea = cv2.findContours(Ipomoea_mask.copy(), 1, 2)


centres = []

for i in range(len(contours_mama)):
  moments_mama = cv2.moments(contours_mama[i])
  cx = int(moments_mama['m10'] / moments_mama['m00'])
  cy = int(moments_mama['m01'] / moments_mama['m00'])
  area_mama = moments_mama['m00']

  if area_mama > min_object_area:
    centres.append((cx,cy))
    cv2.circle(image_bgr, (cx, cy), 3, (255, 0, 0), -1)
    cv2.putText(image_bgr, (str(cx) + " , " + str(cy)), (cx - 40, cy - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(image_bgr, "MAMA", (cx - 20, cy + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0),2)
    cv2.drawContours(image_bgr, contours_mama, -1, (0, 255, 0), 2)

for j in range(len(contours_mincepork)):
  moments_mincepork = cv2.moments(contours_mincepork[j])
  cx1 = int(moments_mincepork['m10'] / moments_mincepork['m00'])
  cy1 = int(moments_mincepork['m01'] / moments_mincepork['m00'])

  area_mincepork = moments_mincepork['m00']

  if area_mincepork > min_object_area:
    cv2.circle(image_bgr, (cx1, cy1), 3, (255, 0, 0), -1)
    cv2.putText(image_bgr, (str(cx1) + " , " + str(cy1)), (cx1 - 40, cy1 - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(image_bgr, "mincepork", (cx1 - 20, cy1 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0),2)
    cv2.drawContours(image_bgr, contours_mincepork, -1, (0, 0, 255), 2)

for i in range(len(contours_meatball)):
  moments_meatball = cv2.moments(contours_meatball[i])
  cx = int(moments_meatball['m10'] / moments_meatball['m00'])
  cy = int(moments_meatball['m01'] / moments_meatball['m00'])
  area_meatball = moments_meatball['m00']

  if area_meatball > min_object_area:
    centres.append((cx,cy))
    cv2.circle(image_bgr, (cx, cy), 3, (255, 0, 0), -1)
    cv2.putText(image_bgr, (str(cx) + " , " + str(cy)), (cx - 40, cy - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(image_bgr, "meatball", (cx - 20, cy + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0),2)
    cv2.drawContours(image_bgr, contours_meatball, -1, (0, 255, 0), 2)


cv2.imshow('image_original', image_bgr)
cv2.imshow('mask_image', mama_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()


