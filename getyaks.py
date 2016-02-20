from yaklient import *

def getYaksByCoords(latitude, longitude):
    user = User(Location(42.2964, -71.2931), "AB9126086390455FA9DA7BAFB95B0D81")
    yaks = user.get_yaks(Location(latitude, longitude))
    return yaks
