# -*- coding:utf-8 -*-
__author__ = 'sh.ahn'

from project_base import *

@app.route('/',  methods=["GET"])
def index():
     return render_template("index.html", title="project")
