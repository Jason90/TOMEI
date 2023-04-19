import os
from model.const import FileType

def read(file_name) ->str:
    with open(os.path.join(os.getcwd(),"data",file_name), encoding="UTF-8") as f:
        return f.read()


def gettype(file_name) ->FileType:
    ext=os.path.splitext(file_name)[1]
    if ext==".json":
        return FileType.json
    else:
        return FileType.xml
    