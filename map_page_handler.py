
__author__ = "posixroot"

import tornado.web
import json
# import psycopg2
# import psycopg2.extras
from psycopg2._psycopg import ProgrammingError
from database_controller import DatabaseController

class MapPageHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('webcontent/start.html')
        dbc = DatabaseController()
        connection_handle = dbc.connection('mydb')
