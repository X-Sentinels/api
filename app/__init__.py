from werkzeug.contrib.fixers import ProxyFix

from flask import Flask
from flask_bootstraps import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
app.wsgi_app = ProxyFix(app.wsgi_app)
bootstrap = Bootstrap(app)

from app import views