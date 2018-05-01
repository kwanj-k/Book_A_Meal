from flask import json, request, jsonify
from flask_restful import Resource, reqparse, abort
from app.models import Account, Db


class LoginResource(Resource):
    """
    A login resource that provides post methods for login.
    """
    def post(self):
        json_data = request.get_json(force=True)

        user = Db.get_user(
            email=json_data['email'], password=json_data['password'])
        if user:
            return {"status": "success"}, 200
        return "Account not registered,please sign up"


class RegisterResource(Resource):
    """
    A Registration resource with post method for user registration.
    """
    def post(self):
        json_data = request.get_json(force=True)
        # username = json_data['username']
        # password  = json_data['password']
        # user_type = json_data['user_type']
        account = Account(username=json_data['username'],
                          email=json_data['email'],
                          password=json_data['password'],
                          user_type=json_data['user_type'])
        user2 = Db.get_user_info(
            email=json_data['email'], username=json_data['username'])
        if user2:
            return {"message": "Account is already registered, please proceed to login"}, 409
            # if username != '':
            #     if len(password) > 6:
            #         if user_type == 1 or user_type == 2:
        Db.user_accounts.append(account)
        res = "Your account is now registered please proceed to login"
        return {"status": "success", "data": res}, 201
