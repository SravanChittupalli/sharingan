import numpy as np

def bgr2gray(img, method='weighted'):
    '''
    method_to_use = 'average', 'weighted'
    '''
    # each pixel value of bgr image uses a memory of 24bits
    # 8-B, 8-G, 8-R
    # 
    # Average method
    # https://www.tutorialspoint.com/dip/grayscale_to_rgb_conversion.htm
    
    img = np.asarray(img)
    if method == 'average':
        grayimg = img[:,:,0]*(1/3) + img[:,:,1]*(1/3) + img[:,:,2]*(1/3)

    elif method == 'weighted':
        #ref http://jscience.org/experimental/javadoc/org/jscience/computing/ai/vision/GreyscaleFilter.html
        grayimg = img[:,:,0]*0.07 + img[:,:,1]*0.72 + img[:,:,2]*0.21

    return grayimg