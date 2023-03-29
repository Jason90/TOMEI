from business.base import Base
from util import httputil
from util import serializeutil
from model.tom import TOM

class CD1018(Base):

   def __init__(self):
      super(CD1018,self).__init__("cbs/cd1018.xml")

   def query(self):
      headers = {'Content-Type': 'application/xml'}
      req=serializeutil.jsontoxml(self.request.dumps())
      res=httputil.post(TOM.config.url.cd1018 ,req,headers) 
      self.response=serializeutil.loadxmls(res.text) 
      return self.response
   