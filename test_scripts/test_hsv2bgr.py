import cv2
import os
import sys
import matplotlib.pyplot as plt 
import time

sys.path.append('..')
import sharingan

img_original = cv2.imread(os.path.join('..', 'assets\chapter3_images\leaf.jpg'))
img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)
print(img_hsv)

prev = time.time()
img_bgr = sharingan.hsv2bgr(img_hsv)
print("time taken: ", time.time()-prev)

print(img_bgr.shape)
#subplot(r,c) provide the no. of rows and columns
# f, axarr = plt.subplots(1,2)

# axarr[0].imshow(img_original)
# axarr[0].title.set_text('original')
# axarr[1].imshow(img_bgr)
# axarr[1].title.set_text('bgr')
# cv2.imshow('original', img_original)
# cv2.waitKey(0)
cv2.imshow('hsv2bgr', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()