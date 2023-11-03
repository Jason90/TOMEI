import os
from model.const import FileType
from util import regexutil

def read(file_name) ->str:
    with open(os.path.join(os.getcwd(),file_name),mode="r", encoding="UTF-8") as f:
        return f.read()
    
def write(file_name,data) ->int:
    with open(os.path.join(os.getcwd(),file_name),mode="w", encoding="UTF-8") as f:
        return f.write(data)

def gettype(file_name) ->FileType:
    ext=os.path.splitext(file_name)[1]
    if ext==".json":
        return FileType.json
    else:
        return FileType.xml

def createdir(dir): 
    if not os.path.exists(dir):
        os.mkdir(dir)

def replace(file_name,source,target): 
    data=read(file_name)
    modify=regexutil.replace(data,source,target)
    write(file_name,modify)
    