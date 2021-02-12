import numpy as np

def bgr2gray(img, method='weighted'):
    '''
    @brief
    Converts a bgr image to a grayscale image using the selected 'method'
    
    @input
    img = colored image; BGR is the channel order
    method_to_use = 'average', 'weighted'

    @output
    grayscale image
    '''
    # check if image is 3 channeled or not
    assert len(img.shape) == 3

    # convert to numpy array for broadcasting
    img = np.asarray(img)

    # each pixel value of bgr image uses a memory of 24bits
    # 8-B, 8-G, 8-R

    # Average method
    # https://www.tutorialspoint.com/dip/grayscale_to_rgb_conversion.htm
    if method == 'average':
        grayimg = (img[:,:,0]*(1/3) + img[:,:,1]*(1/3) + img[:,:,2]*(1/3)).astype(np.uint8)

    elif method == 'weighted':
        #ref http://jscience.org/experimental/javadoc/org/jscience/computing/ai/vision/GreyscaleFilter.html
        grayimg = (img[:,:,0]*0.07 + img[:,:,1]*0.72 + img[:,:,2]*0.21).astype(np.uint8)

    return grayimg

def gray2bgr(img):
    '''
    @brief
    Converts a grayscale image to a 3 channeled image. For a given pixel all 3 channels will have the same intensities
    
    @input
    img = grayscale image

    @output
    3 channeled image
    '''
    img = np.expand_dims(np.asarray(img), axis=2)

    three_channel_img = np.concatenate([img, img, img], axis=2).astype(np.uint8)

    return three_channel_img