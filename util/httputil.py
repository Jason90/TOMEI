import json
import requests

#todo:response to objDict by whether content-type contains json
def post(url,data=None,headers=None):
    if (headers==None):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    return requests.post(url, data=data.encode('utf8'), headers=headers)