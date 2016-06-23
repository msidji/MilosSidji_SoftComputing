# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:38:27 2016

@author: Milos
"""

import notebookOperacije as  my

#*****************************************************
# ucitavanje digitalne slike
img_color = my.load_image('images/all1.jpg')

# formiranje grayscale slike
img_grayscale = my.image_gray((img_color))

# formiranje binarne slike
img_bin = my.image_bin_adaptive(img_grayscale)

my.plt.figure(1)
my.display_image('Ucitavanje digitalne slike', img_color)

my.plt.figure(2)
my.display_image('Formiranje grayscale slike', img_grayscale)

my.plt.figure(3)
my.display_image('Formiranje binarne slike', img_bin)

img_no_noise = my.remove_noise(img_bin)
my.plt.figure(4)
my.display_image('img_bin sa remove_noise', img_no_noise)

img_selected_regions, letters, region_distances, regions_color = my.select_roiV3(img_color.copy(), img_no_noise)
print '\nBroj prepoznatih regiona:', len(letters)

my.plt.figure(5)
my.display_image('img_selected_regions', img_selected_regions)

#regions_signs = []
#my.findRegionsWithColor(img_color.copy(), regions_color, regions_signs)
#print '\nlen(regions_signs)=', len(regions_signs)

