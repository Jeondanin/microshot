import numpy as np
import cv2 as cv


class Cut():
    def __init__(self, image_path=None):
        self.batch_w = 200 
        self.batch_h  = 200 
        self.all_part = {}
        if image_path is not None:
            self.imread(image_path)
            self.height = self.image.shape[0]
            self.width = self.image.shape[1]
            self.h_value = self.height//self.batch_h
            self.h_remain = self.height - self.h_value*self.batch_h
            self.w_value = self.width//self.batch_w
            self.w_remain = self.width - self.w_value*self.batch_w
            self.stride_h = self.batch_h/2
            self.stride_w = self.batch_w/2
            
        else:
            raise ValueError("please input a image to cut")

    def imread(self, image_path):
        tmp = cv.imread(image_path)
        self.image = cv.cvtColor(tmp ,cv.COLOR_BGR2GRAY)



    def start(self):
        for i in range(self.h_value if self.h_remain==0 else self.h_value + 1):
            start_h  = int(self.batch_h*i)
            end_h    = int(self.batch_h*(i+1)) 
            self.all_part[str(i)] = {}
            tmp_row  = self.image[start_h:end_h]
            for j in range(self.w_value if self.w_remain==0 else self.w_value + 1):
                start_w  = int(self.batch_w*j) 
                end_w    = int(self.batch_w*(j+1)) 
                tmp_part  =  tmp_row[:,start_w:end_w]
                self.all_part[str(i)][str(j)] = tmp_part

        return self.all_part
