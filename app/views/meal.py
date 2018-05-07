""" Meal resource to create all endpoints related to meals """

from flask import json, request
from flask_restful import reqparse, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models import db, Meal, User
from .validators import require_admin, name_validator, space_stripper


class Meals(Resource):
    """
    Meal Resource with GET, POST, PUT and DELETE methods
    """

    @jwt_required
    @require_admin
    def get(self, id):
        """
        Method gets a meal by id.
        """
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        meal = Meal.query.filter_by(id=id).first()
        if meal is None:
            return {"status": "Failed!!", "message": "Meal does not exist."}, 404
        if meal.user_id == current_user.id:
            response = meal.json_dump()
            return response
        return {"status": "Failed!", "message": "Meal does not exist."}, 404

    @jwt_required
    @require_admin
    def put(self, id):
        """
        Method updates meal.
        """
        json_data = request.get_json(force=True)
        if 'meal_name' not in json_data:
            return {"status": "Failed!", "message": "Please provide a meal a name."}, 406
        meal_name = json_data['meal_name']
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        meal = Meal.query.filter_by(id=id).first()
        if meal is None:
            return {"status": "Failed!!", "message": "Meal does not exist."}, 404
        if meal.user_id == current_user.id:
            if meal_name == '' or not name_validator(json_data['meal_name']):
                return {"status": "Failed!",
                        "message": "Meal name can not be empty or contain special characters."}, 406
            meal.meal_name = space_stripper(meal_name)
            db.session.commit()
            response = meal.json_dump()
            return{"status": "success", "data": response}, 200
        return {"status": "Failed!!", "message": "Meal does not exist."}, 404

    @jwt_required
    @require_admin
    def delete(self, id):
        """
         Method deletes a meal by id.
        """
        json_data = request.get_json(force=True)
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        meal = Meal.query.filter_by(id=id).first()
        if meal is None:
            return {"status": "Failed!!",
                    "data": "Meal does not exist."}, 404
        if meal.user_id == current_user.id:
            Meal.query.filter_by(id=id).delete()
            db.session.commit()
            response = json.loads(json.dumps(json_data))
            return {"status": "deleted!", "data": response}, 200
        return {"message": "Meal does not exist."}, 404


class MealList(Resource):
    """
    MealList resource that has a get and post method.
    """
    @jwt_required
    @require_admin
    def get(self):
        """
        Method to get all meals.
        """
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        meals = Meal.query.filter_by(user_id=current_user.id)
        if meals is None:
            return{"message": "You do not have meals at the moment."}, 404
        response = [meal.json_dump() for meal in meals]
        return {"status": "success", "data": response}, 200

    @jwt_required
    @require_admin
    def post(self):
        """
         Method creates a meal.
        """
        json_data = request.get_json(force=True)
        if 'meal_name' not in json_data:
            return {"status": "Failed!", "data": "Please provide a meal a name."}, 406
        meal_name = space_stripper(json_data['meal_name'])
        if meal_name == '' or not name_validator(meal_name):
            return {"status": "Failed",
                    "message": "Meal name can neither be empty nor contain special characters."}, 406
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        user_id = current_user.id
        meal = Meal(meal_name=meal_name, user_id=user_id)
        meal.save()
        response = json.loads(json.dumps(meal.json_dump()))
        return {"status": "success", "data": response}, 201
