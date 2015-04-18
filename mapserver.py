#!/usr/bin/python

__author__ = "posixroot"


import os
import tornado
from map_page_handler import MapPageHandler

os.path.dirname(os.path.abspath(__file__))
application = tornado.web.Application([
    (r"/", MapPageHandler),
])


if __name__ == '__main__':
    application.listen(8880)
    tornado.ioloop.IOLoop.instance().start()
