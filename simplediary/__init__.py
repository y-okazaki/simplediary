from flask import Flask

app = Flask(__name__)
app.config.from_object('simplediary.config')
app.config.from_pyfile('config.py')
