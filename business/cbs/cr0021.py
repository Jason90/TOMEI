from business.base import Base
from util import httputil
from util import serializeutil
from model.tom import TOM

class CR0021(Base):

   def __init__(self):
      super(CR0021,self).__init__("cbs/cr0021.json", TOM.config.url.cr0021)


   