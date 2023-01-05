import os
import json
from xml.etree.ElementTree import fromstring
from xmljson import badgerfish as bf
from model import JsonObject


def load(file_name):
    ext=os.path.splitext(file_name)[1]
    if ext==".json":
        return loadjson(file_name)
    else:
        return loadxml(file_name)

def loadjson(file_name):
    with open(os.path.join(os.getcwd(),"data",file_name)) as f:
        jsonObj=json.load(f,object_hook=JsonObject)
        return jsonObj   

def loadxml(file_name):
    with open(os.path.join(os.getcwd(),"data",file_name)) as f:
        jsonObj=bf.data(fromstring(f.read()))
        return json.loads(json.dumps(jsonObj),object_hook=JsonObject)

def loadxmls(str):
    jsonObj=bf.data(fromstring(str))
    return json.loads(json.dumps(jsonObj),object_hook=JsonObject)