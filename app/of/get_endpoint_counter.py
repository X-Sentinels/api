#-*-coding:utf-8-*-
from app.of.get_auth import get_Apitoken
import requests
from config import name, password, api_addr,api_ip


Apitoken = get_Apitoken(name, password, api_addr)


def get_endpoint():
    """
    获取到json的所有节点的 节点名和id
    {
        "endpoint": "raspberry-01-li",
        "id": 995
    },
    :return:
    """
    print(Apitoken)
    h = {
        "Apitoken": Apitoken,
        "X-Forwarded-For": api_ip
    }

    d = {
        "q": "."
    }

    r = requests.get("%s/graph/endpoint" % (api_addr,), params=d, headers=h)

    if r.status_code != 200:
        raise Exception("%s %s" % (r.status_code, r.text))

    return r.text


def get_endpoint_counter(eidlist, metriclist):
    """
    获取到所有eidlist = 178
    所有metriclist = .
    的 counter 名称
    {
        "counter": "agent.alive",
        "endpoint_id": 178,
        "step": 60,
        "type": "GAUGE"
    },
    {
        "counter": "cpu.guest",
        "endpoint_id": 178,
        "step": 60,
        "type": "GAUGE"
    }
    :param eidlist:
    :param metriclist:
    :return:
    """
    print(Apitoken)
    d = {
        "eid": eidlist,
        "metricQuery": metriclist
    }
    h = {
        "Apitoken": Apitoken,
        "X-Forwarded-For": api_ip
    }
    r = requests.get("%s/graph/endpoint_counter" % (api_addr,), params=d, headers=h)
    if r.status_code != 200:
        raise Exception("%s %s" % (r.status_code, r.text))

    return r.text


