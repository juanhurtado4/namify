import json
import pdb
from flask import Flask, request, jsonify, make_response
from pymongo import MongoClient
from bson import Binary, Code
from bson.json_util import dumps
from flask_restful import Resource, Api

app = Flask(__name__)
mongo = MongoClient('localhost', 27017)
app.db = mongo.namify
api = Api(app)

# TODO: Validate signup for empty pass or username
# TODO: Validate signup for username and pass length
# TODO: Validate signup for existing username

def display_bad_request(status_code):
    response = jsonify(data=[])
    response.status_code = status_code
    return response

class Collections:
    def __init__(self):
        self.user_collection = app.db.users
        self.image_collection = app.db.images

class Signup(Resource, Collections):

    def post(self):
        user = request.json
        if len(user['username']) < 2:

        pdb.set_trace()
        # user_collection = app.db.users
        # add_user = user_collection.insert_one(user)
        add_user = self.user_collection.insert_one(user)
    
class Login(Resource, Collections):

    def post(self):
        client_username = request.json['username'].lower()
        client_pass = request.json['password']
        # user_collection = app.db.users        
        # user = user_collection.find_one({"username": client_username})
        user = self.user_collection.find_one({"username": client_username})
        pdb.set_trace()
        if user['password'] == client_pass:
            return user
        else:
            return display_bad_request(404)

class Images(Resource, Collections):

    def get(self):
        # pdb.set_trace()
        gender = request.args.get('gender')
        if gender.lower() == 'male' or 'female':
            names_pics = self.image_collection.find({'gender': gender})
            pdb.set_trace()
            return names_pics
        else:
            return display_bad_request(404)            

@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(dumps(data), code)
    resp.headers.extend(headers or {})
    return resp


api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Images, '/images')


if __name__=='__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)