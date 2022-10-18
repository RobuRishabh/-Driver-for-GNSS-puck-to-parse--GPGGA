import bagpy
from bagpy import bagreader
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sea
import pandas as pd

bag = bagreader('/home/rishabh/catkin_ws/src/gpsdriver/data/walking_data.bag')
bag.topic_table
data = bag.message_by_topic('/gps')
readings = pd.read_csv(data)
readings['UTM_easting'] = readings['UTM_easting'] - readings['UTM_easting'].min()
readings['UTM_northing'] = readings['UTM_northing'] - readings['UTM_northing'].min()
print(readings[['UTM_easting', 'UTM_northing']])
print(readings)
readings[['UTM_easting','UTM_northing']].plot()
fig, ax = bagpy.create_fig(1)
ax[0].scatter(x = 'UTM_easting', y = 'UTM_northing', data = readings, s= 50, label = 'UTM_easting VS UTM_northing')
for axis in ax:
    axis.legend()
    axis.set_xlabel('UTM_easting')
    axis.set_ylabel('UTM_northing')
plt.show()
