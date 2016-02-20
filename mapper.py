import googlemaps, re

class Mapper:

    def __init__(self):
        # I REALLY shouldn't be doing this but hackathon
        self.gmaps = googlemaps.Client(key="AIzaSyDlcYxUtGE4UL5hiuxjPN3wLwOkXVHeKig")
        self.DEFAULT_ADDRESS = '1000 Olin Way, Needham, MA'

    def get_address_from_college_name(self, college_name):
        # TODO turn this into a database
        f = open("mapsData/hd2014.csv")
        colleges = f.readlines()

        college_compare = college_name.lower()

        for college in colleges:
            info = college.split(',')
            if(college_compare in info[1].lower()):
                return self.build_address(info)

        return self.DEFAULT_ADDRESS

    def build_address(self, info):
        address = ', '.join(info[2:5])
        return re.sub("\"", "", address)

    def get_coords_from_name(self, query):
        address = self.get_address_from_college_name(query)
        result = self.gmaps.geocode(address)
        geo = result[0]["geometry"]["location"]
        coords = (geo["lat"], geo["lng"])

        return coords