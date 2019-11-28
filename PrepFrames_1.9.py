import os, errno
import matplotlib as mp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from matplotlib.patches import Circle, Polygon
import matplotlib.colors as colors

from datetime import datetime, timedelta

# set current directory as working directory
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
# os.chdir('C:/Users/User/Documents/geodataanalysis/soliflu')  # set working directory manually

file = pd.read_csv('alldata_utf8_ClShort.csv', sep=',') # load data
file['date.time'] = pd.to_datetime(file['date.time'], format='%d.%m.%Y %H:%M') # define date and time format in data

# choose the time for which data will be visualized --> from "starttag" to "endtag" (date and time must be definded)
starttag = datetime.strptime("01.09.2015 18:00", '%d.%m.%Y %H:%M')  # first possible: "01.09.2015"
endtag = datetime.strptime('02.08.2015 22:00', '%d.%m.%Y %H:%M')

# choose elevation for which data should be visualized (2400, 2500 or 2600)
elevation = 2400

# Create Folder, if it not already exists, to save frames which will be created later
try:
    os.makedirs('pics' + str(elevation))
except OSError as e:
    if e.errno == errno.EEXIST:
        print("Folder already exists")
    else:
        raise
Ordner = 'pics' + str(elevation) + '/'

cmap = plt.cm.get_cmap('coolwarm')
hmap = plt.cm.get_cmap('winter_r')
hnorm = mp.colors.Normalize(vmin=0, vmax=0.3)

# Center colorramp of temp at zero
class MidpointNormalize(colors.Normalize):
    def __init__(self, vmin=None, vmax=None, vcenter=None, clip=False):
        self.vcenter = vcenter
        colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        x, y = [self.vmin, self.vcenter, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))


midnorm = MidpointNormalize(vmin=-5, vcenter=0, vmax=5)

# load prapared image (scheme) to draw on
im = Image.open('Schema Blauberg weiss clean.png') 
size = im.size
sizeII = np.asarray(size)*0.5

subset = file.loc[(file['date.time'] >= starttag) & (file['date.time'] <= endtag) & (file['M_asl'] == elevation)]

# Make list with all time steps within the previously definded time
datumsliste = []
datum = starttag
while datum <= endtag:
    datumsliste.append(datum)
    datum = datum + timedelta(hours=1) # hours = hier können Zeitschritte übersprungen werden, hours= 2 --> jede 2. Stunde, ganze Zeile weg (#) --> jede halbe Stunde

