from simplediary import bcrypt, db
from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True)
    _password = db.Column('password', db.String(140), nullable=False)
    diary = db.relationship("Diary", backref=db.backref('User'))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext).decode('utf-8')

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

class Pond(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pondname = db.Column(db.String(140), nullable=False)
    diary = db.relationship("Diary", backref=db.backref('Pond'))

class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seasonname = db.Column(db.String(140), nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    note = db.Column(db.Text)
    diary = db.relationship("Diary", backref=db.backref('Season'))

class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pond_id = db.Column(db.Integer, db.ForeignKey('pond.id'), nullable=False)
    season_id = db.Column(db.Integer, db.ForeignKey('season.id'), nullable=False)
    stock_number = db.Column(db.Integer)
    feeding = db.Column(db.String(140))
    report = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    update_date = db.Column(db.TIMESTAMP(), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    pond = db.relationship("Pond", backref=db.backref('Diary'))
    season = db.relationship("Season", backref=db.backref('Diary'))
    user = db.relationship("User", backref=db.backref('Diary'))
