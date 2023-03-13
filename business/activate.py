from business.base import Base
from util import httputil
from model.tom import TOM

class Activate(Base):

   def __init__(self):
      super(Activate,self).__init__("Activate.xml")

   #todo:对case装饰器加载测试数据
   def aps(self):
      self.response=httputil.post(TOM.config.url.activate_aps ,self.data.dumps()) 
      return self.response
   
   def blacklist(self,tag):
      return True
   
   def risk(self):
      return True

   def incomplete(self):
      return True