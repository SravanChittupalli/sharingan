# from sharingan.utils import in_range
import cv2
import os
import sys
import matplotlib.pyplot as plt 
import time

sys.path.append('..')
import sharingan

def main():
    # img_original = cv2.imread(os.path.join('..', 'assets\chapter3_images\leaf.jpg'))
    img_original = cv2.imread(os.path.join('..', 'assets\shapes_colors.jfif'))
    # print(img_original.shape)

    prev = time.time()
    img_in_range = sharingan.in_range(img_original, [[200,255], [200,255], [200,255]])
    print("time taken bgr2hsv: ", time.time()-prev)
    # print(img_in_range)

    #subplot(r,c) provide the no. of rows and columns
    f, axarr = plt.subplots(1,2)

    axarr[0].imshow(img_original[:,:,[2,1,0]])
    axarr[0].title.set_text('weighted')
    axarr[1].imshow(img_in_range, cmap='gray')
    axarr[1].title.set_text('average')
    plt.show()

    # print(img_in_range)
    # cv2.imshow("demo", img_in_range)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
