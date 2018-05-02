from flask import json, request
from flask_restful import Resource
from app.models import db, Order


class OrderResource(Resource):
    """
    Order Resource with GET, POST, PUT and DELETE methods
    """

    def get(self):
        orders = Order.query.all()
        response = [order.json_dump() for order in orders]
        return {"status": "success", "data": response}, 200

    def post(self):
        json_data = request.get_json(force=True)
        order = Order(item_id=json_data['item_id'],user_id=json_data['user_id'],
                        quantity=json_data['quantity'])
        order.save()
        response = json.loads(json.dumps(order.json_dump()))
        return {"status": "success", "data": response}, 201

    def put(self, id):
        json_data = request.get_json(force=True)
        order = Order.query.filter_by(id=id).first()
        order.item_id = json_data['item_id']
        order.quantity = json_data['quantity']
        db.session.commit()
        response = order.json_dump()
        return{"status": "success", "data": response}, 200

    def delete(self, id):
        json_data = request.get_json(force=True)
        Order.query.filter_by(id=id).delete()
        db.session.commit()
        response = json.loads(json.dumps(json_data))
        return {"status": "deleted", "data": response}, 200
