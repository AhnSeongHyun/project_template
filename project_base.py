__author__ = 'sh.ahn'

# -*- coding:utf-8 -*-
__author__ = 'sh.ahn'

from flask import Flask

from commons.conf import Conf
from flask import render_template
from flask import request
from flask import jsonify
import server

from commons.conf import Conf

app = Flask(__name__, static_url_path="", static_folder="static")
app.config.update(
    DEBUG=True,
)

# read conf
project_conf = Conf.create_conf('./project.conf')




