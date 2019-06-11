#coding=utf-8

import time
import requests
# pip install requests
import json

def get_Apitoken(name, password, api_addr):
    d = {
        "name": name, "password": password,
    }

    h = {"Content-type":"application/json"}

    r = requests.post("%s/user/login" %(api_addr,), data=json.dumps(d), headers=h)

    if r.status_code != 200:
        raise Exception("%s %s" %(r.status_code, r.text))

    sig = json.loads(r.text)["sig"]
    return json.dumps({"name":name,"sig":sig})
