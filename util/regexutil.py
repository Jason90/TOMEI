import re

def match(pattern,str):
    matchObj=re.search(pattern,str)
    if matchObj:
        return matchObj.group(0)
    return ''

# 从xml中查找某个属性值  
def get_xml_property(xml,tag)->str:
    pattern='(?<={0}=")[^"]*'.format(tag)
    return match(pattern,xml)

def get_xml_element(xml,tag) ->str:
    pattern='<{0}[^>]*?'.format(tag)
    return match(pattern,xml)

def get_xml_value(xml,tag) ->str:
    pattern='(?<=<{0}>)[^<]*'.format(tag)
    return match(pattern,xml)

def replace(str,pattern,repl)->str:
    return re.sub (pattern,repl,str)