# For refrence https://github.com/hastagAB/Awesome-Python-Scripts/blob/master/Location_Of_Adress/locator.py

#Requirements
#geocoder

import geocoder
t=input("enter the location:")
g = geocoder.arcgist(t)
print(g.latlng)
