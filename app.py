from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# config
import os
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

# import db schema
from models import *

# register blueprints
from project.users.views import users_blueprint
app.register_blueprint(users_blueprint)

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


if __name__ == '__main__':
    app.run()