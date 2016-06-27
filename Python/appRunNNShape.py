# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 06:15:17 2016

@author: Milos
"""
import neuralNetwork as nn
import numpy as np
import appRunShapesTrain as shapesTrain
import appRunShapesPredict as shapesPredict

# TODO - NEURAL NETWORK TRAIN
# obučavanje neuronske mreže
#img_selected_regions_obucavanje, regions_obucavanje, regions_color_obucavanje = my.select_roiShapes(shapesTrain.img_color.copy(), shapesTrain.img_no_noise, 'TRAIN')

inputs_obucavanje = nn.prepare_for_ann(shapesTrain.regions)
signs_alphabet = ['zabranjeno oba smera', 'stop', 'ogranicenje 40', 'zabranjeno polukruzno', 'pesacki prelaz']
outputs_obucavanje = nn.convert_output(signs_alphabet)

print '\nlen(inputs_obucavanje)=', len(inputs_obucavanje), ' len(outputs_obucavanje)=', len(outputs_obucavanje)
ann = nn.create_ann()
ann = nn.train_ann(ann, inputs_obucavanje, outputs_obucavanje)


# TODO - NEURAL NETWORK PREDICT
# predikcija na osnovu obučene neuronske mreže
print '\n\nPREDIKCIJA ***\n\n'
#img_selected_regions_test, regions_test, regions_by_color_test = my.select_roiShapes(shapesPredict.img_color.copy(), shapesPredict.img_no_noise, 'PREDICT')

inputs_test = nn.prepare_for_ann(shapesPredict.regions)
results_test = ann.predict(np.array(inputs_test, np.float32))
print '\nresults_test=\n', results_test
print nn.display_result_reverse_ann(results_test, signs_alphabet)
