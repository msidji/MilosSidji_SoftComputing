# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:17:51 2016

@author: Milos
"""

import notebookOperacije as my
import theano
import numpy
import scipy
import cv2
import numpy as np

n = [1.290192, 3.0002, 22.119199999999999, 3.4110999999999998, 12]
n = map(my.prettyFloat4, n)

x = 1.33333445
print 'xx', n, '\nx=', my.prettyFloat4(x)
print n.index(12)

#theano.test()
#numpy.test()
#scipy.test()
signs_alphabet = {}
for x in range(0, 35):
    signs_alphabet[x] = (x+1)*10
    print "We're on time %d" % (signs_alphabet[x])

img=cv2.imread("images/oblici1.jpg")
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# lower mask (0-10)
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

# upper mask (170-180)
lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)


    # define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask2 = cv2.inRange(img_hsv, lower_blue, upper_blue)

    # define range of blue color in HSV
lower_white = np.array([20,100,100])
upper_white = np.array([40,255,255])
mask3 = cv2.inRange(img_hsv, lower_white, upper_white)



# join my masks
mask = mask0+mask1+mask2+mask3

# set my output img to zero everywhere except my mask
output_img = img.copy()
output_img[np.where(mask==0)] = 0

# or your HSV image, which I *believe* is what you want
output_hsv = img_hsv.copy()
output_hsv[np.where(mask==0)] = 0
my.display_image('output_hsv', output_hsv)

white = np.uint8([[[0,0,0 ]]])
hsv_green = cv2.cvtColor(white,cv2.COLOR_BGR2HSV)
print hsv_green