import cv2
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('..')
import sharingan

img_greyscale = cv2.imread(os.path.join('..', 'assets\chapter3_images\Fig0310(b)(washed_out_pollen_image).tif'), 0)

sharingan.get_histogram(img_greyscale)

img = sharingan.contrast_stretching(img_greyscale, (100, 50), (130, 220), do_inverse=False)
cv2.imshow('demo_stretched', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

sharingan.get_histogram(img)