# make video 
# (.mp4 bzw *'mp4v' can be replaced by .avi bzw 'DIVX' to change video format)

import cv2
import numpy as np
import glob

# make list of all frames in "pics" folder
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
