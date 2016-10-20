from flask import render_template, request, redirect, url_for, flash
from simplediary import app, db
from simplediary.models import User, Pond, Season, Diary
from simplediary.forms import UserForm, UserEditForm, UserLoginForm, PondForm, SeasonForm, DiaryForm, DiaryEditForm
from flask.ext.login import login_user, current_user, login_required, logout_user
import datetime

@app.route('/')
def index():
    data = Diary.query.order_by('id desc')
    return render_template('index.html', diaries=data)

@app.route('/user/', methods=['GET', 'POST'])
def user_list():
    user_list = User.query.order_by('id desc')
    return render_template('user/list.html', user_list=user_list)

@app.route('/user/signin', methods=['GET', 'POST'])
def signin():
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first_or_404()
        if user.is_correct_password(form.password.data):
            login_user(user)
            flash("ログインしました")
            return redirect(url_for('index'))
        else:
            return redirect(url_for('signin'))
    return render_template('user/signin.html', form=form)

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


@app.route('/pond/')
def pond_list():
    data = Pond.query.order_by('id desc')
    return render_template('pond/list.html', pond_list=data)

@app.route('/pond/add', methods=['GET', 'POST'])
def add_pond():
    form = PondForm(request.form)
    if form.validate_on_submit():
        pond = Pond()
        form.populate_obj(pond)
        db.session.add(pond)
        db.session.commit()
        return redirect(url_for('pond_list'))
    return render_template('pond/add.html', form=form)

@app.route('/pond/<pond_id>/edit', methods=['GET','POST'])
def edit_pond(pond_id):
    pond = Pond.query.filter_by(id=pond_id).first_or_404()
    form = PondForm(request.form, pond)
    if form.validate_on_submit():
        form.populate_obj(pond)
        db.session.add(pond)
        db.session.commit()
        return redirect(url_for('pond_list'))
    return render_template('pond/edit.html', form=form)

@app.route('/pond/<pond_id>/delete', methods=['GET', 'POST'])
def delete_pond(pond_id):
    pond = Pond.query.filter_by(id=pond_id).first_or_404()
    if request.method == 'POST':
        db.session.delete(pond)
        db.session.commit()
        return redirect(url_for('pond_list'))
    return render_template('pond/delete.html', pond=pond)

@app.route('/season/')
def season_list():
    data = Season.query.order_by('id desc')
    return render_template('season/list.html', season_list=data)

@app.route('/season/add', methods=['GET', 'POST'])
def add_season():
    form = SeasonForm(request.form)
    if form.validate_on_submit():
        if request.form["end_date"] == "":
            del form.end_date
        season = Season()
        form.populate_obj(season)
        db.session.add(season)
        db.session.commit()
        return redirect(url_for('season_list'))
    return render_template('season/add.html', form=form)

@app.route('/season/<season_id>/edit', methods=['GET', 'POST'])
def edit_season(season_id):
    season = Season.query.filter_by(id=season_id).first_or_404()
    form = SeasonForm(request.form, season)
    if form.validate_on_submit():
        if request.form["end_date"] == "":
            del form.end_date
        form.populate_obj(season)
        db.session.add(season)
        db.session.commit()
        return redirect(url_for('season_list'))
    return render_template('season/edit.html', form=form)

@app.route('/season/<season_id>/delete', methods=['GET', 'POST'])
def delete_season(season_id):
    season = Season.query.filter_by(id=season_id).first_or_404()
    if request.method == 'POST':
        db.session.delete(season)
        db.session.commit()
        return redirect(url_for('season_list'))
    return render_template('season/delete.html', season=season)

@app.route('/diary/')
def diary_list():
    data = Diary.query.order_by('id desc')
    return render_template('diary/list.html', diary_list=data)

@app.route('/diary/<diary_id>')
def detail_diary(diary_id):
    diary = Diary.query.filter_by(id=diary_id).first_or_404()
    return render_template('diary/detail.html', diary=diary)

@app.route('/diary/add', methods=['GET', 'POST'])
def add_diary():
    form = DiaryForm(request.form)
    if form.validate_on_submit():
        diary = Diary()
        form.populate_obj(diary)
        db.session.add(diary)
        db.session.commit()
        return redirect(url_for('diary_list'))
    return render_template('diary/add.html', form=form)

@app.route('/diary/<diary_id>/edit', methods=['GET', 'POST'])
def edit_diary(diary_id):
    diary = Diary.query.filter_by(id=diary_id).first_or_404()
    form = DiaryEditForm(request.form, diary)
    if form.validate_on_submit():
        form.populate_obj(diary)
        db.session.add(diary)
        db.session.commit()
        return redirect(url_for('detail_diary', diary_id=diary_id))
    return render_template('diary/edit.html', form=form)

@app.route('/diary/<diary_id>/delete', methods=['GET', 'POST'])
def delete_diary(diary_id):
    diary = Diary.query.filter_by(id=diary_id).first_or_404()
    if request.method == 'POST':
        db.session.delete(diary)
        db.session.commit()
        return redirect(url_for('diary_list'))
    return render_template('diary/delete.html', diary=diary)
