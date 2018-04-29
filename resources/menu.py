from flask import json, request,jsonify
from flask_restful import Resource
from models.models import Menu,Db

class MenuResource(Resource):
    """
    Create a Menu Resource with GET, POST, PUT and DELETE methods
    """
    
    def get(self):
        menus = Db.menus
        response = [menu.json_dump() for menu in menus]
        return {"status": "success", "data": response}, 200

    def post(self):
        json_data = request.get_json(force=True)
        menu = Menu(meal=json_data['meal'], item=json_data['item'])
        Db.menus.append(menu)
        response = json.loads(json.dumps(menu.json_dump()))
        return {"status": "success", "data": response}, 201

