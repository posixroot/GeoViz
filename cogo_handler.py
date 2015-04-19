__author__ = "posixroot"


import tornado.web
import json
from database_controller import DatabaseController
from datetime import datetime

class CogoHandler(tornado.web.RequestHandler):

    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        db_name = 'curio'
        dbc = DatabaseController()

        result = {}
        result['station_details'] = []
        result['station_availability'] = []


        station_details_query = "SELECT station_id, station_name, \
            lat, lng FROM cogo_stations;"

        station_details = dbc.fetch_records(db_name, \
            station_details_query)

        for item in station_details['data']:
            row_list = item.split('*#*')
            result['station_details'].append(row_list)


        station_availability_query = "SELECT station_id, \
                    available_docks, total_docks, \
                    available_bikes, avail_time FROM \
                    cogo_station_status \
                    ORDER BY avail_time desc limit 30;"

        station_availability = dbc.fetch_records(db_name, \
            station_availability_query)

        time_fmt = '%Y-%m-%d %H:%M:%S'
        for item in station_availability['data']:
            row_list = item.split('*#*')
            # tstamp = datetime.strptime(row_list[4], time_fmt)
            result['station_availability'].append(row_list)


        self.write(json.dumps(result))
