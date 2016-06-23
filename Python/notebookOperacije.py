# -*- coding: utf-8 -*-

#*****************************************************
#import potrebnih biblioteka
import cv2
import collections
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from scipy.spatial import distance

# k-means
from sklearn.cluster import KMeans

# keras
from keras.models import Sequential
from keras.layers.core import Dense,Activation
from keras.optimizers import SGD

import matplotlib.pylab as pylab
#pylab.rcParams['figure.figsize'] = 16, 12 # za prikaz većih slika i plotova, zakomentarisati ako nije potrebno

#*****************************************************
#Funkcionalnost implementirana u V1
def load_image(path):
    return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
def image_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
def image_bin(image_gs):
    ret,image_bin = cv2.threshold(image_gs, 127, 255, cv2.THRESH_BINARY)
    return image_bin
def image_bin_adaptive(image_gs):
    image_bin = cv2.adaptiveThreshold(image_gs, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 35, 10)
    return image_bin
def invert(image):
    return 255-image
def display_image(title, image, color= False):
    #plt.figure(figsize=(5, 8))
    plt.figure(figsize=(8, 11))
    if color:
        plt.title(title)
        plt.imshow(image)
    else:
        plt.title(title)
        plt.imshow(image, 'gray')
def dilate(image):
    #kernel = np.ones((4,4)) # strukturni element 3x3 blok
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    return cv2.dilate(image, kernel, iterations=2)
def erode(image):
    #kernel = np.ones((7,7)) # strukturni element 3x3 blok
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    return cv2.erode(image, kernel, iterations=2)

#*****************************************************
#Funkcionalnost implementirana u V2
def resize_region(region):
    resized = cv2.resize(region,(28,28), interpolation = cv2.INTER_NEAREST)
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

#*****************************************************
# Uklanjanje šuma
def remove_noise(binary_image):
    ret_val = erode(dilate(binary_image))
    #
    #
    ret_val = invert(ret_val)
    #
    #
    return ret_val
    
    

