from flask import render_template, request, redirect, url_for, flash
from simplediary import app, db
from simplediary.models import User, Pond, Season, Diary
from simplediary.forms import UserForm

@app.route('/')
def index():
    data = Diary.query.order_by('id desc')
    return render_template('index.html', diaries=data)

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm(request.form)
    if form.validate_on_submit():
        user = User()
        # print(request.form['password'])
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('user/add.html', form=form)
