import re
import json
from business.base import Base
from util import httputil
from util import regexutil
from model.tom import TOM

class Blaze(Base):

   def __init__(self):
      super(Blaze,self).__init__("blz/blaze.json", TOM.config.url.blaze)
      
