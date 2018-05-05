""" Order resource to define all orders endpoints"""

from flask import json, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.models import db, Order, Menu, Meal, User
from .validators import require_admin, num_check, name_validator


class Orders(Resource):
    """
    Order Resource with GET, POST, PUT and DELETE methods
    """

    @jwt_required
    def get(self, id):
        """
        Method gets a order by id.
        """
        order = Order.query.filter_by(id=id).first()
        if order is None:
            return {"status": "Failed!",
                    "message": "Order  does not exist."}, 404
        response = order.json_dump()
        return response

    @jwt_required
    def put(self, id):
        """
        Method updates order.
        """
        json_data = request.get_json(force=True)
        order = Order.query.filter_by(id=id).first()
        if order is None:
            return {"status": "Failed!",
                    "message": "Order does not exist."}, 404
        if 'user_id' not in json_data or \
                'item_id' not in json_data or 'quantity' not in json_data:
            return {"status": "Failed!",
                    "message": "Please supply user id, item id and quantity"}, 406
        if not num_check(json_data['item_id']) or not num_check(json_data['quantity']):
            return {"status": "Failed!", "meassage": "Meal_id,item_id and quantity must be integers."}, 406
        item = Menu.query.filter_by(id=json_data['item_id']).first()
        if item is None:
            return {"status": "Failed!",
                    "message": "Item does not exist."}, 404
        user = User.query.filter_by(id=json_data['user_id']).first()
        if user is None:
            return {"status": "Failed!!",
                    "message": "User does not exist.Please enter a valid User id"}, 404
        else:
            order.user_id = json_data['user_id']
            order.item_id = json_data['item_id']
            order.quantity = json_data['quantity']
            db.session.commit()
            response = order.json_dump()
            return{"status": "success", "data": response}, 200

    @jwt_required
    def delete(self, id):
        """
         Method deletes a order by id.
        """
        json_data = request.get_json(force=True)
        order = Order.query.filter_by(id=id).first()
        if order is None:
            return {"status": "Failed!!",
                    "data": "Order id does not exist.Please enter a valid order id"}, 404
        else:
            Order.query.filter_by(id=id).delete()
            db.session.commit()
            response = json.loads(json.dumps(json_data))
            return {"status": "deleted!", "data": response}, 200


class OrderList(Resource):
    """
    OrderList resource that has a get and post method.
    """
    @jwt_required
    @require_admin
    def get(self):
        """
        Method to get all orders.
        """
        orders = Order.query.all()
        response = [order.json_dump() for order in orders]
        return {"status": "success", "data": response}, 200

    @jwt_required
    def post(self):
        """
         Method creates an order.
        """
        json_data = request.get_json(force=True)
        if 'user_id' not in json_data or \
                'item_id' not in json_data or 'quantity' not in json_data:
            return {"status": "Failed!",
                    "message": "Please supply user id, item id and quantity"}, 406
        if not num_check(json_data['item_id']) or not num_check(json_data['quantity']):
            return {"status": "Failed!"}
        item_id = json_data['item_id']
        user_id = json_data['user_id']
        quantity = json_data['quantity']
        item = Menu.query.filter_by(id=item_id).first()
        user = User.query.filter_by(id=user_id).first()
        if item_id == '':
            return {"status": "Failed!",
                    "message": "Item can not be empty."}, 406
        elif user_id == '':
            return {"status": "Failed!",
                    "data": "User id can not be empty.Please enter a valid user id"}
        elif quantity == '':
            return {"status": "Failed!",
                    "message": "Quantity can not be empty."}, 406
        if item is None:
            return {"status": "Failed!",
                    "data": "Item id does not exist."}, 404
        if user is None:
            return {"status": "Failed!",
                    "message": "User does not exist."}, 404
        else:
            order = Order(user_id=user_id, item_id=item_id, quantity=quantity)
            order.save()
            response = json.loads(json.dumps(order.json_dump()))
            return {"status": "success", "data": response}, 201
