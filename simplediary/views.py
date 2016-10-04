from flask import render_template, request, redirect, url_for, flash
from simplediary import app, db
from simplediary.models import User, Pond, Season, Diary

@app.route('/')
def index():
    data = Diary.query.order_by('id desc')
    return render_template('index.html', diaries=data)
