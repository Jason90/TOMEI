import json
import requests

def post(url,data=None,headers=None):
    if (headers==None):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    return requests.post(url, data.encode('UTF-8') , headers=headers)