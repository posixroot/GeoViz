__author__ = "posixroot"

import psycopg2
import psycopg2.extras
from config import Config
from psycopg2._psycopg import ProgrammingError
from datetime import datetime
from config import Config

class DatabaseController(object):

    def __init__(self):
        self.config_details = Config().get_config()

    def connection(self, db_name):
        connection_string = 'host=\'localhost\' dbname=\'%s\' '\
            'user=\'%s\' password=\'%s\' port=\'%s\'' %(
            db_name, self.config_details['DB_USER'],
            self.config_details['DB_PASSWORD'],
            self.config_details['PORT']
            )
        connection_handle = psycopg2.connect(connection_string)
        return connection_handle
