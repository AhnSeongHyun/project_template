__author__ = 'sh.ahn'

from project_base import *
from api_response_data import APIResponse

@app.route('/api',  methods=["GET"])
def api():
     return APIResponse(code=200)
