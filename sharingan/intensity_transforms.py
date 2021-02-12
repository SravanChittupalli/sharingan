import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
# Max intensity level
L = 256

def negative(img):
    '''
    @brief: Sent image goes through intensity transform s = L-1-r
        s = output pixels
        L = max intensity level (assumed 255)
        r = input pixel intensities

    @parameters: 
        img = image array (RGB or greyscale)
    
    @output:
        image that is negative of img(input image)
    '''
    # if a 3rd channel is found then convert 
    # [TODO] Use your own function to go between different color spaces
    try:
        if img.shape[2] == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except:
        pass

    for row in range (img.shape[0]):
        for col in range (img.shape[1]):
            img[row][col] = L - 1 - img[row][col]
    
    return img

def log_transform(img, power):
    '''
    @brief: Sent image goes through log transform s = c log(1+L)**power
        c = scaling factor..so that max output of log(1+L) = 255
            Higher values of input levels are mapped to a narrower range in the output.
        s = output pixels
        L = max intensity level (assumed 255)
        r = input pixel intensities
        power = power>0; power < 1 then the lower intensities are expanded; power > 1 brighter pixel intensities are expanded

    @parameters: 
        img = image array (RGB or greyscale)
    
    @output:
        log transformed image of input
    '''
    # if a 3rd channel is found then convert 
    # [TODO] Use your own function to go between different color spaces
    try:
        if img.shape[2] == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except:
        pass
    
    # scaling factor to map output to [0, 255]
    c = L/math.log(1+L)**power

    for row in range (img.shape[0]):
        for col in range (img.shape[1]):
            img[row][col] = c*math.log(1+img[row][col])**power
    return img

def gamma_transform(img, gamma):
    '''
    @brief: Sent image goes through log transform s = c*r**gamma
        c = scaling factor..so that max output of r**gamma = 255
            Higher values of input levels are mapped to a narrower range in the output if gamma is < 1 and > 0.
        s = output pixels
        L = max intensity level (assumed 255)
        r = input pixel intensities
        gamma = gamma>0; gamma < 1 then the lower intensities are expanded; gamma > 1 brighter pixel intensities are expanded

    @parameters: 
        img = image array (RGB or greyscale)
    
    @output:
        gamma transformed image of input
    '''
    # if a 3rd channel is found then convert 
    # [TODO] Use your own function to go between different color spaces
    try:
        if img.shape[2] == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except:
        pass
    
    # scaling factor to map output to [0, 255]
    c = L/(L**gamma)

    # plot for gamma > 3 to understand
    # 255**4 or 255**5 gets too latge
 
    # plot_x = np.arange(0, 255, 1)
    # plot_y = c*(plot_x**gamma)
    # plt.scatter(plot_x, plot_y)
    # plt.show()

    for row in range (img.shape[0]):
        for col in range (img.shape[1]):
            img[row][col] = c*(img[row][col]**gamma)
    return img

def get_intensity_val(val, pt1, pt2):
    return (((pt2[1]-pt1[1])/(pt2[0]-pt1[0]))*(val - pt1[0])) + pt1[1]

def contrast_stretching(img, pt1, pt2, do_inverse=False):
    # if a 3rd channel is found then convert 
    # [TODO] Use your own function to go between different color spaces
    try:
        if img.shape[2] == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except:
        pass

    for row in range (img.shape[0]):
        for col in range (img.shape[1]):
            if img[row][col] > 0 and img[row][col] < pt1[0]:
                if not do_inverse:
                    img[row][col] = get_intensity_val(img[row][col], (0,0), pt1)
                else:
                    img[row][col] = get_intensity_val(img[row][col], (0,255), pt1)
            elif img[row][col] > pt1[0] and img[row][col] < pt2[0]:
                img[row][col] = get_intensity_val(img[row][col], pt1, pt2)
            else:
                if not do_inverse:
                    img[row][col] = get_intensity_val(img[row][col], pt2, (255, 255))
                else:
                    img[row][col] = get_intensity_val(img[row][col], pt2, (255, 0))
    return img