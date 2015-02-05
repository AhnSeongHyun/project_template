# -*- coding:utf-8 -*-
__author__ = 'sh.ahn'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from project_base import *
from api.project_api import api
from views.project_view import index


if __name__ == '__main__':
    port = 8000
    server.start(app=app, port=project_conf.server.port)
