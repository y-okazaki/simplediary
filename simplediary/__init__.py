from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from flask_bcrypt import Bcrypt

csrf = CsrfProtect()

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('simplediary.config')
app.config.from_pyfile('config.py')
CsrfProtect(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

import simplediary.views
from simplediary.util import filters
