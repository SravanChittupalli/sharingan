import cv2
import os
import sys
import matplotlib.pyplot as plt 
import time

sys.path.append('..')
import sharingan

img_original = cv2.imread(os.path.join('..', 'assets\chapter3_images\leaf.jpg'))

prev = time.time()
img_hsv = sharingan.bgr2hsv(img_original)
print("time taken bgr2hsv: ", time.time()-prev)

prev = time.time()
img_bgr = sharingan.hsv2bgr(img_hsv)
print("time taken hsv2bgr: ", time.time()-prev)

# print(img_bgr.shape)
#subplot(r,c) provide the no. of rows and columns
f, axarr = plt.subplots(1,2)

axarr[0].imshow(img_hsv[:,:,[2,1,0]])
axarr[0].title.set_text('original')
axarr[1].imshow(img_bgr[:,:,[2,1,0]])
axarr[1].title.set_text('bgr')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()