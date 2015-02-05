# -*- coding:utf-8 -*-
__author__ = 'sh.ahn'

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop 
 

def start(app, port=8080):
    print('Server Start..' + str(port))
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port)
    IOLoop.instance().start()
    
def stop():
    print('Server Stop..')
    IOLoop.instance().stop()