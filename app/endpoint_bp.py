#-*-coding:utf-8-*-
from flask import Blueprint,request,render_template,redirect
from app.models import Map
from app.of import get_history,get_dashboardnum,get_curlorping_res
import json,time


endpoint = Blueprint('endpoint',__name__)

@endpoint.route('/raspberry/pingres/',methods=['POST'])
def raspberry_pingres():
    endpoint_id = request.form.get('endpoint_id')
    map = Map.query.filter_by(map_ofid=endpoint_id).first()
    endpoint_name = map.map_ofname
    ping_res_list = get_curlorping_res.get_ping_rasp_res(endpoint_name)
    return json.dumps(ping_res_list)

@endpoint.route('/raspberry/curlres/',methods=['POST'])
def raspberry_curlres():
    endpoint_id = request.form.get('endpoint_id')
    map = Map.query.filter_by(map_ofid=endpoint_id).first()
    endpoint_name = map.map_ofname
    curl_res_list = get_curlorping_res.get_curl_rasp_res(endpoint_name)
    return json.dumps(curl_res_list)


@endpoint.route('/raspberry/',methods=['GET','POST'])
def raspberry():
    if request.method == 'GET':
        maplist = Map.query.filter_by().all()
        return render_template('raspberry_detail.html',endpointlist = maplist)
    else:
        print(request.form.get('endpoint_id'))
        endpoint_id = request.form.get('endpoint_id')
        counterlists = get_dashboardnum.get_endpoint_counter(endpoint_id, '.')
        counterlist = []
        print(counterlists)
        for re in json.loads(counterlists):
            print(re)
            counterlist.append(re['counter'])
            # counterlist = counterlist + ',' + re['counter']


        print(counterlist)

        counterlist1 = json.dumps(counterlist)
        counterlist2 = "'agent.alive', 'cpu.guest', 'cpu.idle'"
        print(counterlist1)

        map = Map.query.filter_by(map_ofid=endpoint_id).first()
        endpoint_name = map.map_ofname

        temp=counterlist
        res = get_history.get_counter_history2(endpoint_name,temp , 500)
        # temp1={}
        # temp1['counter']=endpoint_name
        # temp1['timestamp']=time.time()
        # temp1['value']=len(json.dumps(res))
        # temp2=[]
        # for re in res:
        #     temp2.append(re)
        # temp2.append(temp1)
        # res=[]
        # for counter in counterlist:
        #     re = get_history.get_counter_history(endpoint_name, counter, 500)
        #     print("========")
        #     print(json.loads(re)[0])
        #     print(json.loads(re)[0]['timestamp'])
        #     print(json.loads(re)[0]['value'])
        #     re_temp={}
        #     re_temp['endpoint']=counter
        #     re_temp['timestamp']=json.loads(re)[0]['timestamp']
        #     re_temp['value'] = json.loads(re)[0]['value']
        #     res.append(re_temp)
        #
        # for re in res:
        #
        #     print(re)
        #return render_template('raspberry_detail.html',counter_res=res)



        return json.dumps(res)
        #return render_template('raspberry_detail.html' ,counter_res= res)

@endpoint.route('/endpoint_detail/',methods=['GET','POST'])
def endpoint_detail():
    if request.method == 'GET':
        maplist = Map.query.filter_by().all()
        return render_template('endpoint_detail.html',endpointlist = maplist)
    else:
        print(request.form.get('endpoint_select'))
        print(request.getParameter('endpoint_select'))
        print(request.form.get('counter_select'))
        return render_template('endpoint_detail.html')

@endpoint.route('/counter/',methods=['POST','GET'])
def counter_list():
    # print(request.values)
    endpoint_id = request.form.get('endpoint_id')
    # print(endpoint_id)
    counterlist = get_dashboardnum.get_endpoint_counter(endpoint_id, '.')

    return counterlist

@endpoint.route('/counters/',methods=['POST','GET'])
def results_list():
    endpoint_id = request.form.get('endpoint_id')
    counter_name = request.form.get('counter_name')
    map = Map.query.filter_by(map_ofid = endpoint_id).first()
    endpoint_name = map.map_ofname
    counterlist=[]
    counterlist.append(counter_name)
    # print(endpoint_name)
    # print(counter_name)
    res = get_history.get_counter_history(endpoint_name, counterlist,3600)

    return res

@endpoint.route('/counter/detail/<endpoint_name>/<counter_name>',methods=['GET'])
def counter_detail(endpoint_name,counter_name):

    print(endpoint_name)
    print(counter_name)
    timelist ,valuelist = get_history.get_counter_history(endpoint_name,counter_name)
