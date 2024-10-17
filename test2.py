import getLocation
import random

mapdata = getLocation.getLocations()

NamedLocation = getLocation.FindNamedLocation(mapdata.data,True)
location = random.choice(NamedLocation)
print(location.name)