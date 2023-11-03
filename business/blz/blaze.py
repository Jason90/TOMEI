import re
import json
from business.base import Base
from util import httputil
from util import regexutil
from model.tom import TOM

class Blaze(Base):

   def __init__(self):
      super(Blaze,self).__init__("blz/blaze.xml", TOM.config.url.blaze)
      self.headers= {'Content-Type': 'text/xml; charset=utf-8'}
      # http post url"blaze":"http://130.1.11.211:8091/GBG.HRBCN.Activate.Blaze.WebService/BlazeQueryService.asmx/Query",-->
      
   def get_property(self,tag):
      return regexutil.get_xml_property(self.response_xml,tag)
   
   def has_element(self,tag) ->bool:
      return len(regexutil.get_xml_element(self.response_xml,tag))>0
   
   def __purify_response(self):
      xml=regexutil.get_xml_value(self.res.text,'QueryResult')
      xml=regexutil.replace(xml,'&lt;','<')
      xml=regexutil.replace(xml,'&gt;','>')
      xml=regexutil.replace(xml,'&amp;','&')
      xml=regexutil.replace(xml,'&apos;','\'')
      xml=regexutil.replace(xml,'&quot;','\"')
      xml=regexutil.replace(xml,'[\t\n]','')
      self.response_xml=xml
      return xml  
   
   
   def query(self):
      super(Blaze,self).query()
      self.__purify_response()