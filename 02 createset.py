from os import listdir
from numpy import asarray
from numpy import vstack
from keras.preprocessing import image
from numpy import savez_compressed

import cv2
import PIL
import random 
import os
import numpy as np
import sys
import matplotlib.pyplot as plt
from tqdm import tqdm
from numba import jit
import datetime
 
# load all images in a directory into memory
def load_images(src_1_path, out_path, size=(256,256)):
    src_list, tar_list = list(), list()        
    for filename in tqdm(listdir(src_1_path)):
        pixels1 = image.load_img(src_1_path + filename, target_size=size)
        pixels1 = image.img_to_array(pixels1)
        src_list.append(pixels1)
    for filename in tqdm(listdir(out_path)):
        pixels = image.load_img(out_path + filename, target_size=size)
        pixels = image.img_to_array(pixels)
        tar_list.append(pixels)
    return np.array(src_list), np.array(tar_list)

src_1_path = 'in1/'
src_2_path = 'in2/'
out_1_path = 'out1/'
out_2_path = 'out2/'
[src_images, tar_images] = load_images(src_1_path, out_1_path)
print('Loaded: ', src_images.shape, tar_images.shape)
filename = 'image_data1.npz'
savez_compressed(filename, src_images, tar_images)
print('Saved dataset: ', filename)


[src_images, tar_images] = load_images(src_2_path, out_2_path)
print('Loaded: ', src_images.shape, tar_images.shape)
filename = 'image_data2.npz'
savez_compressed(filename, src_images, tar_images)
print('Saved dataset: ', filename)
