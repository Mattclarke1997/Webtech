from flask_login import UserMixin   #adds extra attributes to my user class
from . import db

class User(UserMixin, db.Model): #define database fields
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))