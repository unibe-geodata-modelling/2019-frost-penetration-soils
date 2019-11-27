# 2019-frost-penetration-soils
Frost penetration in alpine solifluction lobes dependig on relative water content

The aim of this little project is to visualize data from field masurements in a video or a GIF.

A scheme of a solifluction lobe (.png) is colorized depending on measurment values of volumetric water content and temperature below ground.

## Prerequisits
- Python 3.7
- Have the file "Schema Blauberg weiss clean.png" in the working directory
- Have the file "alldata_utf8.csv" also in the working directory
- Install dependencies:
  -  matplotlib
  -  pandas
  -  numpy
  -  Pillow
  -  imageio
  -  opencv-python
  
## How to use
- definde the timeframe of the data to be visualized in Line 21 and line 23   
  - it is best to choose within:
  
    | Start     | End       |
    |-----------|-------    |
    |01.09.2015 |30.06.2017 |
    
    One image will be created every houer within the timeframe unless definded differently (see section "What can be adjusted")
    
- there are three scripts
  - PrepFrames.py prepares frames to be packed in a video or gif with the other scripts
  - makeVideo.py packs the beforehand generated images (.png) to a video
  - makeGIF.py packs the beforehand generated images to a gif file
 
- The scripts can somehow not be executed entirely via the "run" button in PyCharm. Select all (Ctrl + A) and "run" works however.
  
 ## Result
  - you will find a folder with images in the working directory (one image each hour by default)
  - a video file or GIF file will be saved in the working directory
  
## What can be adjusted
  - time
  - elevation
  - fps (gif und video)
  - hours to skip

Authors: Martina Hasler, Lukas Munz
