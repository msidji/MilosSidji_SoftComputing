# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:38:27 2016

@author: Milos
"""

import notebookOperacije as  my
import neuralNetwork as nn
import numpy as np


#*****************************************************
# ucitavanje digitalne slike
#img_color = my.load_image('images/ulica4.jpg')
#
## formiranje grayscale slike
#img_grayscale = my.image_gray((img_color))
#
## formiranje binarne slike
#img_bin = my.image_bin_adaptive(img_grayscale)
#
#my.plt.figure(1)
#my.display_image('Ucitavanje digitalne slike', img_color)
#
#my.plt.figure(2)
#my.display_image('Formiranje grayscale slike', img_grayscale)
#
#my.plt.figure(3)
#my.display_image('Formiranje binarne slike', img_bin)
#
#img_no_noise = my.remove_noise(img_bin)
#my.plt.figure(4)
#my.display_image('img_bin sa remove_noise', img_no_noise)
#
#img_selected_regions, signs, region_distances, regions_color = my.select_roiV3(img_color.copy(), img_no_noise)
#print '\nBroj prepoznatih regiona:', len(signs)
#
#my.plt.figure(5)
#my.display_image('img_selected_regions', img_selected_regions)

#regions_signs = []
#my.findRegionsWithColor(img_color.copy(), regions_color, regions_signs)
#print '\nlen(regions_signs)=', len(regions_signs)



#*****************************************************
# TODO - NEURAL NETWORK
# obucavanje neuronske mreze
image_original_obucavanje = my.load_image('images/obucavajuciSkup3.jpg')
image_obucavanje = my.remove_noise(my.image_bin(my.image_gray(image_original_obucavanje)))

selected_test_obucavanje, signs_obucavanje, region_distances_obucavanje, regions_color_obucavanje = my.select_roiV3(image_original_obucavanje.copy(), image_obucavanje)

inputs_obucavanje = nn.prepare_for_ann(signs_obucavanje)
signs_alphabet = ['stop']
outputs_obucavanje = nn.convert_output(signs_alphabet)

print '\nlen(inputs_obucavanje)=', len(inputs_obucavanje), ' len(outputs_obucavanje)=', len(outputs_obucavanje)
ann = nn.create_ann()
ann = nn.train_ann(ann, inputs_obucavanje, outputs_obucavanje)

## predikcija na osnovu obucene neuronske mreze
#image_test_original = my.load_image('images/stop1.jpg')
#image_test = my.remove_noise(my.image_bin(my.image_gray(image_test_original)))
#
#selected_regions_test, signs_test, region_distances_test, regions_color_test = my.select_roiV3(image_test_original.copy(), image_test)
#
#inputs_test = nn.prepare_for_ann(signs_test)
#results_test = ann.predict(np.array(inputs_test, np.float32))
#print my.display_result(results_test, signs_alphabet)


