""" Authenitication resource for registration and login"""

from flask import json, request
from flask_restful import Resource
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity)

from app.models import db, User
from .validators import (email_validator,
                         password_validator,
                         user_name_validator,
                         space_stripper,
                         bool_transform)


class RegisterResource(Resource):
    """
    Registration Resource with a POST method
    """

    def post(self):
        json_data = request.get_json(force=True)
        if 'username' not in json_data or \
                'email' not in json_data or 'password' not in json_data or 'is_admin' not in json_data:
            return {"status": "Failed!",
                    "message": "Please supply username,email,password and whether admin"}, 406
        user = User.query.filter_by(email=json_data['email']).first()
        if not user:
            if not email_validator(json_data['email']):
                return {"status": "Failed!", "message": "Please enter a valid email."}, 406
            if not password_validator(json_data['password']):
                return {"status": "Failed!", "message": "Too short password"}, 406
            if not user_name_validator(json_data['username']):
                return {"status": "Failed!",
                        "message": "Username cannot be empty or have special characters."}, 406
            if not user_name_validator(json_data['is_admin']):

                return {"status": "Failed!",
                        "message": "Please use either True or False for the is_admin field."}, 406

            account = User(username=space_stripper(json_data['username']),
                           email=json_data['email'],
                           is_admin=bool_transform(json_data['is_admin']),
                           password=space_stripper(json_data['password']))
            account.save()
            response = json.loads(json.dumps(account.json_dump()))
            return {"status": "success", "data": response}, 201
        else:
            return {"status": "Failed!", "message": "Email already in use by existing user"}, 406


class LoginResource(Resource):
    """
    Login Resource with a POST method
    """

    def post(self):
        """Login  post method"""
        json_data = request.get_json(force=True)
        if 'email' not in json_data or 'password' not in json_data:
            return {"status": "Failed!",
                    "message": "Please supply , email and password"}, 406
        if not email_validator(json_data['email']):
            return {"status": "Failed!", "message": "Please enter a valid email"}, 406

        user = User.query.filter_by(email=json_data['email']).first()
        if user and user.password_is_valid(json_data['password']):
            response = json.loads(json.dumps(user.json_dump()))
            access_token = create_access_token(identity=json_data['email'])
            return {"status": "success",
                    "data": response, "token": access_token}, 200
        return {"message": "Invalid login credentials"}, 406
