# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:38:27 2016

@author: Milos
"""

import notebookOperacije as  my

# TODO - IMAGE PROCESSING
# ucitavanje digitalne slike
img_color = my.load_image('images/stop15.jpg')
my.plt.figure(1)
my.display_image('Ucitavanje digitalne slike', img_color)

# formiranje grayscale slike
img_grayscale = my.image_gray((img_color))
my.plt.figure(2)
my.display_image('Formiranje grayscale slike', img_grayscale)

# formiranje binarne slike
img_bin = my.image_bin_adaptive(img_grayscale)
my.plt.figure(3)
my.display_image('Formiranje binarne slike', img_bin)

# uklanjanje šuma sa binarne slike
img_no_noise = my.remove_noiseColor(img_bin)
my.plt.figure(4)
my.display_image('img_bin sa remove_noise', img_no_noise)

# pronalaženje regiona od interesa
img_selected_regions, regions, regions_by_color, regions_signs = my.select_roiV3(img_color.copy(), img_no_noise, 'appRun')
print '\nBroj prepoznatih regiona (regions):', len(regions)
print 'Broj prepoznatih regiona (regions_by_color):', len(regions_by_color)
print 'Broj prepoznatih regiona (regions_signs):', len(regions_signs)
my.plt.figure(5)
my.display_image('img_selected_regions', img_selected_regions)

'''
# koliko regiona je odgovarajuće boje
regions_signs = []
my.findRegionsWithColor(img_color.copy(), regions_color, regions_signs)
print '\nfindRegionsWithColor -> len(regions_signs)=', len(regions_signs)
'''

'''
# roiv4
img_selected_regions, signs = my.select_roiV4(img_color.copy(), img_no_noise)
ind = 0
for sign in signs:
    my.display_image_small('signs_roiV4_'+str(ind), signs[ind])
    ind = ind + 1
'''

