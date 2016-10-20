from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from flask_bcrypt import Bcrypt
from flask.ext.login import LoginManager

csrf = CsrfProtect()

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('simplediary.config')
# 本番環境の設定に上書き（ルートにinstanceファルダを作りその中にconfig.pyを置く）
app.config.from_pyfile('config.py')
CsrfProtect(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

import simplediary.views
from simplediary.util import filters
from simplediary.models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/user/signin"

@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id==userid).first()
