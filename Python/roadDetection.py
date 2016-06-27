# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 04:30:50 2016

@author: Milos
"""
import notebookOperacije as my
import numpy as np
import cv2

def canny(imgray):
    # zamagljivanje slike pomoćću Gaussian filtera, korisno za uklanjanje šuma
    # zapravo uklnja visoke frekvencije (šumove, ivice) sa slike
    img_gaussian = cv2.GaussianBlur(imgray, (5,5), 200)
    my.display_image('3. gaussian', img_gaussian)

    canny_low = 50 #5
    canny_high = 200 #150

    # pronalazi ivice na slici pomoću Canny algoritma
    # pomoću 1. i 2. threshold-a za histesisnu proceduru
    img_canny = cv2.Canny(img_gaussian,canny_low,canny_high)
    my.display_image('4. canny', img_canny)

    return img_canny

def filtering(imgray):
    img_canny = canny(imgray)

    # Houghova linijska tranformacija za detektovanje pravih linija
    hough_thresh = 50 #50
    lines = cv2.HoughLines(img_canny,1,np.pi/180,hough_thresh)
    print 'lines.shape=',lines.shape

    h = img_color.shape[0]/3
    print 'h=',h

    # računnje i iscrtravanje Hough-ovih linija
    for i in range(0,3):
        for rho,theta in lines[i]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            cv2.line(img_result,(x1,y1),(x2,y2),(255,0,0),5)
    
#*****************************************************
    
# TODO - run
img_color = cv2.imread('images_test/put11.jpg')
img_result = img_color.copy()
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

filtering(img_gray)

my.display_image('1. original', img_color)
my.display_image('2. gray', img_gray)
my.display_image('5. result', img_result)

