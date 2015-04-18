__author__ = "posixroot"


import tornado.web
import json
from database_controller import DatabaseController

class CogoHandler(tornado.web.RequestHandler):

    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        db_name = 'curio'
        dbc = DatabaseController()

        station_details_query = "SELECT station_id, station_name, \
            lat, lng FROM cogo_stations;"

        station_details = dbc.fetch_records(db_name, \
            station_details_query)

        station_availability_query = "SELECT station_id, \
                    available_docks, total_docks, \
                    available_bikes, avail_time FROM \
                    cogo_station_status;"

        station_availability = dbc.fetch_records(db_name, \
            station_availability_query)

        result = {}


        self.write(json.dumps(result))
