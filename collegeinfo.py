import re

class Colleges():

    def __init__(self):
        self.DBNAME = 'maniyak.colleges'
        self.GENERALINFO = 'mapsData/hd2014.csv'
        self.SCHOOLS = {}

    def setupTables(self):
        f = open(self.GENERALINFO, 'r')
        colleges = f.readlines()

        for index in range(0, len(colleges)):
            if(index > 0):
                # Do Work Here
                replace_quotes = ''.join([re.sub(',', ';', element) if element[len(element)-1] != ',' and element[0] != ',' else element for element in colleges[index].split('\"')])
                info = replace_quotes.split(',')

                try:
                    unitid = info[0]
                    name = info[1]

                    address = ', '.join(info[2:5])
                    admin_url = info[15]
                    size = int(info[54])
                    lat = float(info[66])
                    lon = float(info[65])


                except ValueError:
                    info[1]
                    for p in range(0, len(info)):
                        print str(p) + ") " + info[p]

            else:
                continue