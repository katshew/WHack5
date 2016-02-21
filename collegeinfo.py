import re

class Colleges():

    def __init__(self):
        self.GENERALINFO = 'mapsData/hd2014.csv'
        self.SCHOOLS = []
        self.setupInfo()

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

                    unitid = info[0]
                    name = info[1]
                    address = ', '.join(info[2:5])
                    admin_url = info[15]
                    size = int(info[54])
                    lat = float(info[66])
                    lon = float(info[65])

                    school['name'] = name
                    school['address'] = address
                    school['admin_url'] = admin_url
                    school['size'] = size
                    school['lat'] = lat
                    school['lng'] = lon

                    self.SCHOOLS.append(school)
                except ValueError:
                    continue

            else:
                continue

    def find_school_by_name(self, name):
        for school in self.SCHOOLS:
            if(name in school['name']):
                return school
        return None

    def get_coords_from_name(self, name):
        school = self.find_school_by_name(name)
        return (school['lat'], school['lng']) if school is not None else ()

    def get_url_from_name(self, name):
        school = self.find_school_by_name(name)
        return school['admin_url'] if school is not None else ''

    def get_size_category_from_name(self, name):
        school = self.find_school_by_name(name)
        return school['size'] if school is not None else ''