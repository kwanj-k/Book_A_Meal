from flask import json, request, jsonify
from flask_restful import Resource, reqparse, abort
from app.models import Meal, Db


class MealResource(Resource):
    """
    Create a Meal Resource with GET, POST, PUT and DELETE methods
    """

    def get(self):
        meals = Db.meals
        response = [meal.json_dump() for meal in meals]
        return {"status": "success", "data": response}, 200

    def post(self):
        json_data = request.get_json(force=True)

        meal = Meal(name=json_data['name'])
        Db.meals.append(meal)
        response = json.loads(json.dumps(meal.json_dump()))
        return {"status": "success", "data": response}, 201

    def put(self, id):
        json_data = request.get_json(force=True)
        meal = Db.get_meal_by_id(id)
        name = json_data['name']
        if meal:
            if name:
                meal.name = name
                response = json.loads(json.dumps(meal.json_dump()))
                return{"status": "success", "data": response}, 200
        return {"message": "Meal id does not exist"}

    def delete(self, id):
        json_data = request.get_json(force=True)
        meal = Db.get_meal_by_id(id)
        if meal:
            Db.meals.remove(meal)
            response = json.loads(json.dumps(json_data))
            return {"status": "deleted", "data": response}, 200
        return {"message": "Meal id does not exist"}
