import cv2 as cv
import os
import numpy as np

class Solution():
    """
    one solution can read a img and generate its histogram-equalized results
    """
    def __init__(self, img_path):
        self.img_name = img_path[0:-4]
        self.img = cv.imread(img_path)
        self.img_gray = cv.cvtColor(self.img, cv.COLOR_RGB2GRAY)
        self.h, self.w = self.img_gray.shape[:2]
        self.init_hist = np.zeros(256)
        self.mapping = np.zeros(256)
    
    def cvIntergratedEqual4e(self):
        out = cv.equalizeHist(self.img_gray)
        cv.imwrite(self.img_name+'_opencv_included.jpg', out)
    
    def histEqual4e(self):
        data = self.img_gray.flatten()
        total = self.h * self.w
        new_img = np.zeros((self.h, self.w))
        for pixel in list(data):
            self.init_hist[pixel] = self.init_hist[pixel] + 1
        for rk in range(256):
            accumulate = 0
            for _index in range(rk):
                accumulate += self.init_hist[_index]
            sk = int(256*accumulate/total)
            self.mapping[rk] = sk
        for i in range(self.h):
            for j in range(self.w):
                prev_v = self.img_gray[i,j]
                equa_v = self.mapping[prev_v]
                new_img[i,j] = equa_v
        cv.imwrite(self.img_name+'_self_written.jpg', new_img)


if __name__ == "__main__":
    s1 = Solution('./spillway-dark.tif')
    s1.cvIntergratedEqual4e()
    s1.histEqual4e()
    s2 = Solution('./hidden-horse.tif')
    s2.cvIntergratedEqual4e()
    s2.histEqual4e()
    #print(s.mapping)