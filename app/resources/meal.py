""" Meal resource to create all endpoints related to meals """

from flask import json, request
from flask_restful import reqparse,Resource
from flask_jwt_extended import (jwt_required,get_jwt_identity)

from app.models import db, Meal,User
from .validators import require_admin,name_validator,space_stripper

class MealResource(Resource):
    """
    Meal Resource with GET, POST, PUT and DELETE methods
    """
    
    @jwt_required
    @require_admin    
    def get(self, id):
        """
        Method gets a meal by id.
        """
        meal = Meal.query.filter_by(id=id).first()
        if meal is None:
            return {"status":"Failed!!",
            "message":"Meal does not exist."},404
        
        response = meal.json_dump()
        return response
    @jwt_required
    @require_admin
    def put(self, id):
        """
        Method updates meal.
        """
        json_data = request.get_json(force=True)
        if 'meal_name' not in json_data:
            return {"status":"Failed!","message":"Please provide a meal a name."},406
        meal_name = json_data['meal_name']
        meal = Meal.query.filter_by(id=id).first()
        if meal is None:
            return {"status":"Failed!!",
            "message":"Meal does not exist."},404
        if meal_name == '' or not name_validator(json_data['meal_name']):
            return {"status":"Failed!!",
            "message":"Meal name can not be empty or contain special characters."},406
        else:
            meal.meal_name =space_stripper(meal_name)
            db.session.commit()
            response = meal.json_dump()
            return{"status": "success", "data": response}, 200
    @jwt_required
    @require_admin
    def delete(self, id):
        """
         Method deletes a meal by id.
        """
        json_data = request.get_json(force=True)
        meal= Meal.query.filter_by(id=id).first()
        if  meal is None:
            return {"status":"Failed!!",
            "data":"Meal does not exist."},404
        else:
            Meal.query.filter_by(id=id).delete()
            db.session.commit()
            response = json.loads(json.dumps(json_data))
            return {"status": "deleted!", "data": response}, 200

class MealListResource(Resource):
    """
    MealList resource that has a get and post method.
    """
    @jwt_required
    @require_admin    
    def get(self):
        
        """
        Method to get all meals.
        """
        meals = Meal.query.all()
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
            return {"status":"Failed!","data":"Please provide a meal a name."},406
        meal_name = json_data['meal_name']
        if meal_name == '' or not name_validator(meal_name):
            return {"status":"Failed",
            "message":"Meal name can neither be empty nor contain special characters."},406
        meal = Meal(meal_name=meal_name)
        meal.save()
        response = json.loads(json.dumps(meal.json_dump()))
        return {"status": "success", "data": response}, 201

    
