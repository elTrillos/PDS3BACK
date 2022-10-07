from datetime import datetime
from unicodedata import category
from xmlrpc.client import DateTime

from flask import Flask, render_template, redirect, url_for, request, flash, session, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = 'super secret key'
db = SQLAlchemy(app)
app.app_context().push()



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def showHomePage():
    return "This is home page"
@app.route("/post", methods=["POST"] )
def post():
    value=request.form['value']
    return value

@app.route("/debug", methods=["POST"])
def debug():
    text = request.form["sample"]
    print(text)
    return "received"

if __name__ =="__main__":
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run()
