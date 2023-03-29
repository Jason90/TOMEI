from case.test_mail import *
from case.blz.test_blaze import *
from case.act.test_ac1002 import *
from case.cbs.test_cd1002 import *
from case.cbs.test_cd1001 import *
import requests
import json

import sys
import os
path=os.getcwd() 
sys.path.append(path) #用于pytest自动发现测试案例，跨包引用
error_list=[]
from objdict import ObjDict #https://pypi.org/project/objdict/0.4.2/
# print(path)
# print(sys.path)
if __name__ == "__main__":
    # test_cd1001()
    test_cd1002()
    # test_act_aps()
    # test_blaze()
    pass


def objDict_test():
    with open(os.path.join(os.getcwd(),"data","test.json")) as f:
        dt=ObjDict(f.read())
        print (dt)
    jsonStr='{"name": {"first": "fred", "last": "blogs" }}'

    data = ObjDict(jsonStr)
    name = data['name'] # works, but as 'data' is not a real 'dict' not ideal
    name = data.name  # better
    first_name = data.name.first
    first_name = data["name"]["first"]  # works but again not ideal
    data.name.first='Jason'
    print(data.dumps())
    print()
    
def http_test():
    url="http://130.1.11.211/GBG.HRBCN.Activate.Blaze.WebService/BlazeQueryService.asmx/Query"

    datas = {"applicationNumber": "202212151000002", "sourceCode": "stag2"}

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response=requests.post(url,datas,headers)

    url="http://httpbin.org/get"
    data={"name":"jason","age":"40"}
    response=requests.get(url,params=data)

    print(type(response.text))
    print(response.json())
    print(json.loads(response.text))
    print(type(response.json()))
    print(response.json()['args'])


    url="http://httpbin.org/post"
    data={"name":"jason","age":"40"}
    response=requests.post(url,data=data)

    print(type(response.text))