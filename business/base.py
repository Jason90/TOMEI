from util import serializeutil

class Base:

    def __init__(self,name):
        self.data=serializeutil.load(name)