import cv2
import PIL
import random 
import os
import numpy as np
import sys
import matplotlib.pyplot as plt
from tqdm import tqdm
from numba import jit

PATH = dict()
PATH["input_1"] = "input_1"
PATH["input_2"] = "input_2"
PATH["target"] = "target"
PATH["video"] = "C:\\Users\\hrish\\Downloads\\VideoBoost"

dim = (256,256)

def checkDir():
    print (os.listdir())
    if (PATH["input_1"] not in os.listdir()): os.mkdir(PATH["input_1"]);
    if (PATH["input_2"] not in os.listdir()): os.mkdir(PATH["input_2"]);
    if (PATH["target"] not in os.listdir()): os.mkdir(PATH["target"]);
    print(os.listdir())
    


checkDir()

index_img = 0
input_1 = 0
input_2 = 0
target = 0


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
            frame = cv2.resize(frame, (256, 144), interpolation=cv2.INTER_AREA)
            cv2.imwrite(os.path.join(outputpath,str(count)+".jpg"), frame)
        else:
            cv2.imwrite(os.path.join(outputpath,str(count)+".jpg"), frame)
        count+=1
    #print("Avg size of images: ", avg_size/index_img)
    cap.release()
    cv2.destroyAllWindows()
    
    
makeDataSet("C:\\Users\\hrish\\Downloads\\VideoBoost\\HQ1.mp4","C:\\Users\\hrish\\Downloads\\VideoBoost\\out1",1)
makeDataSet("C:\\Users\\hrish\\Downloads\\VideoBoost\\HQ2.mp4","C:\\Users\\hrish\\Downloads\\VideoBoost\\out2", 1)
makeDataSet("C:\\Users\\hrish\\Downloads\\VideoBoost\\HQ1.mp4","C:\\Users\\hrish\\Downloads\\VideoBoost\\in1",0)
makeDataSet("C:\\Users\\hrish\\Downloads\\VideoBoost\\HQ2.mp4","C:\\Users\\hrish\\Downloads\\VideoBoost\\in2",0)

