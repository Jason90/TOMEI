import re

def match(pattern,str):
    matchObj=re.search(pattern,str)
    if matchObj:
        return matchObj.group(0)
    return None

# 从xml中查找某个属性值  
def getproperty(xml,tag):
    pattern='(?<={0}=")[^"]*'.format(tag)
    return match(pattern,xml)