from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField, PasswordField
from wtforms.validators import Required, Email

from .util.validators import Unique
from .models import User, Pond, Season, Diary

class UserForm(Form):
    username = TextField('username', validators=[Required(message='ユーザー名を入力してください。')])
    email = TextField('email', validators=[Required(message='メールアドレスを入力してください。'),
                                Email(message='メールアドレスの書式が正しくありません。')])
    password = PasswordField('password', validators=[Required(message='パスワードを入力してください。')])
