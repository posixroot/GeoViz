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


    def fetch_records(self, db_name, sql):
        result = {
            'type': "table",
            'record_count':0,
            'delimiter': '*#*',
            'data': []
        }
        conn = self.connection(db_name)
        cur = conn.cursor(
            cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(sql)
        rs = cur.fetchall()
        data = []
        for item in rs:
            str_data = ['NULL' if not x else str(x) for x in item]
            data.append('*#*'.join(str_data))
        result['record_count'] = len(data)
        result['data'] = data
        cur.close()
        conn.close()
        return result
