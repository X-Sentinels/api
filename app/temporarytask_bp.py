# -*-coding:utf-8-*-
from flask import Blueprint, request, render_template, redirect
from app.models import Map, Temporary_Ping_Res, Temporary_Curl_Res
from app import db
from app.of import get_history, get_dashboardnum, get_curlorping_res
import json
import time

from app.grpc_push.producer_ping import run as pingrun
from app.grpc_push.producer_curl import run as curlrun

temporarytask = Blueprint('temporarytask', __name__)


@temporarytask.route('/temporarytask_ping/', methods=['GET', 'POST'])
def temporarytask_ping():
    if request.method == 'GET':
        maplist = Map.query.filter_by().all()
        return render_template('temporarytask_ping.html', endpointlist=maplist)
    else:
        maplist = Map.query.filter_by().all()
        print(request.form.get('ipversion'))
        IPVERSION = request.form.get('ipversion')
        print(request.form.get('serialnum'))
        SERIALNUM = request.form.get('serialnum')
        serialnum = request.form.get('serialnum')
        print(request.form.get('endpoint_select'))
        NODE = request.form.get('endpoint_select')
        NODE = NODE + "_ping"
        print(request.form.get('targeturl'))
        TARGETURL = request.form.get('targeturl')
        print(request.form.get('packagesize'))
        PACKAGESIZE = request.form.get('packagesize')
        print(request.form.get('timeout'))
        TIMEOUT = request.form.get('timeout')
        print(request.form.get('count'))
        COUNT = request.form.get('count')
        print(NODE)
        MESSAGE = "ipversion:{0};serialnum:{1};targeturl:{2};packagesize:{3};timeout:{4};count:{5}".format(
            COUNT, SERIALNUM, TARGETURL, PACKAGESIZE, TIMEOUT, IPVERSION)
        print(MESSAGE)

        pingrun(NODE, IPVERSION, SERIALNUM, TARGETURL,
                PACKAGESIZE, TIMEOUT, COUNT)

        # print("====================")
        print(serialnum)
        print(type(serialnum))
        temp = serialnum.encode('utf-8')
        print(temp)

        time.sleep(10)
        return render_template('temporarytask_pingres.html', serialnum=temp)
        # return "OK"


@temporarytask.route('/temporarytask_curl/', methods=['GET', 'POST'])
def temporarytask_curl():
    if request.method == 'GET':
        maplist = Map.query.filter_by().all()
        return render_template('temporarytask_curl.html', endpointlist=maplist)
    else:
        print(request.form.get('serialnum'))
        SERIALNUM = request.form.get('serialnum')
        serialnum = request.form.get('serialnum')
        print(request.form.get('endpoint_select'))
        NODE = request.form.get('endpoint_select')
        NODE = NODE + "_curl"
        print(request.form.get('targeturl'))
        TARGETURL = request.form.get('targeturl')
        print(request.form.get('timeout'))
        TIMEOUT = request.form.get('timeout')
        print(request.form.get('ipversion'))
        IPVERSION = request.form.get('ipversion')

        curlrun(NODE, IPVERSION, SERIALNUM, TARGETURL, TIMEOUT)

        print(serialnum)
        print(type(serialnum))
        temp = serialnum.encode('utf-8')
        print(temp)

        time.sleep(10)

        return render_template('temporarytask_curlres.html', serialnum=temp)


@temporarytask.route('/post_temp_pingres/', methods=['GET', 'POST'])
def post_temp_pingres():
    if request.method == 'GET':
        pass
    else:
        print(request)
        print(request.get_json())
        res = request.get_json()
        print(res['ping_serialnum'])

        temppingres = Temporary_Ping_Res(
            ping_serialnum=res['ping_serialnum'],
            ping_averagetime=res['ping_averagetime'],
            ping_lossrate=res['ping_lossrate'],
            ping_maxtime=res['ping_maxtime'])
        # temppingres = Temporary_Ping_Res(ping_serialnum="asdfghjkl123456",ping_averagetime=3.33,ping_lossrate=0,ping_maxtime=10.0)

        db.session.add(temppingres)
        db.session.commit()

        return 'ok'


@temporarytask.route('/post_temp_curlres/', methods=['GET', 'POST'])
def post_temp_curlres():
    if request.method == 'GET':
        pass
    else:
        print(request)
        print(request.get_json())
        res = request.get_json()
        print(res['curl_serialnum'])

        tempcurlres = Temporary_Curl_Res(
            curl_serialnum=res['curl_serialnum'],
            curl_connect=res['curl_connect'],
            curl_httpcode=res['curl_httpcode'],
            curl_httpconnect=res['curl_httpconnect'],
            curl_nameloopup=res['curl_nameloopup'],
            curl_pretransfer=res['curl_pretransfer'],
            curl_redirect=res['curl_redirect'],
            curl_speeddownload=res['curl_speeddownload'],
            curl_total=res['curl_total'],
            curl_starttransfer=res['curl_starttransfer']
        )

        db.session.add(tempcurlres)
        db.session.commit()
        return 'ok'


@temporarytask.route('/ping_serialnum/', methods=['POST', 'GET'])
def ping_serialnum():
    if request.method == 'POST':
        serialnum = request.form.get('ping_serialnum')
        print(serialnum)

        TPR = None

        print(type(TPR))

        while(TPR is None):
            TPR = Temporary_Ping_Res.query.filter_by(
                ping_serialnum=serialnum).first()

        print(TPR.ping_averagetime)
        print(TPR.ping_lossrate)
        print(TPR.ping_maxtime)
        pingres = {}
        pingres["ping_averagetime"] = TPR.ping_averagetime
        pingres["ping_lossrate"] = TPR.ping_lossrate
        pingres["ping_maxtime"] = TPR.ping_maxtime
        pingres["ping_serialnum"] = TPR.ping_serialnum

        print(json.dumps(pingres))

        return json.dumps(pingres)


@temporarytask.route('/curl_serialnum/', methods=['POST', 'GET'])
def curl_serialnum():
    if request.method == 'POST':
        serialnum = request.form.get('curl_serialnum')
        print(serialnum)

        TCR = None

        print(type(TCR))

        while(TCR is None):
            TCR = Temporary_Curl_Res.query.filter_by(
                curl_serialnum=serialnum).first()

        # print(TCR.ping_averagetime)
        # print(TCR.ping_lossrate)
        # print(TCR.ping_maxtime)
        curlres = {}
        curlres["curl_serialnum"] = TCR.curl_serialnum
        curlres["curl_connect"] = TCR.curl_connect
        curlres["curl_httpcode"] = TCR.curl_httpcode
        curlres["curl_httpconnect"] = TCR.curl_httpconnect
        curlres["curl_nameloopup"] = TCR.curl_nameloopup
        curlres["curl_pretransfer"] = TCR.curl_pretransfer
        curlres["curl_redirect"] = TCR.curl_redirect
        curlres["curl_speeddownload"] = TCR.curl_speeddownload
        curlres["curl_total"] = TCR.curl_total
        curlres["curl_starttransfer"] = TCR.curl_starttransfer

        print(json.dumps(curlres))

        return json.dumps(curlres)
