import sqlite3 as lite
import re

class Colleges():

    def __init__(self):
        self.DBNAME = 'maniyak.colleges'
        self.GENERALINFO = 'mapsData/hd2014.csv'

        # self.CONN = lite.connect(self.DBNAME)
        # self.CONN.execute('''
        #     CREATE TABLE IF NOT EXISTS general (
        #         UNITID  TEXT    PRIMARY KEY     NOT NULL,
        #         NAME    TEXT                    NOT NULL,
        #         ADDRESS    TEXT                    NOT NULL,
        #         ADMINURL    TEXT,
        #         SIZE    INT,
        #         LAT     REAL                        NOT NULL,
        #         LONG    REAL                        NOT NULL);''')

        # self.setupTables()

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
                    name = re.sub('\"', '', info[1])

                    address = re.sub('\"', '', ', '.join(info[2:5]))
                    admin_url = re.sub('\"', '', info[15])
                    size = int(info[54])
                    lat = float(info[66])
                    lon = float(info[65])
                except ValueError:
                    info[1]
                    for p in range(0, len(info)):
                        print str(p) + ") " + info[p]

            else:
                continue