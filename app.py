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
    monsters = db.relationship('Monster', backref='post')
    def __repr__(self):
        return '<User %r>' % self.username
        

class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokenum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    imageName = db.Column(db.String(80), unique=True, nullable=False)
    maxHp=db.Column(db.Integer, nullable=False)
    type=db.Column(db.Integer, nullable=False)
    speed=db.Column(db.Integer, nullable=False)
    attack=db.Column(db.Integer, nullable=False)
    defense=db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return '<User %r>' % self.name

class Battle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fid1=db.Column(db.Integer, db.ForeignKey('user.id')) #el id del jugador
    pid1=db.Column(db.Integer) #pokenum del monstruo
    php1=db.Column(db.Integer) #vida actual del monstruo
    fid2=db.Column(db.Integer, db.ForeignKey('user.id'))
    pid2=db.Column(db.Integer)
    php2=db.Column(db.Integer)
    fid3=db.Column(db.Integer, db.ForeignKey('user.id'))
    pid3=db.Column(db.Integer)
    php3=db.Column(db.Integer)
    fid4=db.Column(db.Integer, db.ForeignKey('user.id'))
    pid4=db.Column(db.Integer)
    php4=db.Column(db.Integer)
    fid5=db.Column(db.Integer, db.ForeignKey('user.id'))
    pid5=db.Column(db.Integer)
    php5=db.Column(db.Integer)
    turn=db.Column(db.Integer)
    def __repr__(self):
        return '<User %r>' % self.id

@app.route("/")
def showHomePage():
    return "This is home page"
@app.route("/post", methods=["POST"] )
def post():
    if request.method == "POST":
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
