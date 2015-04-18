__author__ = "posixroot"

from simplejson import loads

class Config(object):

    def __init__(self):
        self.config_details = {}
        # os.path.dirname(os.path.abspath(__file__))
        with open('config.json', 'r') as config_file:
            self.config_details = loads(config_file.read())

    def get_config(self):
        return self.config_details
