import cv2
import os
import sys
import matplotlib.pyplot as plt 

sys.path.append('..')
import sharingan

img_original = cv2.imread(os.path.join('..', 'assets\chapter3_images\leaf.jpg'))

img_weighted = sharingan.bgr2gray(img_original, method='weighted')
img_avg = sharingan.bgr2gray(img_original, method='average')

#subplot(r,c) provide the no. of rows and columns
f, axarr = plt.subplots(1,2)

axarr[0].imshow(img_weighted, cmap='gray')
axarr[0].title.set_text('weighted')
axarr[1].imshow(img_avg, cmap='gray')
axarr[1].title.set_text('average')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()