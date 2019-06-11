from flask_login import UserMixin
from . import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True, index=True)
    user_passwd = db.Column(db.String(256), index=True)
    user_admin = db.Column(db.Integer)

    @property
    def id(self):
        return self.user_id


class args_ping(db.Model):
    __tablename__ = 'args_ping'
    args_id = db.Column(db.Integer, primary_key=True)
    args_ipversion = db.Column(db.Integer)
    args_url = db.Column(db.String(100))
    args_packagesize = db.Column(db.Integer)
    args_count = db.Column(db.Integer)
    args_timeout = db.Column(db.Integer)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class args_curl(db.Model):
    __tablename__ = 'args_curl'
    args_id = db.Column(db.Integer, primary_key=True)
    args_ipversion = db.Column(db.Integer)
    args_url = db.Column(db.String(45))
    args_timeout = db.Column(db.Integer)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Map(db.Model):
    __tablename__ = 'map'
    map_id = db.Column(db.Integer, primary_key=True, nullable=False)
    map_desc = db.Column(db.String(255))
    map_ofid = db.Column(db.Integer, nullable=False)
    map_ofname = db.Column(db.String(255), nullable=False)


class Curl_Res(db.Model):
    __tablename__ = 'curl_res'
    curl_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    curl_endpoint = db.Column(db.String(255))
    curl_ipversion = db.Column(db.String(255))
    curl_targeturl = db.Column(db.String(255))
    curl_timestamp = db.Column(db.String(255))
    curl_value = db.Column(db.Float)


class Ping_Res(db.Model):
    __tablename__ = 'ping_res'
    ping_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    ping_endpoint = db.Column(db.String(255))
    ping_ipversion = db.Column(db.String(255))
    ping_targeturl = db.Column(db.String(255))
    ping_timestamp = db.Column(db.String(255))
    ping_value = db.Column(db.Float)

class Temporary_Ping_Res(db.Model):
    __tablename__ = 'temporary_pingres'
    ping_serialnum = db.Column(db.String(255) , primary_key=True, nullable=False)
    ping_lossrate = db.Column(db.String(255))
    ping_maxtime = db.Column(db.String(255))
    ping_averagetime = db.Column(db.String(255))


class Temporary_Curl_Res(db.Model):
    __tablename__ = 'temporary_curlres'
    curl_serialnum = db.Column(db.String(255) , primary_key=True, nullable=False)
    curl_httpcode = db.Column(db.String(255))
    curl_httpconnect = db.Column(db.String(255))
    curl_nameloopup = db.Column(db.String(255))
    curl_redirect = db.Column(db.String(255))
    curl_pretransfer = db.Column(db.String(255))
    curl_connect = db.Column(db.String(255))
    curl_starttransfer = db.Column(db.String(255))
    curl_speeddownload = db.Column(db.String(255))
    curl_total = db.Column(db.String(255))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
