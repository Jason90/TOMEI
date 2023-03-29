from business.base import Base
from util import httputil
from util import serializeutil
from model.tom import TOM


class AC1002(Base):
   """aps征信进件接口
   """
   def __init__(self):
      super(AC1002,self).__init__("aps/ac1002.xml", TOM.config.url.ac1002)

