import cv2 as cv
import numpy as np
import os

class Solution():
    """
    test code on hpf
    """
    def __init__(self, img_path):
        super().__init__()
        self.img = cv.imread(img_path)
        self.img_gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)

    def find_range(self, img):
        return img.min(), img.max()

    def Conv2(self, img, kernel):
        # default assertion:
        # kernel size is odd: 3*3, 5*5, etc
        # channel number: 1
        kernel_size = kernel.shape[0]
        padding_size = int((kernel_size-1)/2)
        print(padding_size)
        h, w = img.shape[:2]
        img=np.pad(img, ((padding_size,padding_size),(padding_size,padding_size)),'constant', constant_values=(0,0)) 
        # keep the same size of input
        out = np.zeros((h, w))
        print(img.shape)
        for row in range(0, h):
            for col in range(0, w):
                m1 = img[row: row+kernel_size, col:col+kernel_size]
                m2 = kernel
                val = (m1*m2).sum()
                out[row,col] = val
        return out

    def shapen_with_laplacian(self):
        l_kernel = np.ones((3,3))
        l_kernel[1,1] = -8
        mask = self.Conv2(self.img_gray, l_kernel)
        cv.imwrite('./result_a_lp_mask.jpg', mask)
        out = self.img_gray + mask
        _min, _max = self.find_range(out)
        #out_scaled = img1_scaled = (out-_min) / (_max - _min) * 255
        cv.imwrite('./result_a_1.jpg', out)

    def edge_with_sobel(self):
        init_kernel = np.zeros((3,3))
        sobel_k1 = init_kernel
        sobel_k2 = init_kernel
        sobel_k1[0,0] = -1
        sobel_k1[0,1] = -2
        sobel_k1[0,2] = -1
        sobel_k1[2,0] = 1
        sobel_k1[2,1] = 2
        sobel_k1[2,2] = 1
        _sobel_tmp = sobel_k1
        sobel_k2 = np.transpose(_sobel_tmp)
        print(sobel_k1)
        print(sobel_k2)
        sobel_k1_flipped = np.flip(_sobel_tmp, 0)
        sobel_k2_flipped = np.flip(sobel_k2, 1)
        print(sobel_k1_flipped)
        print(sobel_k2_flipped)
        out_1 = self.Conv2(self.img_gray, sobel_k1)
        out_1_fliped = self.Conv2(self.img_gray, sobel_k1_flipped)
        out_2 = self.Conv2(self.img_gray, sobel_k2)
        out_2_fliped = self.Conv2(self.img_gray, sobel_k2_flipped)
        cv.imwrite('./result_b_1.jpg', out_1)
        cv.imwrite('./result_b_2.jpg', out_2)
        cv.imwrite('./result_b_1_reversed.jpg', out_1_fliped)
        cv.imwrite('./result_b_2_reversed.jpg', out_2_fliped)
        out_3 = self.Conv2(out_1, sobel_k2)
        cv.imwrite('./result_c.jpg', out_3)

        # mag
        sums = out_1 * out_1 + out_2 * out_2
        out_4 = np.sqrt(sums)
        cv.imwrite('./result_d.jpg', out_4)

if __name__ == "__main__":
    s = Solution('./blurry-moon.tif')
    s.shapen_with_laplacian()
    s2 = Solution('./checkerboard1024-shaded.tif')
    s2.edge_with_sobel()