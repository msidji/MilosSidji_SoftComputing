# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:43:50 2016

@author: Milos
"""

import numpy as np
import cv2

# keras
from keras.models import Sequential
from keras.layers.core import Dense,Activation
from keras.optimizers import SGD

# TODO - V2
# Funkcionalnost implementirana u V2
def resize_region(region):
    resized = cv2.resize(region,(64,64), interpolation = cv2.INTER_NEAREST)
    return resized
def scale_to_range(image):
    return image / 255
def matrix_to_vector(image):
    return image.flatten()
def prepare_for_ann(regions):
    ready_for_ann = []
    for region in regions:
        ready_for_ann.append(matrix_to_vector(scale_to_range(region)))
    return ready_for_ann
def convert_output(outputs):
    return np.eye(len(outputs))
def winner(output):
    return max(enumerate(output), key=lambda x: x[1])[0]

# TODO - create_ann
def create_ann():    
    ann = Sequential()
    # postavljanje slojeva neurona mreže 'ann'
    ann.add(Dense(input_dim=4096, output_dim=128,init="glorot_uniform"))
    ann.add(Activation("sigmoid"))
    ann.add(Dense(input_dim=128, output_dim=5,init="glorot_uniform"))
    ann.add(Activation("sigmoid"))
    return ann
   
# TODO - train_ann
def train_ann(ann, X_train, y_train):
    X_train = np.array(X_train, np.float32)
    y_train = np.array(y_train, np.float32)
   
    # definisanje parametra algoritma za obucavanje
    sgd = SGD(lr=0.01, momentum=0.9)
    ann.compile(loss='mean_squared_error', optimizer=sgd)

    # obucavanje neuronske mreze
    ann.fit(X_train, y_train, nb_epoch=500, batch_size=1, verbose = 0, shuffle=False, show_accuracy = False) 
      
    return ann

# TODO - display_result
def display_result_ann(outputs, alphabet):
    print '\n>>>display_result_ann:'
    '''
    Args:
        outputs: niz izlaza iz neuronske mreže.
        alphabet: niz karaktera koje je potrebno prepoznati
    Return:
        Vraća formatiran string
    '''
    #result = '0. ' + alphabet[winner(outputs[0])]
    result = ''
    for idx, output in enumerate(outputs[0:,:]):
        # Iterativno dodavati prepoznate elemente kao u vežbi 2, alphabet[winner(output)]
        result += '\n' + str(idx) + '. '
        result += alphabet[winner(output)]
        
    return result
    
# TODO - display_result_reverse_ann
def display_result_reverse_ann(outputs, alphabet):
    print '\n>>>display_result_reverse_ann:'
    '''
    Args:
        outputs: niz izlaza iz neuronske mreže.
        alphabet: niz karaktera koje je potrebno prepoznati
    Return:
        Vraća formatiran string
    '''
    #result = '0. ' + alphabet[winner(outputs[0])]
    result = ''
    ind = 0
    for idx, output in reversed(list(enumerate(outputs[0:,:]))):
        # Iterativno dodavati prepoznate elemente kao u vežbi 2, alphabet[winner(output)]
        result += '\n' + str(ind) + '. '
        result += alphabet[winner(output)]
        ind = ind + 1
        
    return result