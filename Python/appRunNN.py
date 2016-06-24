# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 15:30:21 2016

@author: Milos
"""
import notebookOperacije as  my
import neuralNetwork as nn
import numpy as np

# TODO - NEURAL NETWORK
# obucavanje neuronske mreze
image_original_obucavanje = my.load_image('images/obucavajuciSkup4.jpg')
image_obucavanje = my.remove_noise(my.image_bin(my.image_gray(image_original_obucavanje)))

selected_test_obucavanje, signs_obucavanje, regions_color_obucavanje = my.select_roiV3(image_original_obucavanje.copy(), image_obucavanje)

#print signs_obucavanje[0].shape ,'shape '

inputs_obucavanje = nn.prepare_for_ann(signs_obucavanje)
signs_alphabet = ['stop', 'neki_znak']
outputs_obucavanje = nn.convert_output(signs_alphabet)

print '\nlen(inputs_obucavanje)=', len(inputs_obucavanje), ' len(outputs_obucavanje)=', len(outputs_obucavanje)
ann = nn.create_ann()
ann = nn.train_ann(ann, inputs_obucavanje, outputs_obucavanje)

# predikcija na osnovu obucene neuronske mreze
image_test_original = my.load_image('images/stop6.jpg')
image_test = my.remove_noise(my.image_bin(my.image_gray(image_test_original)))

selected_regions_test, signs_test, regions_color_test = my.select_roiV3(image_test_original.copy(), image_test)

inputs_test = nn.prepare_for_ann(signs_test)
results_test = ann.predict(np.array(inputs_test, np.float32))
print nn.display_result_ann(results_test, signs_alphabet)
print '\nresults_test=', results_test