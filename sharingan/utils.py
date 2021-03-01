import numpy as np
import multiprocessing as mp
import itertools

# All functions starting with 'pp' are the ones with parallelprocessing code
# All function names starting with 'module' are used to modularize code for parallelprocessing

def module_pp_in_range(row, col, pixel, range_channel_1, range_channel_2, range_channel_3):
    if (pixel[0] >= range_channel_1[0] and pixel[0] <= range_channel_1[1]) and (pixel[1] >= range_channel_2[0] and pixel[1] <= range_channel_2[1]) and (pixel[2] >= range_channel_3[0] and pixel[2] <= range_channel_3[1]):
        # print('entered')
        return (row, col, 255)
    return (row, col, 0)

def pp_in_range(img, all_ranges):
    '''
    @brief Thresholds a 3 channel image according to the specified ranges also using pythons parallel processing

    @input img: any 3 channel image, range of values as list of list or tuple of tuple
                [[red_min,red_max], [green_min,green_max], [blue_min,blue_max]]

    @output: A 2D image with the pixels in specified range of input image are represented as white pixels in output image.
    '''
    range_channel_1, range_channel_2, range_channel_3 = all_ranges

    #extract shape of img
    height, width, _ = img.shape
    # print(img.shape)

    # create 2D image
    img_new = np.zeros((height, width), dtype=np.uint8)
    # print(range_channel_1[0])

    rows = range(height)
    cols = range(width)
    # for row in range(height):
    #     for col in range(width):
    #         pixel = img[row][col]
            # if (pixel[0] >= range_channel_1[0] and pixel[0] <= range_channel_1[1]) and (pixel[1] >= range_channel_2[0] and pixel[1] <= range_channel_2[1]) and (pixel[2] >= range_channel_3[0] and pixel[2] <= range_channel_3[1]):
    
    pool = mp.Pool(mp.cpu_count())
    # create result objects list as we are not using a callback so apply_async will return a pool.ApplyResult object
    result_objects = [pool.apply_async(module_pp_in_range, args=(row, col, img[row][col], range_channel_1, range_channel_2, range_channel_3)) for row, col in itertools.product(rows, cols)]
    
    for r in result_objects:
        img_new[r.get()[0]][r.get()[1]] = r.get()[2]

    pool.close()
    pool.join()
            # img_new[row][col] = 255

    return img_new

def in_range(img, all_ranges):
    '''
    @brief Thresholds a 3 channel image according to the specified ranges.

    @input img: any 3 channel image, range of values as list of list or tuple of tuple
                [[red_min,red_max], [green_min,green_max], [blue_min,blue_max]]

    @output: A 2D image with the pixels in specified range of input image are represented as white pixels in output image.
    '''
    # Check if 3 channels are available
    assert len(img.shape) == 3, "Give a valid image, img.shape != 3"

    range_channel_1, range_channel_2, range_channel_3 = all_ranges

    #extract shape of img
    height, width, _ = img.shape

    # create 2D image
    img_new = np.zeros((height, width), dtype=np.uint8)

    for row in range(height):
        for col in range(width):
            pixel = img[row][col]
            if (pixel[0] >= range_channel_1[0] and pixel[0] <= range_channel_1[1]) and (pixel[1] >= range_channel_2[0] and pixel[1] <= range_channel_2[1]) and (pixel[2] >= range_channel_3[0] and pixel[2] <= range_channel_3[1]):
                img_new[row][col] = 255

    return img_new