from flask import json, request
from flask_restful import Resource
from app.models import db, Meal


class MealResource(Resource):
    """
    Meal Resource with GET, POST, PUT and DELETE methods
    """

    def get(self):
        meals = Meal.query.all()
        response = [meal.json_dump() for meal in meals]
        return {"status": "success", "data": response}, 200

    def post(self):
        json_data = request.get_json(force=True)
        meal = Meal(name=json_data['name'])
        meal.save()
        response = json.loads(json.dumps(meal.json_dump()))
        return {"status": "success", "data": response}, 201

    def put(self, id):
        json_data = request.get_json(force=True)
        meal = Meal.query.filter_by(id=id).first()
        meal.name = json_data['name']
        db.session.commit()
        response = meal.json_dump()
        return{"status": "success", "data": response}, 200

    def delete(self, id):
        json_data = request.get_json(force=True)
        Meal.query.filter_by(id=id).delete()
        db.session.commit()
        response = json.loads(json.dumps(json_data))
        return {"status": "deleted", "data": response}, 200
