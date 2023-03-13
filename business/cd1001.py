from business.base import Base
from util import httputil
from model.tom import TOM

class CD1001(Base):

   def __init__(self):
      super(CD1001,self).__init__("cd1001.xml")

   def query(self):
      self.response=httputil.post(TOM.config.url.CD1001 ,self.data.dumps()) 
      return self.response
   