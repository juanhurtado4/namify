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

class Signup(Resource):

    def post(self):
        user = request.json
        user_collection = app.db.users
        add_user = user_collection.insert_one(user)
    
class Login(Resource):

    def post(self):
        client_username = request.json['username']
        client_pass = request.json['password']
        user_collection = app.db.users        
        user = user_collection.find_one({"username": client_username})
        pdb.set_trace()
        if user['password'] == client_pass:
            return user
        else:
            response = jsonify(data=[])
            response.status_code = 404
            return response

def get(self):
    username = request.args.get('username')
    user_collection = app.db.users
    user = user_collection.find_one({'username': username})
    # pdb.set_trace()
    if user == None:
        response = jsonify(data=[])
        response.status_code = 404
        return response
    else:
        return user

@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(dumps(data), code)
    resp.headers.extend(headers or {})
    return resp


api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')


if __name__=='__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)