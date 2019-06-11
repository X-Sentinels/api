#-*-coding:utf-8-*-
from app.of.get_auth import get_Apitoken
import requests
import json
from config import name, password, api_addr,api_ip
from app.models import Map
from app.of.get_endpoint_counter import get_endpoint, get_endpoint_counter

Apitoken = get_Apitoken(name, password, api_addr)


# dashboard page number

def get_endpoint_number():
    """
    获取所有endpoint的个数
    :return:
    """
    res = get_endpoint()
    if res is not None:
        return len(json.loads(res))
    else:
        return -1


def get_live_endpoint_number():
    """
    获取活着的节点的个数
    TD 需要更改
    :return:
    """
    # print(Apitoken)
    # eidlist = []
    # res = get_endpoint()
    # res = json.loads(res)
    #
    # for re in res:
    #     eidlist.append(re['id'])
    #
    # eidlist = ",".join('%s' % id for id in eidlist)
    #
    # res = get_endpoint_counter(eidlist, "agent.alive")
    #
    # return len(json.loads(res))

    maplist = Map.query.filter_by().all()
    if maplist is None:
        return -1
    else:

        count = 0
        for mapflag in maplist:
            # print(mapflag.map_desc)
            if mapflag.map_desc is not None:
                count = count + 1
        # print(count)
        # return len(maplist)
        return count


def get_pinglist_number():
    """
    获取 ping的个数
    :return:
    """
    path = "http://{}:3456/api/ping".format(api_ip)
    r = requests.get(path)

    if r.status_code != 200:
        # raise Exception("%s %s" % (r.status_code, r.text))
        return -1
    else:
        return len(json.loads(r.text))


def get_curllist_number():
    """
    获取 curl的个数
    :return:
    """
    path = "http://{}:3456/api/curl".format(api_ip)
    r = requests.get(path)

    if r.status_code != 200:
        # raise Exception("%s %s" % (r.status_code, r.text))
        return -1
    else:
        return len(json.loads(r.text))
