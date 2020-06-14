import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def curve_fitting(line_points, im_size=None):
    print(line_points)
    x = []
    y = []
    for i in line_points:
        x.append(i[0])
        y.append(i[1])
    
    x = np.array(x)
    y = np.array(y)
    nSz = np.size(x)
   

    if x.size >2:
        A_mat_square = np.hstack((np.hstack((np.ones((nSz, 1)), np.reshape(x, (nSz, 1)))), np.power(np.reshape(x, (nSz, 1)), 2)))
        A_mat_square_trans = np.transpose(A_mat_square)
        cData_square = np.matmul(np.matmul(np.linalg.pinv(np.matmul(A_mat_square_trans, A_mat_square)), A_mat_square_trans), y)
        r2 = sum(abs(y - np.power(x, 2)*cData_square[2] - x*cData_square[1]-cData_square[0])) # error size

        A_mat_square2 = np.hstack((np.hstack((np.ones((nSz, 1)), np.reshape(y, (nSz, 1)))), np.power(np.reshape(y, (nSz, 1)), 2)))
        A_mat_square_trans2 = np.transpose(A_mat_square2)
        cData_square2 = np.matmul(np.matmul(np.linalg.pinv(np.matmul(A_mat_square_trans2, A_mat_square2)), A_mat_square_trans2), x)

        r3 = sum(abs(x - np.power(y, 2)*cData_square[2] - y*cData_square[1]-cData_square[0])) # error size

        r_min = np.min([ r2, r3])
    else:
        r_min = None
    range_x = 200 if not im_size else im_size[1]
    range_y = 200 if not im_size else im_size[0]
    if not r_min:
        return  np.append(np.array([0,0,0]),
                          np.array([min(x), max(x),'5mm'])
                            )
    elif r_min == r2:
        rx = np.linspace(min(x), max(x), 30)
        ry = np.power(rx, 2)*cData_square[2] + rx*cData_square[1] + cData_square[0]
        plt.xlim([0,range_x])
        plt.ylim([0,range_y])
        plt.plot(ry, range_y-rx)
        plt.show()
        return np.append(cData_square, np.array([min(x), max(x),'5mm']))
    else:
        ry = np.linspace(min(y), max(y), 30)
        rx = np.power(ry, 2)*cData_square[2] + ry*cData_square[1] + cData_square[0]
        plt.xlim([0,range_x])
        plt.ylim([0,range_y])
        plt.plot(ry, range_y-rx)
        plt.show()
        return np.append(cData_square2, np.array([min(y), max(y),'5mm']))

if __name__ == "__main__":
    im = cv.imread('sample/edge_sample.png')
    bin_im    = ((im>125)*255).astype(np.uint8)[:,:]
    list_point = []
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if (im[i][j] == np.array([255, 255, 255], dtype="uint8")).max():
                list_point.append([i,j])
    curve_info = curve_fitting(list_point, bin_im.shape)

    x = []
    y = []
    for i in list_point:
        x.append(i[0])
        y.append(i[1])
        # 1차 방정식
        if len(curve_info) ==2:
            f_y = i[0]*curve_info[1] + curve_info[0]
            dif = abs(i[1] - f_y)
            if dif < 10:
                continue
            else:
                print('this picture is node')
                break
        
        # 2차 방정식
        elif len(curve_info) ==3:
            f_y = np.power(i[0], 2)*curve_info[2] + i[0]*curve_info[1] + curve_info[0]
            dif = abs(i[1] - f_y)
            if dif < 10:
                continue
            else:
                print('this picture is node')
                break
    else:
        print('this picture is edge')
    