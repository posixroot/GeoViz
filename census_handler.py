__author__ = "posixroot"

import tornado.web
import json
from database_controller import DatabaseController

class CensusHandler(tornado.web.RequestHandler):

    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        db_name = 'curio'
        dbc = DatabaseController()
        connection_handle = dbc.connection(db_name)

        result = {}

        self.write(json.dumps(result))
