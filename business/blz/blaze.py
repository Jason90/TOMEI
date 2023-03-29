import re
import json
from business.base import Base
from util import httputil
from util import regexutil
from model.tom import TOM

class Blaze(Base):

   def __init__(self):
      super(Blaze,self).__init__("blz/blaze.xml", TOM.config.url.blaze)
      self.headers={'text/xml;charset=UTF-8'}