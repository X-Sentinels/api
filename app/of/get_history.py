#-*-coding:utf-8-*-
from app.of.get_auth import get_Apitoken
import requests
import time
import json
from config import name,password,api_addr

Apitoken = get_Apitoken(name, password, api_addr)

# use endpoint_name & counter_name 获取过去60s的历史纪录
# endpoint_bp.py
def get_counter_history(endpoint_name, counter_name,interval):
    # Apitoken = {"sig": "848b171f88ee11e882ee005056bab49f", "name": "root"}
    # Apitoken = json.dumps(Apitoken)
    # print(Apitoken)
    print(endpoint_name)
    print(counter_name)

    end_time = int(time.time())
    start_time = end_time - interval

    h = {
        "Apitoken": Apitoken,
        "Content-Type": "application/json"
    }

    b = {
        "step": 60,
        "start_time": start_time,
        "hostnames": [
            endpoint_name
        ],
        "end_time": end_time,
        "counters":
            counter_name
        ,

        "consol_fun": "AVERAGE"
    }

    print("getcounterhistory------"+json.dumps(b))

    r = requests.post("%s/graph/history" % (api_addr,), data=json.dumps(b), headers=h)

    if r.status_code != 200:
        raise Exception("%s %s" % (r.status_code, r.text))

    # print("debug---"+r.text)
    # timelist,valuelist = get_front_list(json.loads(r.text))
    mydict = get_front_list(json.loads(r.text))
    # print(r.text)
    # return r.text
    # return json.dumps(timelist), json.dumps(valuelist)
    # print(mydict)
    # print(type(mydict))
    # print(json.dumps(mydict))
    #
    return json.dumps(mydict)
#

def get_front_list(res):
    # for zhexiantu
    time_list = []
    value_list = []
    # print(res)
    # print(res[0])
    # print(res[0]['Values'])
    # print(len(res[0]['Values']))
    for re in res[0]['Values']:

        # print(re['timestamp'])
        # print( time.strftime('%H:%M',time.localtime(re['timestamp'])) )
        time_list.append(time.strftime('%H:%M',time.localtime(re['timestamp'])))
        re['timestamp'] = time.strftime('%H:%M',time.localtime(re['timestamp']))
        # print(re['value'])
        value_list.append(re['value'])

    print(time_list)
    print(value_list)
    # return time_list,value_list
    return  res[0]['Values']



def get_counter_history2(endpoint_name, counter_name,interval):
    # Apitoken = {"sig": "848b171f88ee11e882ee005056bab49f", "name": "root"}
    # Apitoken = json.dumps(Apitoken)
    # print(Apitoken)
    print(endpoint_name)
    print(counter_name)

    end_time = int(time.time())
    start_time = end_time - interval

    h = {
        "Apitoken": Apitoken,
        "Content-Type": "application/json"
    }

    b = {
        "step": 60,
        "start_time": start_time,
        "hostnames": [
            endpoint_name
        ],
        "end_time": end_time,
        "counters":
            counter_name
        ,

        "consol_fun": "AVERAGE"
    }

    print("getcounterhistory------"+json.dumps(b))

    r = requests.post("%s/graph/history" % (api_addr,), data=json.dumps(b), headers=h)

    if r.status_code != 200:
        raise Exception("%s %s" % (r.status_code, r.text))

    # print("debug---"+r.text)
    # timelist,valuelist = get_front_list(json.loads(r.text))
    mydict = get_front_list2(json.loads(r.text))
    # print(r.text)
    # return r.text
    # return json.dumps(timelist), json.dumps(valuelist)
    # print(mydict)
    # print(type(mydict))
    # print(json.dumps(mydict))
    #
    temp1={}
    temp1['counter']="counternum"
    temp1['timestamp']=time.time()
    temp1['value']=len(mydict)
    mydict.append(temp1)

    temp1={}
    temp1['counter']="endpointname"
    temp1['timestamp']=time.time()
    temp1['value']=endpoint_name

    mydict.append(temp1)

    return json.dumps(mydict)
#

def get_front_list2(res):
    # time_list = []
    # value_list = []
    # # print(res)
    # # print(res[0])
    # # print(res[0]['Values'])
    # # print(len(res[0]['Values']))
    # for re in res[0]['Values']:
    #
    #     print(re['timestamp'])
    #     # print( time.strftime('%H:%M',time.localtime(re['timestamp'])) )
    #     time_list.append(time.strftime('%H:%M',time.localtime(re['timestamp'])))
    #     re['timestamp'] = time.strftime('%H:%M',time.localtime(re['timestamp']))
    #     # print(re['value'])
    #     value_list.append(re['value'])
    #
    # print(time_list)
    # print(value_list)
    # return time_list,value_list

    res_list=[]
    for re in res:
        temp={}
        # print(re['counter'])
        temp['counter']=re['counter']
        # print(time.strftime('%H:%M',time.localtime(re['Values'][0]['timestamp'])))
        # print(re['Values'][0]['timestamp'])
        temp['timestamp'] = re['Values'][0]['timestamp']
        # print(time.strftime('%H:%M', time.localtime(float(re['Values'][0]['timestamp']))))
        # print( time.localtime(re['Values'][0]['timestamp']))
        # print(re['Values'][0]['value'])
        temp['value'] = re['Values'][0]['value']
        res_list.append(temp)



    return  res_list
