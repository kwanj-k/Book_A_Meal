from flask import json, request
from flask_restful import Resource
from app.models import db, User


class RegisterResource(Resource):
    """
    Registration Resource with a POST method
    """
    def post(self):
        json_data = request.get_json(force=True)
        account = User(email=json_data['email'],password=json_data['password'])
        account.save()
        response = json.loads(json.dumps(account.json_dump()))
        return {"status": "success", "data": response}, 201


class LoginResource(Resource):
    """
    Login Resource with a POST method
    """
    def post(self):
        json_data = request.get_json(force=True)
        user = User.query.filter_by(email=json_data['email']).first()
        if user and user.password_is_valid(json_data['password']):
            response = json.loads(json.dumps(user.json_dump()))
            return {"status": "success", "data": response}, 201
        return {"data":"Invalid login credentials."}