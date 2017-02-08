import numpy as np
import cv2
from matplotlib import pyplot as plt

image_bgr = cv2.imread('meatball.jpg',1)

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([image_bgr], [i], None, [256], [0, 256])
    cv2.imshow('meatball',image_bgr)
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()