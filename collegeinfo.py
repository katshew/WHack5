# -*- coding: utf-8 -*-

import re, googlemaps

class Colleges():

    def __init__(self):
        self.GENERALINFO = "mapsData/hd2014.csv" #'/var/www/whack/whack/hd2014.csv'
        self.SCHOOLS = []
        self.setupInfo()

        # I REALLY shouldn't be doing this but hackathon        
        self.gmaps = googlemaps.Client(key="AIzaSyDlcYxUtGE4UL5hiuxjPN3wLwOkXVHeKig")

    def setupInfo(self):
        f = open(self.GENERALINFO, 'r')
        colleges = f.readlines()

        for index in range(0, len(colleges)):
            if(index > 0):
                # Do Work Here
                replace_quotes = ''.join([re.sub(',', ';', element) if element[len(element)-1] != ',' and element[0] != ',' else element for element in colleges[index].split('\"')])
                info = replace_quotes.split(',')

                try:
                    school = {}

                    school['name'] = info[1]
                    school['address'] = ', '.join(info[2:5])
                    school['admin_url'] = info[15]
                    school['size'] = int(info[54])
                    school['lat'] = float(info[66])
                    school['lng'] = float(info[65])

                    self.SCHOOLS.append(school)
                except ValueError:
                    continue

            else:
                continue

    def find_school_by_name(self, name):
        for school in self.SCHOOLS:
            if(name.lower() in school['name'].lower()):
                return school
        return None

    def get_coords_from_name(self, name):
        school = self.find_school_by_name(name)
        if(school is not None):
            return (school['lat'], school['lng'])
        else:
            result = self.gmaps.geocode(name)     
            geo = result[0]["geometry"]["location"]       
            return (geo["lat"], geo["lng"]) 

    def get_url_from_name(self, name):
        school = self.find_school_by_name(name)
        return school['admin_url'] if school is not None else ''

    def get_size_category_from_name(self, name):
        school = self.find_school_by_name(name)
        return school['size'] if school is not None else ''

    def get_school_information(self, name):
        school = self.find_school_by_name(name)
        return school if school is not None else {}
