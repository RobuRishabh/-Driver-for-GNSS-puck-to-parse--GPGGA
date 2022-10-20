# Universal Transverse Mercator (UTM)
UTM is a projection, designed to display features on 2D surface. To get a better idea of what
UTM is, let’s do an experiement:
  1. Imagine a cylinder placed over earth
  2. Insert a light source inside it which projects the surface of the earth onto the walls of the
  cylinder.
  3. Then cut the cylinder into two halves and make it like a rectangular map.
  4. This is how we get the projection on a 2D surface. And, it is 6॰ segment of the earth. As, the
earth is spherical in shape.
```
360॰ / 6॰ = 60 Zones
```
UTM establishes a set of coordinate system over the globe. East to West, cells are labelled
from 1 to 60 and centered over Greenwich, England.South to North cells are labelled from C
to X.
Using UTM Cells, the X-axis is called Easting and Y-axis is called Northing.
UTM Projection minimizes distortion within that zone. So this means that when you want to
show features in several UTM Zones, it starts becoming a poor choice of map projection.
In this Lab experiment using GPS puck, I got the longitude and latitude which I converted to
UTM Easting and UTM Northing values and did analysis of the data I got from GPS puck.

# Sources of Error
* **Orbit errors**
* **Satellite clocks**
* **Ionospheric delays**
* **Tropospheric delays**
* **Receiver Noise**
* **Multipath**

# Stationary and Walking Data Plots

  Scatter plot            |  Line plot             | 
:-------------------------:|:------------------------:|
| <img src="gpsdriver/data/Stationary_scatter.png" width=500px> | <img src="gpsdriver/data/Stationary_line.png" width=500px> | 
| <img src="gpsdriver/data/walking_scatter.png" width=500px> | <img src="gpsdriver/data/walking_line.png" width=500px> |

# Compensating Errors
Every error has it’s own way of compensating it, such as:
  1. For compensating Satellite clock error, one need to download precise satellite clock information from an spaced based augmentation system (SBAS) or         precise point positioning(PPP) service provider.
  2. Ionospheric and tropospheric Delays can be compensated by differential GNSS and RTK systems.
  3. The simplest way to reduce multipath errors is to place the GNSS antenna in a location that is away from the reective surface.


# Follow the steps to perform experiment of parsing the $GPGGA message from GNSS puck 
# 1. Set up the GPS puck
  If you are using a virtual machine, like virtual box, you may have to:
  1. Connect the USB.
  2. Go to the Settings of the VM
  3. Select the USB settings from the left pane
  4. Add the USB device in the list from by clicking on the icon
  5. Boot the VM with the USB device plugged in
  6. Make sure the device is selected/captured in USB settings (click on it) before you can see
  it in /dev/ttyUSB*
  When you will connect your GPS device, you can see the device name with this terminal
command.
```
$ ls –lt /dev/tty* | head
```
You will see a list of devices from which you have to figure out your device file identifier. Let us
say it is /dev/ttyUSB2. Run this command without the GPS plugged in, the missing COM port is your GPS device.
Then you need to set the read write permissions for reading the device properly.
```
$ sudo chmod 666 /dev/ttyUSB2
```

Get minicom with:
```
$ sudo apt install minicom
```
Configure your device’s settings in minicom:
```
$ sudo chmod 666 /etc/minicom
$ minicom -s
```
Go to serial port setup, Ctrl-a p, change the Bps/Par/Bits to “4800” and Hardware Flow Control
to “No”. You will have to scroll through a series of Bps values by selecting prev or next. For
example, if minicom is set to 9600 Bps then select prev to get 4800
Run minicom with : 
```
$ minicom
```
To save data to a text file, you need to use –C flag on minicom. In minicom, Ctrl-A brings up
your options, including to exit. Save as gps-data.txt. When you want to stop writing to the file,
press “Ctrl-a” and then “x”
To check the contents of the file: 
```
$ more gps_data.txt
```
# 2. Write a Device Driver for GNSS puck to parse $GPGGA
The GNSS puck provides several differently formatted messages. We will focus our attention on the messages that are formatted according to the $GPGGA format.
1. Ensure you can read the data from the puck (If you do not have the puck, you can use minicom as a virtual puck & the same driver should work with the real puck)
2. Parse the $GPGGA string for the latitude, longitude, and altitude. We have provided an example device driver for a depth sensor in the appendix section so that you can use that as a template
3. Convert the latitude & longitude to UTM.
4. Define a custom ROS message (called gps_msg.msg) with a Header, Latitude, Longitude, Altitude, UTM_easting, UTM_northing, Zone, Letter as fields.

- Please match the naming & capitalization
- Ensure correct data types.
- The Header is supposed to be a ROS Header data type. This is very important especially
when you start working with tfs and do sensor fusion in ROS
- The Latitude & Longitude are supposed to be signed floats.
- The ROS Header should contain the GPGGA time stamp & not your system time (as it may
be out of sync which could cause problems in a real-world system).
- The frame_ID should be a constant “GPS1_Frame” since our publisher is giving us data
from the solo GPS sensor we gave you.
5. Your ROS node should then publish this custom ROS message over a topic called /gps
6. You now have a working driver, let’s make it more modular. Name this GPS driver as gps_driver_try.py and add a feature to run this file with some argument. This argument will contain the path to the serial port of the GPS puck (example /dev/ttyUSB2 . Ofcourse the puck will not always be at the same port so it allows us to connect it anywhere without the script failing)
7. Even though this driver is now sufficiently modular, on a real robot we can have many sensors & launching their drivers individually can be too much work. This is where we shall use the power of ROS.
- Create a launch file called “driver.launch”
- This launch file should be able to take in an argument called “port” which we will specify
for the puck’s port.
- Have this launch file run your gps_driver.py with the argument that was passed when it was
launched.
- If you have done everything correctly, run the following command & you should get the
same results you were getting at 2.5
```
$ roslaunch driver.launch port:=”/dev/ttyUSB0” #Or basically any ttyUSB*
```
# 3. Go outside and collect data
1. Stationary data outdoors: In a new rosbag recording, go outside and collect 10 minutes ofdata at one spot. Name this rosbag “stationary_data.bag”
2. Walk in a straight line outdoors: In a new rosbag recording, walk in a straight line for a few
hundred meters. Name this rosbag “walking_data.bag”

# 4. Data analysis by plotting
1. Read the rosbag data into MATLAB (requires ROS toolbox) or python (make sure you install
bagpy with pip3 install bagpy, etc.):

References:
- https://jmscslgroup.github.io/bagpy/installation.html
- https://www.mathworks.com/help/ros/ref/rosbag.html
- https://www.mathworks.com/help/ros/ref/readmessages.html
