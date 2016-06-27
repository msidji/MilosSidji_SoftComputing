# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 15:30:21 2016

@author: Milos
"""
import notebookOperacije as  my
import neuralNetwork as nn
import numpy as np

# TODO - NEURAL NETWORK TRAIN
# obučavanje neuronske mreže
image_original_obucavanje = my.load_image('images/obucavajuciSkup12.jpg')
image_obucavanje = my.remove_noise(my.image_bin(my.image_gray(image_original_obucavanje)))

img_selected_regions_obucavanje, regions_obucavanje, regions_color_obucavanje, regions_signs_obucavnje = my.select_roiV3(image_original_obucavanje.copy(), image_obucavanje, 'TRAIN')
my.plt.figure(3)
my.display_image('img_selected_regions_obucavanje', img_selected_regions_obucavanje)

inputs_obucavanje = nn.prepare_for_ann(regions_obucavanje)
'''
#signs_alphabet = ['Obavezno zaustavljanje', 'Zabrana saobraćaja u oba smera']
signs_alphabet = {}
for x in range(0, 8):
    signs_alphabet[x] = str((x+1)*10)
    #print "We're on time %d" % (signs_alphabet[x])
'''
signs_alphabet = ['opasnost na putu', 'ogranicenje 30', 'obrnuti trougao', 'stop', 'zabrenjo oba smera', 'ogranicenje 40', 'zabranjeno polukruzno', 'obavezan smer desno', 'pesacki prelaz']
outputs_obucavanje = nn.convert_output(signs_alphabet)

print '\nlen(inputs_obucavanje)=', len(inputs_obucavanje), ' len(outputs_obucavanje)=', len(outputs_obucavanje)
ann = nn.create_ann()
ann = nn.train_ann(ann, inputs_obucavanje, outputs_obucavanje)


# TODO - NEURAL NETWORK PREDICT
# predikcija na osnovu obučene neuronske mreže
print '\n\nPREDIKCIJA ***\n\n'
image_test_original = my.load_image('images_test/blue11.jpg')
image_test = my.remove_noise(my.image_bin(my.image_gray(image_test_original)))

img_selected_regions_test, regions_test, regions_by_color_test, regions_signs_test = my.select_roiV3(image_test_original.copy(), image_test, 'PREDICT')

inputs_test = nn.prepare_for_ann(regions_by_color_test)
results_test = ann.predict(np.array(inputs_test, np.float32))
print '\nresults_test=\n', results_test
print nn.display_result_ann(results_test, signs_alphabet)

print '\nBroj prepoznatih regiona (regions_test):', len(regions_test)
print 'Broj prepoznatih regiona (regions_by_color_test):', len(regions_by_color_test)
print 'Broj prepoznatih regiona (regions_signs_test):', len(regions_signs_test)
my.plt.figure(5)
my.display_image('img_selected_regions_test', img_selected_regions_test)
