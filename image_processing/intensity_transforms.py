import cv2

# Max intensity level
L = 255

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