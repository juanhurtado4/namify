from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_restful import Resource, Api
import pdb

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://namify:NewYorkCity@localhost:8889/namify'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
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

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, score, user, date=None):
        self.score = score
        self.user = user
        if date == None:
            date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.date = date
    
    def __repr__(self):
        return 'Score {!r}, {!r}'.format(self.score, self.user)
'''
class Login(Resource):

    def Post(self):
        print(request.json)
'''
# @app.route('/signup', methods=['POST'])
# def signup():
#     request = request.json
#     return request
@app.route('/signup', methods=['GET'])
def signup():
    # user = User.query.filter_by(id=1).first()
    # request = request.json
    # pdb.set_trace()
    user = request.args.get('username', type=str)
    return user

if __name__=='__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run()