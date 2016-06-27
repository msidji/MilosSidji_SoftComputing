# -*- coding: utf-8 -*-

#*****************************************************
#import potrebnih biblioteka
import cv2
import collections
import numpy as np
#import scipy as sc
import matplotlib.pyplot as plt
#from scipy.spatial import distance
import math

#*****************************************************
# TODO - V1
# Funkcionalnost implementirana u V1
def load_image(path):
    return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)    
def load_imageHSV(path):
    return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2HSV)    
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
def display_image_small(title, image, color= False):
    #plt.figure(figsize=(5, 8))
    plt.figure(figsize=(3, 5))
    if color:
        plt.title(title)
        plt.imshow(image)
    else:
        plt.title(title)
        plt.imshow(image, 'gray')
def dilate(image):#POVECAVA BELE
    #kernel = np.ones((3,3)) # strukturni element 3x3 blok
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
    return cv2.dilate(image, kernel, iterations=3)
def erode(image): #UKLANJA  BELE
    #kernel = np.ones((3,3)) # strukturni element 3x3 blok
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(2,2))
    return cv2.erode(image, kernel, iterations=1)
def resize_region(region):
    resized = cv2.resize(region,(64,64), interpolation = cv2.INTER_NEAREST)
    return resized

# Uklanjanje šuma
def remove_noise(binary_image):
    ret_val = erode(dilate(binary_image))
    ret_val = invert(ret_val)
    return ret_val
    
