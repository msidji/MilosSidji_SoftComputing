# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 01:34:15 2016

@author: Milos
"""

import notebookOperacije as my
import cv2
import numpy as np

# TODO - IMAGE PROCESSING
img_path = 'images/stop12.jpg'
# ucitavanje digitalne slike
img_color = my.load_image(img_path)
my.plt.figure(1)
my.display_image('Ucitavanje digitalne slike', img_color)

# formiranje hsv slikes
img_hsv = my.load_imageHSV(img_path)
my.plt.figure(5)
my.display_image('img_hsv', img_hsv)

    # define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask_blue1 = cv2.inRange(img_hsv, lower_blue, upper_blue)

    # define range of red color in HSV
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask_red1 = cv2.inRange(img_hsv, lower_red, upper_red)

    # define range of red color in HSV
lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])
mask_red2 = cv2.inRange(img_hsv, lower_red, upper_red)

lower_white = np.array([0,0,100])
upper_white = np.array([150,250,250])
mask_white1 = cv2.inRange(img_hsv, lower_white, upper_white)

lower_yellow = np.array([20,100,100])
upper_yellow = np.array([40,255,255])
mask_yellow1 = cv2.inRange(img_hsv, lower_yellow, upper_yellow)

lower_black = np.array([0,0,0])
upper_black = np.array([179,50,50])
mask_black1 = cv2.inRange(img_hsv, lower_black, upper_black)

mask =  mask_red1 + mask_red2 #+ mask_white1 #+ mask_blue1# + mask_black1# + mask_yellow1

output_hsv = img_hsv.copy()
output_hsv[np.where(mask==0)] = 0
my.plt.figure(6)
my.display_image('output_hsv', output_hsv)

    # Threshold the HSV image to get only red colors
#img_mask = cv2.inRange(img_hsv, lower_red, upper_red)
#my.plt.figure(7)
#my.display_image('img_mask', img_mask)

    # Bitwise-AND mask and original image
img_result = cv2.bitwise_and(img_color.copy(),img_color.copy(), mask=mask)
my.plt.figure(8)
my.display_image('img_result', img_result)

#--------------------------
# formiranje grayscale slike
img_grayscale = my.image_gray((img_result))
my.plt.figure(2)
my.display_image('Formiranje grayscale slike', img_grayscale)

# formiranje binarne slike
img_bin = my.image_bin(img_grayscale)
my.plt.figure(3)
my.display_image('Formiranje binarne slike', img_bin)

# uklanjanje šuma sa binarne slike
img_no_noise = my.invert(my.remove_noise(img_bin))
my.plt.figure(4)
my.display_image('img_bin sa remove_noise', img_no_noise)
#--------------------------

img_selected_regions, regions, regions_by_color = my.select_roiShapes(img_color.copy(), img_no_noise, 'appRunShapes')
print '\nBroj prepoznatih regiona (regions):', len(regions)
print 'Broj prepoznatih regiona (regions_by_color):', len(regions_by_color)
my.plt.figure(9)
my.display_image('img_selected_regions', img_selected_regions)