#*****************************************************
# TODO - select_roiV3
# Funkcija za selekciju regiona od interesa v3
def select_roiV3(image_orig, image_bin):
    '''
    Funkcija kao u vežbi 2, iscrtava pravougaonike na originalnoj slici, pronalazi sortiran niz regiona sa slike,
    i dodatno treba da sačuva rastojanja između susednih regiona.
    '''
    img, contours, hierarchy = cv2.findContours(image_bin.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Način određivanja kontura je promenjen na spoljašnje konture: cv2.RETR_EXTERNAL
    regions_dict = {}
    regions_color = []
    image_orig_copy = image_orig.copy()
    for contour in contours: 
        x,y,w,h = cv2.boundingRect(contour)
        region = image_bin[y:y+h+1,x:x+w+1];
        # Proveri da li je region odgovarajuće boje
        region_color = image_orig_copy[y:y+h+1,x:x+w+1];
        regions_color.append(region_color)
        regions_signs = []
        color = []
        color = checkRegionColor(image_orig_copy, region_color, regions_signs)
        # Proširiti regions_dict elemente sa vrednostima boundingRect-a ili samim konturama
        regions_dict[x] = [resize_region(region), (x,y,w,h)]
        cv2.rectangle(image_orig,(x,y),(x+w,y+h),color,3)

    sorted_regions_dict = collections.OrderedDict(sorted(regions_dict.items()))
    sorted_regions = np.array(sorted_regions_dict.values())
    
    sorted_rectangles = sorted_regions[:,1]
    region_distances = [-sorted_rectangles[0][0]-sorted_rectangles[0][2]]
    # Izdvojiti sortirane parametre opisujućih pravougaonika
    # Izračunati rastojanja između svih susednih regiona po x osi i dodati ih u region_distances niz
    for x,y,w,h in sorted_regions[1:-1, 1]:
        region_distances[-1] += x
        region_distances.append(-x-w)
    region_distances[-1] += sorted_rectangles[-1][0]
    
    return image_orig, sorted_regions[:, 0], region_distances, regions_color


# Funkcija za selekciju regiona od interesa v4
def select_roiV4(image_orig, image_bin):
    
    img, contours_borders, hierarchy = cv2.findContours(image_bin.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    contours = []
    contour_angles = []
    contour_centers = []
    contour_sizes = []
    for contour in contours_borders:
        center, size, angle = cv2.minAreaRect(contour)
        xt,yt,h,w = cv2.boundingRect(contour)

        region_points = []
        for i in range (xt,xt+h):
            for j in range(yt,yt+w):
                dist = cv2.pointPolygonTest(contour,(i,j),False)
                if dist>=0 and image_bin[j,i]==255: # da li se tacka nalazi unutar konture?
                    region_points.append([i,j])
        contour_centers.append(center)
        contour_angles.append(angle)
        contour_sizes.append(size)
        contours.append(region_points)
    
    #Postavljanje kontura u vertikalan polozaj
    #contours = rotate_regions(contours, contour_angles, contour_centers, contour_sizes)
    
    #spajanje kukica i kvacica
    #contours = merge_regions(contours)
    
    regions_dict = {}
    for contour in contours:
    
        min_x = min(contour[:,0])
        max_x = max(contour[:,0])
        min_y = min(contour[:,1])
        max_y = max(contour[:,1])

        region = np.zeros((max_y-min_y+1,max_x-min_x+1), dtype=np.int16)
        for point in contour:
            x = point[0]
            y = point[1]
            
             # koordinate tacaka regiona prebaciti u relativne koordinate
            '''Pretpostavimo da gornja leva tačka regiona ima apsolutne koordinate (100,100).
            Ako uzmemo tačku sa koordinatama unutar regiona, recimo (105,105), nakon
            prebacivanja u relativne koordinate tačka bi trebala imati koorinate (5,5) unutar
            samog regiona.
            '''
            region[y-min_y,x-min_x] = 255

        
        regions_dict[min_x] = [resize_region(region), (min_x,min_y,max_x-min_x,max_y-min_y)]
        
    sorted_regions_dict = collections.OrderedDict(sorted(regions_dict.items()))
    sorted_regions = np.array(sorted_regions_dict.values())
    
    sorted_rectangles = sorted_regions[:,1]
    region_distances = [-sorted_rectangles[0][0]-sorted_rectangles[0][2]]
    for x,y,w,h in sorted_regions[1:-1, 1]:
        region_distances[-1] += x
        region_distances.append(-x-w)
    region_distances[-1] += sorted_rectangles[-1][0]
    
    return image_orig, sorted_regions[:, 0], region_distances        
    
#*****************************************************    
                                                    #*****************************************************
#*****************************************************
# cv2.mean (BLUE, GREEN, RED, ignored_value)            
# TODO - findRegionsWithColor
def findRegionsWithColor(image_color, regions_color, regions_signs):
    print '\n>>>findRegionsWithColor'
    ind = 0
    for ind in xrange(len(regions_color)):
        region = regions_color[ind]
        mean_val = cv2.mean(region, mask = None)
        mean_val = map(prettyFloat4, mean_val)
        print '\nmean_val[', ind, ']', '=', mean_val
        
        region_size = isRegionTooSmall(region.shape[0], region.shape[1], image_color.shape[0], image_color.shape[1])
        if  region_size:
            if isRegionRed(ind, region):
                print('FOUND isRegionRed ***')
                regions_signs.append(region)
            elif isRegionBlue(ind, region):
                print('FOUND isRegionBlue ***')     
                regions_signs.append(region)
            elif isRegionWhite(ind, region):
                print('FOUND isRegionWhite ***')
                regions_signs.append(region)
            else:
                print 'H=', str(region.shape[0]), 'W=', str(region.shape[1])
                print('else ---> nije odgovarajuce boje region')
                plt.figure(10+ind)
                display_image('mean_NOT_COLOR_' + str(ind), region)                
        else:
            print 'region size is TOO SMALL'

# TODO - isRegionTooSmall    
def isRegionTooSmall(region_height, region_width, img_height, img_width):
    region_povrsina = region_height * region_width
    img_povrsina = img_height * img_width
    odnos_povrsina = (region_povrsina*100) / float(img_povrsina)

    # bio je 1.1
    if odnos_povrsina > 1.1:
        print 'odnos_povrsina=', format(odnos_povrsina, '.4f'), '\n\tregion_povrsina=', region_povrsina, '\n\timg_povrsina=', img_povrsina
        return True
    else:
        return False

# TODO - isRegionRed    
def isRegionRed(ind, region):
    mean_val = cv2.mean(region, mask = None)
    if mean_val[0] > 115 and mean_val[1] < 150 and mean_val[2] < 150:
        if mean_val[0] > mean_val[1] and mean_val[0] > mean_val[2]:
            if mean_val[0] > 150 or ( mean_val[1] < 100 or mean_val[2] < 100):
                print 'meanRED=[', str(ind), ']=', 'H=', str(region.shape[0]), 'W=', str(region.shape[1])
                
                plt.figure(10+ind)
                display_image('meanR_' + str(ind), region)
                return True
            else:
                return False
                
# TODO - isRegionBlue
def isRegionBlue(ind, region):
    mean_val = cv2.mean(region, mask = None)
    if mean_val[2] > 115 and mean_val[1] < 170 and mean_val[0] < 150:
        if mean_val[2] > mean_val[0] and mean_val[2] > mean_val[1]:
            if mean_val[2] > 150 or ( mean_val[0] < 100 or mean_val[1] < 100):
                print 'meanBLUE[', str(ind), ']=', 'H=', str(region.shape[0]), 'W=', str(region.shape[1])
                
                plt.figure(10+ind)
                display_image('meanB_' + str(ind), region)
                return True
            else:
                return False

# TODO - isRegionWhite
def isRegionWhite(ind, region):
    mean_val = cv2.mean(region, mask = None)
    if mean_val[0] > 180 and mean_val[1] > 140 and mean_val[2] > 140:
        print 'meanWHITE=[', str(ind), ']=', 'H=', str(region.shape[0]), 'W=', str(region.shape[1])
        
        plt.figure(10+ind)
        #display_image('meanW_' + str(ind), region)
        return True
    else:
        return False
        
class prettyFloat4(float):
    def __repr__(self):
        return "%0.4f" % self

# TODO - checkRegionColor
def checkRegionColor(image_color, region_color, regions_signs):
    print '\n>>>checkRegionColor'
    ind = 0
    region = region_color
    mean_val = cv2.mean(region, mask = None)
    mean_val = map(prettyFloat4, mean_val)
    print 'mean_val[', ind, ']', '=', mean_val
    
    region_size = isRegionTooSmall(region.shape[0], region.shape[1], image_color.shape[0], image_color.shape[1])
    if  region_size:
        if isRegionRed(ind, region):
            print('FOUND isRegionRed ***')
            regions_signs.append(region)
            return [255, 0, 0]
        elif isRegionBlue(ind, region):
            print('FOUND isRegionBlue ***')     
            regions_signs.append(region)
            return [0, 0, 255]
        elif isRegionWhite(ind, region):
            print('FOUND isRegionWhite ***')
            regions_signs.append(region)
            return [0, 0, 0]
        else:
            print 'H=', str(region.shape[0]), 'W=', str(region.shape[1])
            print('else ---> nije odgovarajuce boje region')
            plt.figure(10+ind)
            display_image('mean_NOT_COLOR_' + str(ind), region)
            return [160, 32, 240] # purple
    else:
        print 'region size is TOO SMALL'  
        return [0, 255, 0] # green
            
            
            