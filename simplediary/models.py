from simplediary import db

class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_number = db.Column(db.Integer)
    feeding = db.Column(db.String(140))
    report = db.Column(db.Text)
    user = db.relationship("User", backref = db.backref('Diary'))
    date = db.Column(db.Date, nullable=False)
    update = db.Column(db.DateTime, nullable=False)
    created = db.Column(db.DateTime, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True)
    _password = db.Column('password', db.String(140), nullable=False)
