from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash #built in password hashing to increase security of my app
from .models import User
from .import db
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login') #define routes
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST']) #assign POST method for passing user data
def login_post():
    email = request.form.get('email') #grab user emial & password
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first() #check the users email first

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again') #flash error message
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.profile')) #if all user details match what is saved in the db, log them in and display their profile

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email') #get data from form
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))
    #assign new user data & hash passowrd for increased security
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))#sha256 is the hashing method to hash the users password

    db.session.add(new_user)
    db.session.commit() #commit new user details into the database

    return redirect(url_for('auth.login'))

@auth.route('/logout') #end user session
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))