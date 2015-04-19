#!/usr/bin/python

__author__ = "posixroot"


import os
import tornado
from cogo_handler import CogoHandler
from main_page_handler import MainPageHandler
from census_handler import CensusHandler

os.path.dirname(os.path.abspath(__file__))
application = tornado.web.Application([
    (r"/", MainPageHandler),
    (r"/cogomap/", CogoHandler),
    (r"/censusmap/", CensusHandler),
])


if __name__ == '__main__':
    application.listen(8880)
    tornado.ioloop.IOLoop.instance().start()
