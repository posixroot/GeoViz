__author__ = "posixroot"

import tornado.web

class MainPageHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('webcontent/start.html')
