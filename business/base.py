from util import serializeutil

class Base:

    def __init__(self,name):
        self.request=serializeutil.load(name)