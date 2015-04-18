#!/usr/bin/python

__author__ = "posixroot"


import os
import tornado
from map_page_handler import CogoHandler
from main_page_handelr import MainPageHandler

os.path.dirname(os.path.abspath(__file__))
application = tornado.web.Application([
    (r"/", MainPageHandler),
    (r"/cogomap/", CogoHandler),
    (r"/censusmap/" CensusHandler),
])


if __name__ == '__main__':
    application.listen(8880)
    tornado.ioloop.IOLoop.instance().start()
