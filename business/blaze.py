import re
import json
from business.base import Base
from util import httputil
from util import regexutil
from model.tom import TOM

class Blaze(Base):

   def __init__(self):
      super(Blaze,self).__init__("blaze.json")#todo:自动获取文件名
      
   def query(self):
      self.response=httputil.post(TOM.config.url.blaze,self.data.dumps())
      return self.response
   
   def getproperty(self,tag):
      pattern='(?<={0}=")[^"]*'.format(tag)
      return regexutil.match(pattern,self.response.text)
   