import cv2
import os
import sys

sys.path.append('..')
import sharingan

#read image
# img = cv2.imread(os.path.join('..', 'assets\chapter3_images\Fig0308(a)(fractured_spine).tif'))
img = cv2.imread(os.path.join('..', 'assets\chapter3_images\Fig0309(a)(washed_out_aerial_image).tif'))

# perform gamma transform
img_0_4 = sharingan.gamma_transform(img, 4)
img_0_6 = sharingan.gamma_transform(img, 3)
img_0_3 = sharingan.gamma_transform(img, 5)

# display transformed images
cv2.imshow('gamma = 0.6', img_0_6)
cv2.imshow('gama = 0.4', img_0_4)
cv2.imshow('gamma = 0.3', img_0_3)
cv2.waitKey(0)
cv2.destroyAllWindows()