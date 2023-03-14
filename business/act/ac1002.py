from business.base import Base
from util import httputil
from util import serializeutil
from model.tom import TOM


class AC1002(Base):
   """aps征信进件接口
   """
   def __init__(self):
      super(AC1002,self).__init__("aps/ac1002.xml")

   #todo:对case装饰器加载测试数据
   #todo:query 放到父类,需重构只有url不同
   def query(self):
      headers = {'Content-Type': 'application/xml;charset=utf-8'}
      req=serializeutil.jsontoxml(self.request.dumps())
      res=httputil.post(TOM.config.url.ac1002 ,req,headers)
      self.response=serializeutil.loadxmls(res.text) 
      return self.response
   
   # def aps(self,tag):
   #    return True

   # def blacklist(self,tag):
   #    return True
   
   # def risk(self):
   #    return True

   # def incomplete(self):
   #    return True