from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user-system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Users = SQLAlchemy(app)

class timeTB(Users.Model):
    id = Users.Column(Users.Integer, primary_key=True, autoincrement = True)
    stime = Users.Column(Users.Integer)
    time = Users.Column(Users.Integer)
    venue = Users.Column(Users.String(50))
    course = Users.Column(Users.String(50))
    c_color = Users.Column(Users.String(50))
    whichday = Users.Column(Users.String(50))
    faculty = Users.Column(Users.String(50))


class User(Users.Model):
    id = Users.Column(Users.Integer, primary_key=True)
    name = Users.Column(Users.String(50), nullable=False)
    email = Users.Column(Users.String(50), unique=True, nullable=False)
    password = Users.Column(Users.String(50), nullable=False)
with app.app_context():
    Users.create_all()


