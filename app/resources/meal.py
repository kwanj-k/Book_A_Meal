from flask import json, request
from flask_restful import reqparse,Resource
from app.models import db, Meal,User
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from .validators import require_admin,mealname_and__menuitem_validator


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
            "data":"Meal id does not exist.Please enter a valid meal id"}
        
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
            return {"status":"Failed!","data":"Please provide a meal a name."}
        meal_name = json_data['meal_name']
        meal = Meal.query.filter_by(id=id).first()
        if meal is None:
            return {"status":"Failed!!",
            "data":"Meal id does not exist.Please enter a valid meal id"}
        if meal_name == '' or not mealname_and__menuitem_validator(json_data['meal_name']):
            return {"status":"Failed!!",
            "data":"Meal name can not be empty.Please enter a valid meal name"}
        else:
            meal.meal_name = meal_name
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
            "data":"Meal id does not exist.Please enter a valid meal id"}
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
            return {"status":"Failed!","data":"Please provide a meal a name."}
        meal_name = json_data['meal_name']
        if meal_name == '':
            return {"status":"Failed",
            "data":"Meal name can not be empty.Please enter a valid meal name"}
        meal = Meal(meal_name=meal_name)
        meal.save()
        response = json.loads(json.dumps(meal.json_dump()))
        return {"status": "success", "data": response}, 201

    
