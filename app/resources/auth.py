from flask import json, request
from flask_restful import Resource
from app.models import db, User
from .validators import email_validator,password_validator,user_name_validator
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


class RegisterResource(Resource):
    """
    Registration Resource with a POST method
    """
    def post(self):
        json_data = request.get_json(force=True)
        if 'user_name' not in json_data or \
             'user_email' not in json_data or 'password' not in json_data:
              return {"status": "Failed!",
               "data": "Please supply username, email and password"},406
        user = User.query.filter_by(user_email=json_data['user_email']).first()
        if not user:
            if not email_validator(json_data['user_email']):
                return {"status":"Failed!","data":"Please enter a valid email."}
            if not password_validator(json_data['password']):
                return {"status":"Failed!","data":"Too short password"}
            if not user_name_validator(json_data['user_name']):
                return {"status":"Failed!","data":"Please use a username without special characters."}
            User.admin = False
            if json_data['user_email'] == 'caterer@admin.com':
                User.admin = True
            account = User(user_name=json_data['user_name'],
                            user_email=json_data['user_email'],
                            password=json_data['password'])
            account.save()
            response = json.loads(json.dumps(account.json_dump()))
            return {"status": "success", "data": response}, 201
        else:
            return {"status":"Failed!","data":"Email already in use by existing user"}


class LoginResource(Resource):
    """
    Login Resource with a POST method
    """
    def post(self):
        """Login  post method"""
        json_data = request.get_json(force=True)
        # if not json_data:
        #     return {"status":"Failed!","data":"Please login with email and password"},401
        if 'user_email' not in json_data or 'password' not in json_data:
              return {"status": "Failed!",
               "data": "Please supply , email and password"},406
        if not email_validator(json_data['user_email']):
            return {"status":"Failed!","data":"Please enter a valid email"}

        user = User.query.filter_by(user_email=json_data['user_email']).first()
        if user and user.password_is_valid(json_data['password']):
            response = json.loads(json.dumps(user.json_dump()))
            access_token = create_access_token(identity=json_data['user_email'])
            return {"status": "success", 
            "data": response, "token":access_token}, 200
        return {"data":"Invalid login credentials"}

