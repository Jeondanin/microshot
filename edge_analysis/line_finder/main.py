import cv2
import numpy as np
import region_growing
from imageUtil import cut
import curve_fitting
import pandas as pd
import time
from multiprocessing import Process, Queue


result_list = []

def work(id, node_list, bin_im, loop):
    # 노드포인트를 그림과함께 넘겨야합니다. 
    gs = region_growing.model.GrowSeedAlgo(node_list,im=bin_im)
    Allpoints = gs.start()
    global result_list
    for line_points in Allpoints:
        if line_points:
            result = curve_fitting.main.curve_fitting(line_points)
            result_list.append(result)
    
    # result_list = []
    # mocks = [i for i in range(5)]
    # for i in mocks:
    #     result_list.append(i)
    #     print('process %s is playing'%(id,))




if __name__ == "__main__":
    tic = time.time()
    # 원본 cut
    instance = cut.Cut('cell3.png')
    parted = instance.start()
    batch_h = 200
    batch_w = 200
    stride_h = 100
    stride_w = 100

    # multiprocessing Q 
    QO = Queue()
    id = 0
    processes = []
    for row_i, row_pic in parted.items():
        for part_i, part_pic in row_pic.items():
            loop = len(parted)*len(row_pic)
            bin_im    = ((part_pic>125)*255).astype(np.uint8)[:,:]
            cv2.imwrite('part/%s.png'%(id,),bin_im)
            # 노드포인트 필요합니다.
            df        = pd.read_csv('node.csv', header=None)
            start_h  = int(batch_h*int(row_i)) 
            end_h    = int(batch_h*(int(row_i)+1)) 
            start_w  = int(batch_w*int(part_i)) 
            end_w    = start_w + batch_w
            # before converting
            node_list = df[(df[0] >=start_h) & (df[0] <end_h) & (df[1] >=start_w) & (df[1] <end_w)]
            print(node_list)
            # after converted
            node_list.loc[:,0] -= start_h
            node_list.loc[:,1] -= start_w
            print(node_list)
            # a process of Mulitprocessing
            if id ==99:
                th = Process(target=work, args=(id, node_list,bin_im,loop))
                th.daemon = True
                th.start()
                processes.append(th)
            
            id += 1

    for i in processes:
        i.join()

    QO.put('STOP')

    
    total = 0
    while True:
        tmp = QO.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp
    toc = time.time()
    print(toc - tic)
    print(f"Result: {total}")
