from flask import json, request,jsonify
from flask_restful import Resource,reqparse,abort
from app.models import Order,Db

class OrderResource(Resource):
    """
    Create a Order Resource with GET, POST, PUT and DELETE methods
    """
    def get(self):
        orders = Db.orders
        response = [order.json_dump() for order in orders]
        return {"status": "success", "data": response}, 200

    def post(self):
        json_data = request.get_json(force=True)
        order = Order(name=json_data['name'],
                        item=json_data['item'],
                        quantity=json_data['quantity'])
        Db.orders.append(order)
        response = json.loads(json.dumps(order.json_dump()))
        return {"status": "success", "data": response}, 201

    def put(self, id):
        json_data = request.get_json(force=True)
        order = Db.orders[id]
        Db.orders.remove(order)
        order = Order(name=json_data['name'],item=json_data['item'],quantity=json_data['quantity'])
        Db.orders.append(order)
        response = json.loads(json.dumps(order.json_dump()))
        return{"status": "success", "data": response}, 201

    def delete(self, id):
        json_data = request.get_json(force=True)
        meal = Db.meals[id]
        Db.meals.remove(meal)
        response = json.loads(json.dumps(json_data))
        return {"status": "deleted", "data": response}, 200