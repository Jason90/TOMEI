import os
from util import serializeutil
from util import httputil
from model.tom import TOM
from objdict import ObjDict
from util import fileutil
from model.const import FileType


class Base:

    def __init__(self, name, url):
        self.dataType=fileutil.gettype(name)
        self.headers= {'Content-Type': 'application/{0}'.format(self.dataType.name)}
        self.request = serializeutil.load(name)
        self.name = name
        self.url = url

    def query(self):
        if self.dataType == FileType.json:
            req = self.request.dumps()
            res = httputil.post(self.url, req, self.headers)
            self.response = ObjDict(res.text)
            return self.response
        else:
            req = serializeutil.jsontoxml(self.request.dumps())
            res = httputil.post(self.url, req, self.headers)
            self.response = serializeutil.loadxmls(res.text)
            return self.response
