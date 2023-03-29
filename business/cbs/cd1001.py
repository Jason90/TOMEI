from business.base import Base
from util import httputil
from util import serializeutil
from model.tom import TOM

class CD1001(Base):

   def __init__(self):
      super(CD1001,self).__init__("cbs/cd1001.xml", TOM.config.url.cd1001)


   