# save images/ frames in the before created "pics" folder 
for i in datumsliste:
    pfad = (Ordner, str(elevation), i.strftime('_%Y.%m.%d_%H.%M'), '.png')
    BilderOrt = ''.join(pfad)
    if not os.path.exists(BilderOrt):  #  check if frame is already there
        try:  # in case of a missing time step in the data, go to next time step
            
            # create polygons depending on temperature
            temp1 = subset.loc[(subset['auf_unter'] == 'auf') & (i == subset['date.time'])]['C.Temp.1']
            temp2 = subset.loc[(subset['auf_unter'] == 'auf') & (i == subset['date.time'])]['C.Temp.2']
            temp3 = subset.loc[(subset['auf_unter'] == 'auf') & (i == subset['date.time'])]['C.Temp.3']
            temp4 = subset.loc[(subset['auf_unter'] == 'auf') & (i == subset['date.time'])]['C.Temp.4']
            temp5 = subset.loc[(subset['auf_unter'] == 'unter') & (i == subset['date.time'])]['C.Temp.1']
            temp6 = subset.loc[(subset['auf_unter'] == 'unter') & (i == subset['date.time'])]['C.Temp.2']
            temp7 = subset.loc[(subset['auf_unter'] == 'unter') & (i == subset['date.time'])]['C.Temp.3']
            temp8 = subset.loc[(subset['auf_unter'] == 'unter') & (i == subset['date.time'])]['C.Temp.4']

            polygon1 = Polygon([(1275+230, 530-90), (1350+230, 530-90), (1350+230, 590-90), (1275+230, 590-90)], True, color=cmap(midnorm(temp1.values[0])))
            polygon2 = Polygon([(1275+230, 610-90), (1350+230, 610-90), (1350+230, 670-90), (1275+230, 670-90)], True, color=cmap(midnorm(temp2.values[0])))
            polygon3 = Polygon([(1275+230, 690-90), (1350+230, 690-90), (1350+230, 750-90), (1275+230, 750-90)], True, color=cmap(midnorm(temp3.values[0])))
            polygon4 = Polygon([(1275+230, 770-90), (1350+230, 770-90), (1350+230, 830-90), (1275+230, 830-90)], True, color=cmap(midnorm(temp4.values[0])))

            polygon5 = Polygon([(1200-290, 530+780), (1275-290, 530+780), (1275-290, 590+780), (1200-290, 590+780)], True, color=cmap(midnorm(temp5.values[0])))
            polygon6 = Polygon([(1200-290, 610+780), (1275-290, 610+780), (1275-290, 670+780), (1200-290, 670+780)], True, color=cmap(midnorm(temp6.values[0])))
            polygon7 = Polygon([(1200-290, 690+780), (1275-290, 690+780), (1275-290, 750+780), (1200-290, 750+780)], True, color=cmap(midnorm(temp7.values[0])))
            polygon8 = Polygon([(1200-290, 770+780), (1275-290, 770+780), (1275-290, 830+780), (1200-290, 830+780)], True, color=cmap(midnorm(temp8.values[0])))
            
            # create round paches depending on water content values
            hum1 = subset.loc[(subset['auf_unter'] == 'auf') & (i == subset['date.time'])]['m3.m3.VWC.1']
            hum2 = subset.loc[(subset['auf_unter'] == 'auf') & (i == subset['date.time'])]['m3.m3.VWC.2']
            hum3 = subset.loc[(subset['auf_unter'] == 'auf') & (i == subset['date.time'])]['m3.m3.VWC.3']
            hum4 = subset.loc[(subset['auf_unter'] == 'auf') & (i == subset['date.time'])]['m3.m3.VWC.4']
            hum5 = subset.loc[(subset['auf_unter'] == 'unter') & (i == subset['date.time'])]['m3.m3.VWC.1']
            hum6 = subset.loc[(subset['auf_unter'] == 'unter') & (i == subset['date.time'])]['m3.m3.VWC.2']
            hum7 = subset.loc[(subset['auf_unter'] == 'unter') & (i == subset['date.time'])]['m3.m3.VWC.3']
            hum8 = subset.loc[(subset['auf_unter'] == 'unter') & (i == subset['date.time'])]['m3.m3.VWC.4']

            kreisli1 = Circle((1450, 470), radius=24, color=hmap(hnorm(hum1.values[0])))
            kreisli2 = Circle((1450, 550), radius=24, color=hmap(hnorm(hum2.values[0])))
            kreisli3 = Circle((1450, 630), radius=24, color=hmap(hnorm(hum3.values[0])))
            kreisli4 = Circle((1450, 710), radius=24, color=hmap(hnorm(hum4.values[0])))
            kreisli5 = Circle((850, 530+780+30), radius=24, color=hmap(hnorm(hum5.values[0])))
            kreisli6 = Circle((850, 610+780+30), radius=24, color=hmap(hnorm(hum6.values[0])))
            kreisli7 = Circle((850, 690+780+30), radius=24, color=hmap(hnorm(hum7.values[0])))
            kreisli8 = Circle((850, 770+780+30), radius=24, color=hmap(hnorm(hum8.values[0])))

            plt.ioff()  # prevent popping up of every single plot
            im = Image.open('Schema Blauberg weiss clean.png')
            fig = plt.figure()
            ax1 = plt.gca()
            
            # draw the before created patches
            ax1.add_patch(polygon1)
            ax1.add_patch(polygon2)
            ax1.add_patch(polygon3)
            ax1.add_patch(polygon4)
            ax1.add_patch(polygon5)
            ax1.add_patch(polygon6)
            ax1.add_patch(polygon7)
            ax1.add_patch(polygon8)

            ax1.add_patch(kreisli1)
            ax1.add_patch(kreisli2)
            ax1.add_patch(kreisli3)
            ax1.add_patch(kreisli4)
            ax1.add_patch(kreisli5)
            ax1.add_patch(kreisli6)
            ax1.add_patch(kreisli7)
            ax1.add_patch(kreisli8)
            
            # add colotbars
            im1 = ax1.imshow(im, cmap=cmap, norm=midnorm)
            cbar = fig.colorbar(im1, orientation='vertical', pad=-0.02, shrink=0.35)
            cbar.set_label('Temp\n°C', rotation=0, labelpad=5, fontsize=5)
            cbar.set_ticks([-5, 0, 5])
            cbar.ax.tick_params(labelsize=5)

            im2 = ax1.imshow(im, cmap=hmap, norm=hnorm)
            cbar1 = fig.colorbar(im2, orientation='vertical', pad=0.02, shrink=0.35)
            cbar1.set_label('VWC\n%', rotation=0, labelpad=5, fontsize=5)
            cbar1.set_ticks([0.0, 0.1, 0.2, 0.3])
            cbar1.ax.tick_params(labelsize=5)
            
            # add desctiption of the frame with time stamp and elevation
            date = i.strftime('%d.%m.%Y %H:%M')

            plt.text(100,100,1, text="Volumetric Water Content (VWC) and" + "\n" + "Temperature Below Ground", fontsize=7, weight='demibold')
            plt.text(100, 230, 1, text="Altitude: " + str(elevation) + " m a.s.l.", fontsize=7)
            plt.text(100, 480, 1, text=date[:10] + "\n" + date[11:], color='black', fontsize=7)

            ax1.set_axis_off()
            
            # save frame in the previously definded folder
            plt.savefig(BilderOrt, dpi=im.info['dpi'][0] * 0.75, bbox_inches='tight') # tight entfernt den weissen Rahmen um das Bild --> kleineres File

            print(i)
            plt.close()
        except:
            print(str(i) + ' is missing')
            continue
    else:
        if os.path.exists(BilderOrt):
            print('Frame ' + str(i) + ' already exists')

