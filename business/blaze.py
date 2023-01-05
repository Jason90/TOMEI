import re
import json
from business.base import Base
from util import httputil
from util import regexutil

class Blaze(Base):

   def __init__(self):
      super(Blaze,self).__init__("blaze.json")#todo:自动获取文件名
      
   def query(self):
      self.response=httputil.post(self.data.url,vars(self.data.request)) #vars 将object转换dict
      return self.response
   
   def getproperty(self,tag):
      pattern='(?<={0}=")[^"]*'.format(tag)
      return regexutil.match(pattern,self.response.text)
   