#functionality was developed following authentication and authorization - PrettyPrinted
#https://scotch.io/tutorials/authentication-and-authorization-with-flask-login?fbclid=IwAR0nHBWBstEnXh4bkKA-7BYscQySJYsL_vVgCcjyY2rHb77cbGCTrzi2WA8

from flask import Flask, render_template, Blueprint, url_for #this script handles my route redirects 
from flask_login import login_required, current_user

main = Blueprint('main', __name__)#assign my main blueprint

#creating the routes for templates
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required #only allows logged in users to visit this page
def profile():
    return render_template('profile.html', name=current_user.name)
