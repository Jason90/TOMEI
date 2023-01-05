import json
import requests


def post(url,data=None,headers=None):
    if (headers==None):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response=requests.post(url, data=data, headers=headers)

    return response