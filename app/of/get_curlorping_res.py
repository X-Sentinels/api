# -*-coding:utf-8-*-

import requests
import time
import json
from config import name, password, api_addr
from app.models import Curl_Res ,Ping_Res


def get_curl_rasp_res(endpointname):
    res1 = Curl_Res.query.order_by(Curl_Res.curl_id.desc()).first()
    print(res1.curl_id)

    res2 = Curl_Res.query.filter_by(curl_timestamp=res1.curl_timestamp,curl_endpoint=endpointname).order_by(Curl_Res.curl_value.desc()).all()
    # print(res2.curl_timestamp)

    res_list = []

    for re in res2:
        temp = {}
        temp['curl_endpoint'] = re.curl_endpoint
        temp['curl_ipversion'] = re.curl_ipversion
        temp['curl_targeturl'] = re.curl_targeturl
        temp['curl_timestamp'] = re.curl_timestamp
        temp['curl_value'] = re.curl_value
        res_list.append(temp)


    for re in res_list:
        print(re)

    return res_list

def get_ping_rasp_res(endpointname):
    res1 = Ping_Res.query.order_by(Ping_Res.ping_id.desc()).first()
    print(res1.ping_id)

    res2 = Ping_Res.query.filter_by(ping_timestamp=res1.ping_timestamp,ping_endpoint=endpointname).order_by(Ping_Res.ping_value.desc()).all()
    # print(res2.curl_timestamp)

    res_list = []

    for re in res2:
        temp = {}
        temp['ping_endpoint'] = re.ping_endpoint
        temp['ping_ipversion'] = re.ping_ipversion
        temp['ping_targeturl'] = re.ping_targeturl
        temp['ping_timestamp'] = re.ping_timestamp
        temp['ping_value'] = re.ping_value
        res_list.append(temp)


    for re in res_list:
        print(re)

    return res_list


def get_curl_res():
    res1 = Curl_Res.query.order_by(Curl_Res.curl_id.desc()).first()
    print(res1.curl_id)

    res2 = Curl_Res.query.filter_by(curl_timestamp=res1.curl_timestamp).order_by(Curl_Res.curl_value.desc()).all()
    # print(res2.curl_timestamp)

    res_list = []
    count = 0
    for re in res2:
        temp = {}
        temp['curl_endpoint'] = re.curl_endpoint
        temp['curl_ipversion'] = re.curl_ipversion
        temp['curl_targeturl'] = re.curl_targeturl
        temp['curl_timestamp'] = re.curl_timestamp
        temp['curl_value'] = re.curl_value
        res_list.append(temp)
        if count == 7:
            break
        else:
            count=count+1

    for re in res_list:
        print(re)

    return res_list

def get_pie_arg():
    res1 = Curl_Res.query.order_by(Curl_Res.curl_id.desc()).first()
    print(res1.curl_id)

    res2 = Curl_Res.query.filter_by(curl_timestamp=res1.curl_timestamp).order_by(Curl_Res.curl_value.desc()).all()

    resdict={
    'num1':0,
    'num2':0,
    'num3':0,
    'num4':0,
    'num5':0,
    }

    print(resdict)
    for re in res2:
        if int(re.curl_value) <= 10:
            resdict['num1']+=1
        elif int(re.curl_value) > 10 and int(re.curl_value) <= 50:
            resdict['num2'] += 1
        elif int(re.curl_value) > 50 and int(re.curl_value) <= 100:
            resdict['num3'] += 1
        elif int(re.curl_value) > 100 and int(re.curl_value) <= 200:
            resdict['num4'] += 1
        else:
            resdict['num5'] += 1
    print(resdict)
    return resdict

# if __name__ == '__main__':
#     get_curl_res()
