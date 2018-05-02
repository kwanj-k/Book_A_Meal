from flask import json, request
from flask_restful import Resource
from app.models import db, Menu


class MenuResource(Resource):
    """
    Menu Resource with GET, POST, PUT and DELETE methods
    """

    def get(self):
        menus = Menu.query.all()
        response = [menu.json_dump() for menu in menus]
        return {"status": "success", "data": response}, 200

    def post(self):
        json_data = request.get_json(force=True)
        menu = Menu(meal_id=json_data['meal_id'] ,item=json_data['item'])
        menu.save()
        response = json.loads(json.dumps(menu.json_dump()))
        return {"status": "success", "data": response}, 201

    def put(self, id):
        json_data = request.get_json(force=True)
        menu = Menu.query.filter_by(id=id).first()
        menu.item = json_data['item']

        db.session.commit()
        response = menu.json_dump()
        return{"status": "success", "data": response}, 200

    def delete(self, id):
        json_data = request.get_json(force=True)
        Menu.query.filter_by(id=id).delete()
        db.session.commit()
        response = json.loads(json.dumps(json_data))
        return {"status": "deleted", "data": response}, 200