#*****************************************************
# TODO - select_roiV3
# Funkcija za selekciju regiona od interesa v3
def select_roiV3(image_orig, image_bin, poziva):
    '''
    Funkcija kao u vežbi 2, iscrtava pravougaonike na originalnoj slici, pronalazi sortiran niz regiona sa slike,
    i dodatno treba da sačuva rastojanja između susednih regiona.
    '''
    img, contours, hierarchy = cv2.findContours(image_bin.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
    regions_dict = {}
    regions_dict_by_color = {}
    regions_signs = []    
    image_orig_copy = image_orig.copy()
    ind = 0
    for contour in contours: 
        x,y,w,h = cv2.boundingRect(contour)
        region = image_bin[y:y+h+1,x:x+w+1];
        
        # dodaj region u boji u listu
        region_color = image_orig_copy[y:y+h+1,x:x+w+1];
        print '\ny=', y, ' x=', x
        color, isSign = checkRegionColor(image_orig_copy, region_color, regions_signs, ind, poziva)

        # proširiti regions_dict elemente sa vrednostima boundingRect-a ili samim konturama
        regions_dict[y] = [resize_region(region), (x,y,w,h)]
        if isSign:
            regions_dict_by_color[y] = [resize_region(region), (x,y,w,h)]
        
        cv2.rectangle(image_orig,(x,y),(x+w,y+h),color,3)
        ind = ind + 1

    sorted_regions_dict = collections.OrderedDict(sorted(regions_dict.items()))
    sorted_regions = np.array(sorted_regions_dict.values())
    
    sorted_regions_dict_by_color = collections.OrderedDict(sorted(regions_dict_by_color.items(), reverse=True))
    sorted_regions_by_color = np.array(sorted_regions_dict_by_color.values())        
    
    return image_orig, sorted_regions[:, 0], sorted_regions_by_color[:, 0], regions_signs

# TODO - select_roiShapes
def select_roiShapes(image_orig, image_bin, poziva):
    img, contours, hierarchy = cv2.findContours(image_bin.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    regions_dict = {}
    regions_color=[]
    
    maxArea = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > maxArea:
            maxArea = area
    for contour in contours: 
        x,y,w,h = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)
        if((area > 300) and (checkCircle(contour) or checkTriangle(contour) or checkSquare(contour) or checkOktagon(contour)) and (area*3 > maxArea)):
            region = image_bin[y:y+h+1,x:x+w+1]
            region_color = image_orig[y:y+h+1,x:x+w+1];
            regions_color.append(region_color)
            regions_dict[y] = [resize_region(region), (x,y,w,h)]
            
            cv2.rectangle(image_orig,(x,y),(x+w,y+h),(0,255,0),3)

    sorted_regions_dict = collections.OrderedDict(sorted(regions_dict.items()))
    sorted_regions = np.array(sorted_regions_dict.values())

    return image_orig, sorted_regions[:,0], regions_color

# TODO - select_roiV4
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
    
    # postavljanje kontura u vertikalan polozaj
    contours = rotate_regions(contours, contour_angles, contour_centers, contour_sizes)
    
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
        
    return image_orig, sorted_regions[:, 0]

# TODO - Rotiranje regiona
def rotate_regions(contours,angles,centers,sizes):
    '''Funkcija koja vrši rotiranje regiona oko njihovih centralnih tačaka
    Args:
        contours: skup svih kontura [kontura1, kontura2, ..., konturaN]
        angles:   skup svih uglova nagiba kontura [nagib1, nagib2, ..., nagibN]
        centers:  skup svih centara minimalnih pravougaonika koji su opisani 
                  oko kontura [centar1, centar2, ..., centarN]
        sizes:    skup parova (height,width) koji predstavljaju duzine stranica minimalnog
                  pravougaonika koji je opisan oko konture [(h1,w1), (h2,w2), ...,(hN,wN)]
    Return:
        ret_val: rotirane konture'''
    ret_val = []
    for idx, contour in enumerate(contours):
                
        angle = angles[idx]
        cx,cy = centers[idx]
        height, width = sizes[idx]
#        if width<height:
#            angle+=90
            
        # Rotiranje svake tačke regiona oko centra rotacije
        alpha = np.pi/2 - abs(np.radians(angle))
        region_points_rotated = np.ndarray((len(contour), 2), dtype=np.int16)
        for i, point in enumerate(contour):
            x = point[0]
            y = point[1]
            
            # izračunati koordinate tačke nakon rotacije
            rx = np.sin(alpha)*(x-cx) - np.cos(alpha)*(y-cy) + cx
            ry = np.cos(alpha)*(x-cx) + np.sin(alpha)*(y-cy) + cy
                        
            region_points_rotated[i] = [rx,ry]
        ret_val.append(region_points_rotated)

    return ret_val

    
#*****************************************************    
                                                    #*****************************************************
#*****************************************************
    
    
# cv2.mean (BLUE, GREEN, RED, ignored_value)            
# TODO - Pronlaženje boje svakog regiona u listi regioni
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
                #display_image_small('mean_NOT_COLOR_' + str(ind), region)                
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
def isRegionRed(ind, region, poziva):
    mean_val = cv2.mean(region, mask = None)
    if mean_val[0] > 115 and mean_val[1] < 150 and mean_val[2] < 150:
        if mean_val[0] > mean_val[1] and mean_val[0] > mean_val[2]:
            if mean_val[0] > 150 or ( mean_val[1] < 100 or mean_val[2] < 100):
                print poziva,'_meanRED[', str(ind), ']=', 'H=', str(region.shape[0]), 'W=', str(region.shape[1])
                
                plt.figure(10+ind)
                display_image_small(poziva + '_meanR_' + str(ind), region)
                return True
            else:
                return False
                
# TODO - isRegionBlue
def isRegionBlue(ind, region, poziva):
    mean_val = cv2.mean(region, mask = None)
    if mean_val[2] > 115 and mean_val[1] < 170 and mean_val[0] < 150:
        if mean_val[2] > mean_val[0] and mean_val[2] > mean_val[1]:
            if mean_val[2] > 150 or ( mean_val[0] < 100 or mean_val[1] < 100):
                print poziva,'_meanBLUE[', str(ind), ']=', 'H=', str(region.shape[0]), 'W=', str(region.shape[1])
                
                plt.figure(10+ind)
                display_image_small(poziva + '_meanB_' + str(ind), region)
                return True
            else:
                return False

# TODO - isRegionWhite
def isRegionWhite(ind, region, poziva):
    mean_val = cv2.mean(region, mask = None)
    if mean_val[0] > 180 and mean_val[1] > 140 and mean_val[2] > 140:
        print poziva,'_meanWHITE[', str(ind), ']=', 'H=', str(region.shape[0]), 'W=', str(region.shape[1])
        
        plt.figure(10+ind)
        display_image_small(poziva + '_meanW_' + str(ind), region)
        return True
    else:
        return False
        
class prettyFloat4(float):
    def __repr__(self):
        return "%0.4f" % self

# TODO - Određivanje boje regiona
def checkRegionColor(image_color, region_color, regions_signs, index, poziva):
    print '>>>checkRegionColor'
    ind = index
    region = region_color
    mean_val = cv2.mean(region, mask = None)
    mean_val = map(prettyFloat4, mean_val)
    print 'mean_val[', ind, ']', '=', mean_val
    
    region_size = isRegionTooSmall(region.shape[0], region.shape[1], image_color.shape[0], image_color.shape[1])
    if  region_size:
        if isRegionRed(ind, region, poziva):
            print('FOUND isRegionRed ***')
            regions_signs.append(region)
            return [255, 0, 0], True
        elif isRegionBlue(ind, region, poziva):
            print('FOUND isRegionBlue ***')     
            regions_signs.append(region)
            return [0, 0, 255], True
        elif isRegionWhite(ind, region, poziva):
            print('FOUND isRegionWhite ***')
            regions_signs.append(region)
            return [0, 0, 0], True
        else:
            print 'H=', str(region.shape[0]), 'W=', str(region.shape[1])
            print('else ---> nije odgovarajuce boje region')
            plt.figure(10+ind)
            #display_image_small('mean_NOT_COLOR_' + str(ind), region)
            return [160, 32, 240], False # purple
    else:
        print 'region size is TOO SMALL'  
        return [0, 255, 0], False # green


# TODO - getAngle
def getAngle(p1,p2,p3):
    v12=np.array([p2[0]-p1[0],p2[1]-p1[1]])
    v13=np.array([p3[0]-p1[0],p3[1]-p1[1]])
    
    scalarProduct=np.dot(v12,v13)
    v12_modul=np.sqrt((v12*v12).sum())
    v13_modul=np.sqrt((v13*v13).sum())
    
    return np.arccos((scalarProduct)/(v12_modul*v13_modul))*(180/math.pi)   
  
# cv2.arcLength -> obim
# cv2.approxPolyDP -> aproksimacija poligona  
# TODO - checkCircle  
def checkCircle(contour):    
    #print "aproksimacija circle"    
    epsilon = 0.008*cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,epsilon,True)
    #print 'len(approx)=',len(approx)
    #print 'approx=',approx

    if len(approx) >=12 and not(cv2.isContourConvex(contour)) and len(approx)<20 :
        return True
    else:
        return False   
  
