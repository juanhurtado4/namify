from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://namify:NewYorkCity@localhost:8889/namify'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    scores = db.relationship('Score', backref='owner')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return 'User({!r}, {!r})'.format(self.username, self.password)

class Score(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    db.Column(db.integer, db.Foreignkey('user.id'))
