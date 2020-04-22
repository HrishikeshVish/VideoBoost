import cv2
from tqdm import tqdm
import os
from os import listdir
import sys
path1 = 'output/'
path2 = 'outputp/'
contrast = 64
for filename in tqdm(listdir(path1)):
    img = cv2.imread(path1+filename, 1)
    f = 131*(contrast + 127)/(127*(131-contrast))
    alpha_c = f
    gamma_c = 127*(1-f)
    buf = cv2.addWeighted(img, alpha_c, img, 0, gamma_c)
    cv2.imwrite(path2+filename, buf)
