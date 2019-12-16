# make GIF

from PIL import Image
import glob
import os

# set current directory as working directory
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
# os.chdir('C:/Users/User/Documents/geodataanalysis/soliflu')  # set working directory manually

# Choose elevation if it is not defined already
try:
    elevation
except NameError:
    elevation = input("choose an elevation! type 2400, 2500 or 2600")
    print("OK")
else:
    print("elevation is already defined")

# make a list of all frames in the "pics2400", "pics2500" or "pics2600" folder
frames = []
imgs = glob.glob('pics' + str(elevation) + '/*.png') 
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
    print(i) # just to get some feedback while it is working


# Save into a GIF file that loops (forever --> loop=0)
frames[0].save(('GIF_' + str(elevation) + '.gif'), format='GIF',
               append_images=frames[:],  # number and range of appended frames can be limited (i.e. in case of difficulty with memory) 
               save_all=True,
               duration=0.05, loop=0) # set time for eacht frame (duration) and how often the GIF will be repeated (0 --> forever)
frames = []

print('your gif ' + '"GIF' + str(elevation) + '"' + ' is now ready in ' + str(dir_path))
