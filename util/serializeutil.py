import os
from objdict import ObjDict
import xmltodict
import json
from xml.etree.ElementTree import fromstring
from xmljson import badgerfish as bf
from model import JsonObject


from json import JSONEncoder


def load(file_name) ->ObjDict:
    ext=os.path.splitext(file_name)[1]
    if ext==".json":
        return loadjson(file_name)
    else:
        return loadxml(file_name)

def loadjson(file_name) ->ObjDict:
    with open(os.path.join(os.getcwd(),"data",file_name, encoding="UTF-8")) as f:
        return ObjDict(f.read())  

def loadxml(file_name) ->ObjDict:
    with open(os.path.join(os.getcwd(),"data",file_name), encoding="UTF-8") as f:
        return ObjDict(xmltojson(f.read()))

def loadxmls(str) ->ObjDict:
    return ObjDict(xmltojson(str))  

def xmltojson(str) ->str:
    dict = xmltodict.parse(str)
    return json.dumps(dict, ensure_ascii=False)

def jsontoxml(str) ->str:
    dict = json.loads(str)
    return xmltodict.unparse(dict)

def dicttoxml(dict) ->str:
    return xmltodict.unparse(dict)