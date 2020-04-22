import cv2
import PIL
import random
import os
import numpy as np
import sys
import matplotlib.pyplot as plt
from tqdm import tqdm
from numba import jit
index_img = 0
def makeDataSet (path,outputpath, flag):
    cap = cv2.VideoCapture(path);
    initial = index_img
    avg_size = 0
    count = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if(ret == False):
            break
        #print(sys.getsizeof(frame))
        #frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        avg_size += sys.getsizeof(frame)
        
        if(flag == 0):
            frame = cv2.resize(frame, (1280,720), interpolation=cv2.INTER_AREA)
            cv2.imwrite(os.path.join(outputpath,str(count)+".jpg"), frame)
        else:
            cv2.imwrite(os.path.join(outputpath,str(count)+".jpg"), frame)
        count+=1
    #print("Avg size of images: ", avg_size/index_img)
    cap.release()
    cv2.destroyAllWindows()

makeDataSet("C:\\Users\\hrish\\Downloads\\VideoBoost\\LQ1.mp4","C:\\Users\\hrish\\Downloads\\VideoBoost\\in1e",0)
