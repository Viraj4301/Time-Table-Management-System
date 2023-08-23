from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Users = SQLAlchemy(app)

class User(Users.Model):
    id = Users.Column(Users.Integer, primary_key=True)
    name = Users.Column(Users.String(50), nullable=False)
    email = Users.Column(Users.String(50), unique=True, nullable=False)
    password = Users.Column(Users.String(50), nullable=False)

'''def __init__(self, name, email, password):
   self.name = name
   self.email = email
   self.password = password'''

with app.app_context():
    Users.create_all()
