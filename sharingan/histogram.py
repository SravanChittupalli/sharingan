import numpy as np
import matplotlib.pyplot as plt
from sharingan.intensity_transforms import get_intensity_val
def get_histogram(img):
    '''
    @brief: The function takes a greyscale image and it shows histogram using a matplotlib bar graph. 

    @parameters: 
        img = image array (greyscale)
    
    @return:
        None
    '''

    # check if image is greyscale or not
    assert len(img.shape) == 2, "Input a greyscale image"

    # get a list from 0 to 255...this makes the x axis
    x = np.arange(0, 256, 1)
    # Initialize an array of same shape as x but with all elements as 0
    y = np.zeros_like(x)

    rows, cols = img.shape
    for row in range(rows):
        for col in range(cols):
            # increment element of y array corresponding to the pixel value
            y[img[row][col]] += 1
    
    # plot the bar graph
    plt.bar(x, y, 2)
    plt.xlabel('pixel values')
    plt.ylabel('number of pixels')
    plt.title('Histogram')
    plt.show()

def histogram_stretching(img, output_range):
    '''
    @brief: The function takes a greyscale image and gets the pixel values into the specified range. 

    @parameters: 
        img = image array (greyscale)
    
    @return:
        Stretched image
    '''
    # check if image is greyscale or not
    assert len(img.shape) == 2, "Input a greyscale image"
    
    rows, cols = img.shape
    max_pixel_val = np.amax(img)
    min_pixel_val = np.amin(img)
    for row in range(rows):
        for col in range(cols):
            img[row][col] = get_intensity_val(img[row][col], (min_pixel_val, output_range[0]), (max_pixel_val, output_range[1]))
    return img
    