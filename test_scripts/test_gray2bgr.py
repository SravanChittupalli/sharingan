import cv2
import os
import sys
import matplotlib.pyplot as plt 

sys.path.append('..')
import sharingan

img_original = cv2.imread(os.path.join('..', 'assets\chapter3_images\leaf.jpg'))

img_weighted = sharingan.bgr2gray(img_original, method='weighted')
three_channeled_img = sharingan.gray2bgr(img_weighted)

#subplot(r,c) provide the no. of rows and columns
f, axarr = plt.subplots(1,2)

axarr[0].imshow(img_weighted, cmap='gray')
axarr[0].title.set_text('gray img')
axarr[1].imshow(three_channeled_img)
axarr[1].title.set_text('colored img')
plt.show()