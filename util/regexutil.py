import re

def match(pattern,str):
    matchObj=re.search(pattern,str)
    if matchObj:
        return matchObj.group(0)
    return None