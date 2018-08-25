from flask import request, jsonify,render_template
from functools import wraps
from app import app
from .models import data_query


def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('X-API-KEY') and request.headers.get('X-API-KEY') == app.config["KEY"]:
            return view_function(*args, **kwargs)
        else:
            result = {"success":False,"msg":"missing X-API-KEY or KEY is Wrong"}
            return jsonify(result),401
    return decorated_function


@app.route('/api/ping', methods=['GET'])
# @require_appkey
def ping():
    results = data_query("args_ping")
    return jsonify(results)


@app.route('/api/curl', methods=['GET'])
# @require_appkey
def curl():
    results = data_query("args_curl")
    return jsonify(results)


@app.route('/index.html',methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/tables.html',methods=['GET','POST'])
def tables():
    return render_template('tables.html')


@app.route('/charts.html',methods=['GET','POST'])
def charts():
    return render_template('charts.html')


@app.route('/forms.html',methods=['GET','POST'])
def forms():
    return render_template('forms.html')
