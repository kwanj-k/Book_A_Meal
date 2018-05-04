from flask import json, request
from flask_restful import Resource
from app.models import db, User
from .validators import email_validator,password_validator,user_name_validator,boolean_validator
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
        if 'username' not in json_data or \
             'email' not in json_data or 'password' not in json_data or 'is_admin' not in json_data:
              return {"status": "Failed!",
               "data": "Please supply username,email,password and whether admin"},406
        user = User.query.filter_by(email=json_data['email']).first()
        if not user:
            if not email_validator(json_data['email']):
                return {"status":"Failed!","data":"Please enter a valid email."}
            if not password_validator(json_data['password']):
                return {"status":"Failed!","data":"Too short password"}
            if not user_name_validator(json_data['username']):
                return {"status":"Failed!","data":"Please use a username without special characters."}
            if not user_name_validator(json_data['is_admin']) or boolean_validator(json_data['is_admin']) :
                return {"status":"Failed!","data":"Please use either True or Fale for the is_admin field."}
            account = User(username=json_data['username'],
                            email=json_data['email'],
                            is_admin=json_data['is_admin'],
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
        if 'email' not in json_data or 'password' not in json_data:
              return {"status": "Failed!",
               "data": "Please supply , email and password"},406
        if not email_validator(json_data['email']):
            return {"status":"Failed!","data":"Please enter a valid email"}

        user = User.query.filter_by(email=json_data['email']).first()
        if user and user.password_is_valid(json_data['password']):
            response = json.loads(json.dumps(user.json_dump()))
            access_token = create_access_token(identity=json_data['email'])
            return {"status": "success", 
            "data": response, "token":access_token}, 200
        return {"data":"Invalid login credentials"}

