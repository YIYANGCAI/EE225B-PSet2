import cv2 as cv
import numpy as np
import os

class Solution(object):
    """
    gaussian based lpf 
    """
    def __init__(self, img_path):
        super(Solution).__init__()
        self.img = cv.imread(img_path)
        self.h, self.w = self.img.shape[:2]
    
    def gaussian_filters(self, img, kernel_size, sigma):
        img_GaussianBlur=cv.GaussianBlur(img, (kernel_size, kernel_size), sigma)
        return img_GaussianBlur
    
    def remain_largest_square(self):
        mask = 255 * np.ones((self.h, self.w, 3))
        negative = mask - self.img
        filtered = self.gaussian_filters(negative, 201, 50)
        cv.imwrite('./result_b_1.jpg', filtered)
        ret, thresh1 = cv.threshold(filtered, 127, 255, cv.THRESH_BINARY)
        out = mask - thresh1
        cv.imwrite('./result_b_2.jpg', out)
    
    def checkerboard_shading(self):
        shade = self.gaussian_filters(self.img, 201, 50)
        cv.imwrite('./result_c_shades.jpg', shade)
        out = (self.img / shade) * 255
        cv.imwrite('./result_c_1.jpg', out)

if __name__ == "__main__":
    # solution to the sub-question a & b
    s = Solution('./testpattern1024.tif')
    img_1 = s.gaussian_filters(s.img, 131, 30)
    cv.imwrite('./result_a.jpg', img_1)
    s.remain_largest_square()

    # solution to the sub-question c
    s2 = Solution('./checkerboard1024-shaded.tif')
    s2.checkerboard_shading()