__author__ = "posixroot"

import tornado.web
import json
from database_controller import DatabaseController

class CensusHandler(tornado.web.RequestHandler):

    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        db_name = 'curio'
        dbc = DatabaseController()
        result = {}

        population_query = "SELECT fips, pop2013, \
            ST_AsGeoJSON(wkb_geometry) FROM \
            censustracts;"

        population = dbc.fetch_records(db_name, population_query)

        max_population = 0
        for item in population['data']:
            row_list = item.split('*#*')
            if max_population < row_list[1]:
                max_population = row_list[1]
            result['population'].append(row_list)

        result['max_population'] = max_population

        self.write(json.dumps(result))
