#-*-coding:utf-8-*-
from flask import Blueprint,render_template,request,redirect,url_for
from app.models import Map
from app import db

map = Blueprint('map',__name__)

@map.route('/mapconfig/')
def mapconfig():
    maplist = Map.query.filter_by().all()

    # print(type(maplist))
    # print(maplist)
    # print(type(maplist[0]))
    # print(maplist[0].map_id)
    return render_template('map_config.html', maplists=maplist)


@map.route('/mapdetail/<mapid>/', methods=['GET', 'POST'])
def mapdetail(mapid):
    if request.method == 'GET':
        # print(mapid)
        map = Map.query.filter_by(map_id=mapid).first()
        # print(map[0])
        return render_template('map_detail.html', map=map)
    else:
        desc = request.form.get('map_desc')
        print(desc)
        if desc == '':
            return redirect(url_for('map.mapconfig'))
        else:
            map = Map.query.filter_by(map_id=mapid).first()
            map.map_desc = desc
            db.session.add(map)
            db.session.commit()
            return redirect(url_for('map.mapconfig'))