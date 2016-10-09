from flask import render_template, request, redirect, url_for, flash
from simplediary import app, db
from simplediary.models import User, Pond, Season, Diary
from simplediary.forms import UserForm, UserEditForm

@app.route('/')
def index():
    data = Diary.query.order_by('id desc')
    return render_template('index.html', diaries=data)

@app.route('/user/', methods=['GET', 'POST'])
def user_list():
    user_list = User.query.order_by('id desc')
    return render_template('user/list.html', user_list=user_list)


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

@app.route('/user/<user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    form = UserEditForm(request.form, user)
    if form.validate_on_submit():
        if request.form["password"] == "":
            del form.password
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('user/edit.html', form=form)
