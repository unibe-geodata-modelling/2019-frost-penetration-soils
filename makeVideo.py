# make video 
# (.mp4 bzw *'mp4v' can be replaced by .avi bzw 'DIVX' to change video format)

import cv2
import numpy as np
import glob
import os

# set current directory as working directory
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
# os.chdir('C:/Users/User/Documents/geodataanalysis/soliflu')  # set working directory manually

# Choose an elevation
try:
    elevation
except NameError:
    elevation = input("choose an elevation! take 2400, 2500 or 2600")
    print("OK")
else:
    print("elevation is already defined")

# make a list of all frames in the "pics2400",  "pics2500" or "pics2600" folder
img_array = []
for filename in glob.glob(('pics' + str(elevation) + '/*.png')):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)
    print(len(img_array))  # just to have some feedback while it's working

# define video properties, the number --> frames per sec (FPS)
out = cv2.VideoWriter(('VIDEO' + str(elevation) + '.avi'), cv2.VideoWriter_fourcc(*'DIVX'), 30, size) 

# create video
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
img_array = []  # free memory
