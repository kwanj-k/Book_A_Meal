from flask import json, request,jsonify
from flask_restful import Resource,reqparse,abort
from models.models import Account,Db

class LoginResource(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        user = Db.get_user(email=json_data['email'],password=json_data['password'])
        if user:
            return {"status": "success"}, 200
        return "Account not registered, sign up"


class RegisterResource(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        account = Account(username=json_data['username'],
                    email=json_data['email'],
                    password=json_data['password'],
                    user_type=json_data['user_type'])
        if json_data['user_type'] == 1:
            Db.user_accounts.append(account)
        else:
            Db.caterer_accounts.append(account)
        res = "Your account is now registered please proceed to login" 
        return {"status": "success", "data": res}, 201  
        

        