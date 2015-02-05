__author__ = 'sh.ahn'
from flask import jsonify

http_status_messages={
    200:'OK',
    301:'Moved Permanently',
    304:'Not Modified',
    400:'Bad Request',
    401:'Unauthorized',
    403:'Forbidden',
    404:'Not Found',
    500:'Internal Server Error'
}

class ResponseBase(object):
    def to_dict(self):
        raise NotImplementedError("Need Implementation")

class APIResponse(ResponseBase):
    meta = None
    data = None

    def __init__(self, code=200, msg=None, data=None):
        self.meta = Meta(code=code, msg=msg)
        self.data = data

    def to_dict(self):
        result = dict()
        result["meta"] = self.meta.__dict__
        if self.data:
            result["data"] = self.data
        return result
    @property
    def json(self):
        return jsonify(self.to_dict()), self.meta.code


class Meta(object):
    code = None
    message = None

    def __init__(self, code=200, msg=None):
        self.code = code
        self.message = http_status_messages[code]
        if msg:
            self.message +="("+msg +")"

