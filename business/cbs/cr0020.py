from business.base import Base
from util import httputil
from util import serializeutil
from model.tom import TOM

class CR0020(Base):

   def __init__(self):
      super(CR0020,self).__init__("cbs/cr0020.json")

   def query(self):
      headers = {'Content-Type': 'application/json'}
      req=self.request.dumps()
      res=httputil.post(TOM.config.url.cr0020 ,req,headers) 
      self.response=serializeutil.loadjson(res.text) 
      return self.response

   