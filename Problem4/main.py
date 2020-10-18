import cv2 as cv
import numpy as np
import os

class Solution(object):
    """
    Use the unsharp masking and high-boosting methods to process the moon image.
    """
    def __init__(self, img_path):
        super(Solution).__init__()
        self.img = cv.imread(img_path)
        self.img_gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)

    def find_range(self, img):
        return img.min(), img.max()
    
    def unsharp_mask(self):
        blur = cv.GaussianBlur(self.img_gray, (3, 3), 0)
        mask = self.img_gray - blur
        cv.imwrite('./mask.jpg', mask)
        out_1 = self.img_gray + 1 * mask
        cv.imwrite('./result_a_1.jpg', out_1)

        out_2 = self.img_gray + 1.25 * mask
        cv.imwrite('./result_a_2.jpg', out_2)

if __name__ == "__main__":
    s = Solution('./blurry-moon.tif')
    s.unsharp_mask()