from business.base import Base
from util import httputil
from util import serializeutil
from model.tom import TOM

class CR0020(Base):

   def __init__(self):
      super(CR0020,self).__init__("cbs/cr0020.json", TOM.config.url.cr0020)


   