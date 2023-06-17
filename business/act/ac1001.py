from business.base import Base
from util import httputil
from util import serializeutil
from model.tom import TOM


class AC1001(Base):
   """aps征信风控前置接口
   """
   def __init__(self):
      super(AC1001,self).__init__("aps/ac1001.xml", TOM.config.url.ac1001)

