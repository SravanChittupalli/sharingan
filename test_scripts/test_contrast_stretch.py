import cv2
import os
import sys

sys.path.append('..')
import sharingan

img_original = cv2.imread(os.path.join('..', 'assets\chapter3_images\Fig0310(b)(washed_out_pollen_image).tif'))

img = sharingan.contrast_stretching(img_original, (100, 60), (170, 225), do_inverse=False)
# img = contrast_stretching(img, (100, 255), (100, 0), do_inverse=True)

cv2.imshow('demo_original', img_original)
cv2.imshow('demo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()