import cv2
import os
import sys

sys.path.append('..')
import sharingan

img = cv2.imread(os.path.join('..', 'assets/chapter3_images/Fig0304(a)(breast_digital_Xray).tif'))

img = sharingan.negative(img)

cv2.imshow('demo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()