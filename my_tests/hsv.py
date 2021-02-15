# from sharingan.change_color_space import bgr2gray
import cv2
import os
import time

img_original = cv2.imread(os.path.join('..', 'assets\chapter3_images\leaf.jpg'))

hsv_img = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)

prev = time.time()
bgr_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
print('time taken: ', time.time()-prev)
# print(max(hsv_img[:, :, 1].all()))
cv2.imshow('original', img_original)
cv2.imshow('HSV', hsv_img)
cv2.imshow('BGR', bgr_img)

cv2.waitKey(0)
cv2.destroyAllWindows()