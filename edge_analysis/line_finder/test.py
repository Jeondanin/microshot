import cv2
import numpy as np
import region_growing
import curve_fitting
from imageUtil import cut
import pandas as pd
import copy

if __name__ == "__main__":
    
    ori_im = cv2.imread('batch0.png', 0) # read a gray image
    in_data = np.ones((5,6), dtype=np.uint8)
    df     = pd.read_csv('node.csv', header=None)
    node_list = df[(df[0] <=200) & (df[1] <=200)]

    bin_im = ((ori_im>125)*255).astype(np.uint8)[:,:]  
    #cv2.imshow('bin_im',bin_im)
    #cv2.waitKey(0)
    
    gs = region_growing.model.GrowSeedAlgo(node_list,im=bin_im,)
    Allpoints = gs.start()

    result_list = []
    for line_points in Allpoints:
        if line_points:
            result = curve_fitting.main.curve_fitting(line_points)
            result_list.append(result)

    copy_im = copy.deepcopy(ori_im)
    color_image =  cv2.merge((copy_im, copy_im, copy_im))
    for result_one in result_list:
        # result_one = [140.42423852975134, -0.9817, 1, 3, 39, '5mm']


        x_s = int(result_one[3])
        x_e = int(result_one[4])
        for i in range(x_s, x_e):
            color_image[i][int(round(float(result_one[2])*np.power(i, 2)+ float(result_one[1])*i + float(result_one[0])))] = (255,0,0)
        
        middle = int((x_s+x_e)/2)
        v_middle = int((float(result_one[2])*np.power(middle, 2)+float(result_one[1])*middle + float(result_one[0])))

        
        # pointer line
        if middle < ori_im.shape[1] -10:
            line = 6
            for i in range(line):
                color_image[middle+i][v_middle+i]=(0,255,255)
            #                                                        height, width
            cv2.putText(color_image, 'L : '+result_one[5], (v_middle+line+4, middle+line+4), cv2.FONT_HERSHEY_PLAIN, 0.6, (0,255,255))

    cv2.imshow("color_src01", color_image)
    cv2.waitKey(0)
    cv2.imwrite("copy.png",color_image)

