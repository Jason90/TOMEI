from util import serializeutil
from util import httputil
from model.tom import TOM
import os
from objdict import ObjDict

class Base:
    
    def __init__(self,name,url):
        self.request=serializeutil.load(name)
        self.name=name
        self.url=url

    def query(self):
      ext_request=os.path.splitext(self.name)[1]
      if ext_request==".json":
        res=httputil.post(self.url,self.request.dumps(),
                                    headers={'Content-Type':'application/json'})
        self.response=ObjDict(res.text)
        return self.response
      else:
        headers = {'Content-Type': 'application/xml'}
        req=serializeutil.jsontoxml(self.request.dumps())
        res=httputil.post(self.url ,req,headers) 
        self.response=serializeutil.loadxmls(res.text) 
        return self.response         