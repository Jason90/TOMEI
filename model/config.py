from objdict import ObjDict
from util import fileutil

class Config(ObjDict):
    #单例模式
    def __new__(self, *args, **kwargs):
        if not hasattr(self,'_instance'):
            self._instance= ObjDict(fileutil.read('data/config.json'))

        return self._instance


        
    