# TODO - checkTriangle  
def checkTriangle(contour):
    #print "aproximacija trougao"
    epsilon = 0.045*cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,epsilon,True)    
    #print 'len(approx)=',len(approx)
    #print 'approx=',approx

    if len(approx) == 3 or len(approx) == 5:
        alpha1=getAngle(approx[0][0],approx[1][0],approx[2][0])
        alpha2=getAngle(approx[1][0],approx[0][0],approx[2][0])
        alpha3=getAngle(approx[2][0],approx[0][0],approx[1][0])
        #print 'alpha1=',alpha1
        #print 'alpha2=',alpha2
        #print 'alpha3=',alpha3
        if( alpha1>40 and alpha1<78 and alpha2>40 and alpha2<78 and alpha3 >40 and alpha3 <78):
            #print 'trueeeeeeeeee checkTriangle'
            return True
        else:
            return False
    else: 
        return False           

# TODO - checkSquare        
def checkSquare(contour):    
    #print "aproksimacija square"
    epsilon = 0.015*cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,epsilon,True)
    #print 'approx=',approx
    
    if len(approx) == 4:
        alpha1=getAngle(approx[0][0],approx[1][0],approx[3][0])
        alpha2=getAngle(approx[1][0],approx[0][0],approx[2][0])
        alpha3=getAngle(approx[2][0],approx[1][0],approx[3][0])
        alpha4=getAngle(approx[3][0],approx[0][0],approx[2][0])
        
        if alpha1>85.0 and alpha1 <95.0 and alpha2>85.0 and alpha2 <95.0 and alpha3>85.0 and alpha3 <95.0 and alpha4>85.0 and alpha4 <95.0:
            return True
        else:
            return False
    else:
        return False    
            
# TODO - checkOktagon
def checkOktagon(contour):
    #print "aproksimacija octagon"
    epsilon = 0.01*cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,epsilon,True)
    #print 'approx=',approx
    
    if len(approx) == 8:
        alpha=getAngle(approx[1][0],approx[2][0],approx[0][0])
       
        if alpha>100.0 and alpha <140.0 :           
            return True
        else:
            return False
    else:
        return False                  
            
            
            