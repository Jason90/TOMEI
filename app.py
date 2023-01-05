from case.test_mail import test_sendmail
from case.test_blaze import test_blaze
import requests
import json

import sys
import os
path=os.getcwd() 
sys.path.append(path) #用于pytest自动发现测试案例，跨包引用

# print(path)
# print(sys.path)
if __name__ == "__main__":

    
    test_blaze()
    
    # test_sendmail()

    pass

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