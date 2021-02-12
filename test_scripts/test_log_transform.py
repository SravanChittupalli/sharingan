import cv2
import os
import sys

sys.path.append('..')
import sharingan

img = cv2.imread(os.path.join('..', 'assets\chapter3_images\Fig0305(a)(DFT_no_log).tif'))

img = sharingan.log_transform(img, 0.5)

cv2.imshow('demo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()