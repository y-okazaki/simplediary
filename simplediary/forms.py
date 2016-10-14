from flask_wtf import Form
from wtforms.fields import TextField, TextAreaField, PasswordField, DateField
from wtforms.validators import Required, Email

from .util.validators import Unique
from .models import User, Pond, Season, Diary

class UserForm(Form):
    username = TextField('username', validators=[Required(message='ユーザー名を入力してください。')])
    email = TextField('email', validators=[Required(message='メールアドレスを入力してください。'),
                                Email(message='メールアドレスの書式が正しくありません。')])
    password = PasswordField('password', validators=[Required(message='パスワードを入力してください。')])

class UserEditForm(Form):
    username = TextField('username', validators=[Required(message='ユーザー名を入力してください。')])
    email = TextField('email', validators=[Required(message='メールアドレスを入力してください。'),
                                Email(message='メールアドレスの書式が正しくありません。')])
    password = PasswordField('password')

class PondForm(Form):
    pondname = TextField('pondname', validators=[Required(message='管理池名を入力してください。')])

class SeasonForm(Form):
    seasonname = TextField('seasonname', validators=[Required(message='シーズン名を入力してください。')])
    start_date = DateField('start_date', validators=[Required(message='シーズン開始年月日を入力してください。')])
    end_date = TextField('end_date')
    note = TextAreaField('note')

class DiaryForm(Form):
    pond_id      = TextField('pond_id', validators=[Required(message='養殖池IDを入力してください。')])
    season_id    = TextField('season_id', validators=[Required(message='シーズンIDを入力してください。')])
    stock_number = TextField('stock_number')
    feeding      = TextField('feeding')
    report       = TextAreaField('report')
    user_id      = TextField('user_id', validators=[Required(message='ユーザーIDを入力してください。')])
    date         = DateField('date', validators=[Required(message='日誌の年月日時を入力してください。')])
    created_date = TextField('created_date', validators=[Required(message='作成年月日時を入力してください。')])
