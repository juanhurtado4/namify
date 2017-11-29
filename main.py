from validate_signup import check_signup_pass, check_signup_username
from hash_password import make_hash_pass, check_hash_pass
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from bson.json_util import dumps
from pymongo import MongoClient
from bson import Binary, Code
import json
import pdb

# TODO: 
# Refactor Login class:
#     * Find username
#     * Check if username exist
#     * If not respond with 404
#     * Check if password is correct
#     * If not respond with 401
#     * If everything is correct respond with 200

app = Flask(__name__)
mongo = MongoClient('localhost', 27017)
app.db = mongo.namify
api = Api(app)

def display_response(status_code, json=None):
    return (json, status_code, None)

class Collections:
    def __init__(self):
        self.user_collection = app.db.users
        self.image_collection = app.db.images

class Signup(Resource, Collections):

    def post(self):
        username = request.json['username']
        password = request.json['password']
        existing_user = self.user_collection.find_one({'username': username})

        if existing_user != None:
            return display_response(409)
        # pdb.set_trace()
        if (check_signup_username(username) == False or 
            check_signup_pass(password) == False):
            return display_response(422)

        hash_pass = make_hash_pass(password)
        user = {'username': username, 'password': hash_pass, 'score': []}
        add_user = self.user_collection.insert_one(user)

        return display_response(201)
    
class Login(Resource, Collections):

    def get(self):
        client_username = request.authorization.username
        client_pass = request.authorization.password
        user = self.user_collection.find_one({"username": client_username})
        if user is None:
            return display_response(404)
        if check_hash_pass(client_pass, user['password']) == True:
            return display_response(200, user)

        return display_response(401)

class Images(Resource, Collections):

    def get(self):
        # pdb.set_trace()
        gender = request.args.get('gender')
        if gender.lower() == 'male' or 'female':
            names_pics = self.image_collection.find({'gender': gender})
            pdb.set_trace()
            return names_pics
        else:
            return display_response(400)            

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
