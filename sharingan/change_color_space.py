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
    assert len(img.shape) == 3, "Give a valid image, img.shape != 3"

    # convert to numpy array for broadcasting
    img = np.asarray(img)

    # each pixel value of bgr image uses a memory of 24bits
    # 8-B, 8-G, 8-R

    # Average method
    # https://www.tutorialspoint.com/dip/grayscale_to_rgb_conversion.htm
    if method == 'average':
        grayimg = (img[:,:,0]*(1/3) + img[:,:,1]*(1/3) + img[:,:,2]*(1/3)).astype(np.uint8)

    # weighs red, green and blue according to their wavelengths
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
    assert len(img.shape) == 1, "Give a valid image, img.shape != 1"
    img = np.expand_dims(np.asarray(img), axis=2)

    three_channel_img = np.concatenate([img, img, img], axis=2).astype(np.uint8)

    return three_channel_img

def bgr2hsv(img):
    '''
    @brief Converts img in HSV space to RGB space

    @input img: HSV image

    @output: converted img in HSV space to RGB space

    Reference: https://www.youtube.com/watch?v=I8i0W8ve-JI

    hue, saturation, and values are expressed in terms of color, shading, and toning.
    hue -> what chroma is there
    saturation -> amount of whiteness in the chroma. More whiteness less is the saturation
    value -> amount of blackness/darkness in the chroma. More the value less is the blackness
    '''
    # Check if 3 channels are available
    assert len(img.shape) == 3, "Give a valid image, img.shape != 3"

    # img = np.asarray(img, dtype=np.float)
    img = img[:,:,:]/255

    hsv_image = np.zeros_like(img, dtype=np.uint8)

    for row in range (img.shape[0]):
        for col in range (img.shape[1]):
            b,g,r = img[row][col]

            # check which of rgb channels is max and min and also store the index of channel with highest intensity
            if (r>=g) and (r>=b):
                idx_of_max_of_bgr = 2
                max_val = r
                min_val = g if g<b else b
            
            elif (g>=b) and (g>=r):
                idx_of_max_of_bgr = 1
                max_val = g
                min_val = b if b<r else r

            elif (b>=g) and (b>=r):
                idx_of_max_of_bgr = 0
                max_val = b
                min_val = g if g<r else r

            # difference between max and min values
            range_min_max = max_val-min_val

            # value = max_value*255
            value = max_val*255

            # range_of_max_min==0 only if:
            # 1) max_value=0 i.e black
            # 2) r=g=b
            if range_min_max == 0:
                saturation = 0
            else:
                saturation = (range_min_max/max_val)*255
            
            #
            if range_min_max == 0:
                hue = 0
            else:
                if idx_of_max_of_bgr == 0: # blue max
                    hue = 60*(4+((r-g)/range_min_max))
                elif idx_of_max_of_bgr == 1: # green max
                    hue = 60*(2+((b-r)/range_min_max))
                elif idx_of_max_of_bgr == 2: # red max
                    hue = 60*(g-b)/range_min_max
                    if hue < 0: # for case when hue is negative then we have to bring it between 0-360
                        hue+=360
            # # print(hue, saturation, value)
            hsv_image[row][col] = [hue, saturation, value]
    
    return hsv_image

def hsv2bgr(img):
    '''
    @brief Converts img in HSV space to RGB space

    @input img: HSV image

    @output: converted img in HSV space to RGB space

    Reference: https://www.youtube.com/watch?v=hW4gZ4tGwds
    '''
    # Check if 3 channels are available
    assert len(img.shape) == 3, "Give a valid image, img.shape != 3"

    img = np.asarray(img, dtype=np.float)

    # normalise satuation and value channels
    img[:,:,1] = img[:,:,1]/255
    img[:,:,2] = img[:,:,2]/255

    # max_rgb val = value of 'value' for the pixel
    max_rgb = img[:,:,2]
    # min_rgb val = max_rgb - value*saturation
    min_rgb = max_rgb[:,:] - (img[:,:,1]*img[:,:,2])

    bgr_img = np.zeros_like(img, dtype=np.uint8)
    
    for row in range (img.shape[0]):
        for col in range(img.shape[1]):
            max = max_rgb[row][col]
            min = min_rgb[row][col]

            if img[row][col][0] >= 0 and img[row][col][0] < 60:
                bgr_img[row][col] = [min*255,((((max-min)*(img[row][col][0]-60))/60)+max)*255,max*255]

            elif img[row][col][0] >= 60 and img[row][col][0] < 120:
                bgr_img[row][col] = [min*255,max*255,((((min-max)*(img[row][col][0]%60))/60)+max)*255]

            elif img[row][col][0] >= 120 and img[row][col][0] < 180:
                bgr_img[row][col] = [((((max-min)*((img[row][col][0]%60)-60))/60)+max)*255,max*255,min*255]

            elif img[row][col][0] >= 180 and img[row][col][0] < 240:
                bgr_img[row][col] = [max*255,((((min-max)*((img[row][col][0]%60)))/60)+max)*255,min*255]

            elif img[row][col][0] >= 240 and img[row][col][0] < 300:
                bgr_img[row][col] = [max*255,min*255,((((max-min)*((img[row][col][0]%60)-60))/60)+max)*255]

            elif img[row][col][0] >= 300 and img[row][col][0] < 360:
                bgr_img[row][col] = [((((min-max)*((img[row][col][0]%60)))/60)+max)*255,min*255,max*255]

    return bgr_img