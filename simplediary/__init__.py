from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('simplediary.config')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

import simplediary.models
