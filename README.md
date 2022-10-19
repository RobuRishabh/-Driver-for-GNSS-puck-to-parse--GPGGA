# Universal Transverse Mercator (UTM)
UTM is a projection, designed to display features on 2D surface. To get a better idea of what
UTM is, let’s do an experiement:
  1. Imagine a cylinder placed over earth
  2. Insert a light source inside it which projects the surface of the earth onto the walls of the
  cylinder.
  3. Then cut the cylinder into two halves and make it like a rectangular map.
  4. This is how we get the projection on a 2D surface. And, it is 6 ◦ segment of the earth. As, the
earth is spherical in shape.
```
360 ◦
= 60 Zones

6 ◦
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




# Driver-for-GNSS-puck-to-parse--GPGGA
Parsed the $GPGGA string for the latitude, longitude, and altitude. Converted the latitude and longitude to UTM. 
