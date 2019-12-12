# 2019-frost-penetration-soils
Frost penetration in alpine solifluction lobes dependig on relative water content

The aim of this little project is to visualize data from field measurements in a video or a GIF.

A scheme of a solifluction lobe (.png) is colorized depending on measurement values of volumetric water content and temperature below ground.

## Prerequisits
- Python 3.7
- Have the file "Schema Blauberg weiss clean.png" in the working directory
- Have the file "alldata_utf8_ClShort.csv" also in the working directory
- Install dependencies:
  -  matplotlib
  -  pandas
  -  numpy
  -  Pillow
  -  imageio
  -  opencv-python
  
## How to use
- definde the timeframe of the data to be visualized in line 21 and line 22   
  - it is best to choose within:
  
    | Start     | End       |
    |-----------|-------    |
    |01.09.2015 |30.06.2017 |
    
    The default is set from 01.09.2015 18:00 to 02.09.2015 22:00 (40 hours / frames)
    
    One image will be created every hour within the timeframe unless defined differently (see section "What can be adjusted")
    
- there are three scripts
  - PrepFrames.py prepares frames to be packed in a video or gif with the other scripts
  - makeVideo.py packs the beforehand generated images (.png) to a video
  - makeGIF.py packs the beforehand generated images to a gif file
 
- if the video or the gif script is run subsequently to PrepFrames in the same console, the elevation will remain set. If a different console is used, the user is asked to define the elevation.
 
- The scripts can somehow not be executed entirely via the "run" button in PyCharm. Select all (Ctrl + A) and "run" works however.
  
 ## Results
  - you will find a folder with images in the working directory (one image each hour by default)
  - a video file or GIF file will be saved in the working directory
  
## What can be adjusted
- PrepFrames.py:
  - line 21 and line 22: time (default is 01.09.2015 18:00 to 02.09.2015 22:00)
  - line 25: elevation (dafault is 2400)
  - line 66: hours to skip (default is 1)
- makeVideo.py:
  - line 33: frames per second (default is 30)
- makeGIF.py:
  - line 34: duration: how many seconds one frame persists (default is 0.05)
  - line 34: loop: how many times the gif repeats (default is 0, infinite repetition)


Authors: Martina Hasler, Lukas Munz
