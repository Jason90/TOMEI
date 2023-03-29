import re
import json
from business.base import Base
from model.tom import TOM

from util import regexutil


class CD1002(Base):

   def __init__(self):
      super(CD1002,self).__init__("cbs/cd1002.json", TOM.config.url.cd1002)

 
   #123
