""" Menu resource to create all endpoints related to meal items."""

from flask import json, request
from flask_restful import Resource
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity)

from app.models import db, Menu, Meal, User
from .validators import require_admin, space_stripper, name_validator, num_check


class Menus(Resource):
    """
    Menu Resource with GET, POST, PUT and DELETE methods
    """

    @jwt_required
    def get(self, id):
        """
        Method gets a menu by id.
        """
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        menu = Menu.query.filter_by(id=id).first()
        if menu is None:
            return {"status": "Failed!!", "message": "Meal item does not exist."}, 404
        if menu.user_id == current_user.id:
            response = menu.json_dump()
            return response
        return {"status": "Failed!", "message": "Meal does not exist."}, 404

    @jwt_required
    @require_admin
    def put(self, id):
        """
        Method updates menu.
        """
        json_data = request.get_json(force=True)
        menu = Menu.query.filter_by(id=id).first()
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        meal = Meal.query.filter_by(id=json_data['meal_id']).first()
        if 'meal_id' not in json_data or 'meal_item' not in json_data:
            return {"status": "Failed!", "message": "Please provide a meal_id and meal_item to update."}, 406
        if menu is None:
            return {"status": "Failed!",
                    "message": "Meal item does not exist."}, 404
        if meal is None:
            return {"status": "Failed!",
                    "message": "Meal does not exist."}, 404
        if not num_check(json_data['meal_id']):
            return {"status": "Failed!",
                    "message": "Meal id must be an integer"}, 406
        if json_data['meal_item'] == '' or json_data['meal_id'] == '':
            return {"status": "Failed!",
                    "message": "Meal item or id can not be empty."}, 406
        if meal.user_id == current_user.id:
            if menu.user_id == current_user.id:
                menu.meal_id = json_data['meal_id']
                menu.meal_item = space_stripper(json_data['meal_item'])
                db.session.commit()
                response = menu.json_dump()
                return{"status": "success", "data": response}, 200
            return {"message": "Item does not exist!"}, 404
        return {"message": "Meal does not exist!"}, 404

    @jwt_required
    @require_admin
    def delete(self, id):
        """
         Method deletes a menu by id.
        """
        json_data = request.get_json(force=True)
        menu = Menu.query.filter_by(id=id).first()
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        if menu is None:
            return {"status": "Failed!!",
                    "message": "Meal item does not exist."}, 404
        if menu.user_id == current_user.id:
            Menu.query.filter_by(id=id).delete()
            db.session.commit()
            response = json.loads(json.dumps(json_data))
            return {"status": "deleted!", "data": response}, 200
        return {"message": "Meal does not exist."}, 404


class MenuList(Resource):
    """
    MenuList resource that has a get and post method.
    """
    @jwt_required
    def get(self):
        """
        Method to get all menus.
        """
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        menus = Menu.query.filter_by(user_id=current_user.id)
        if menus is None:
            return{"message": "You do not have menus at the moment."}, 404
        response = [menu.json_dump() for menu in menus]
        return {"status": "success", "data": response}, 200

    @jwt_required
    @require_admin
    def post(self):
        """
         Method creates a menu.
        """
        json_data = request.get_json(force=True)

        if 'meal_id'not in json_data or 'meal_item' not in json_data:
            return {"status": "Failed!",
                    "message": "Please a valid provide a meal_id and meal_item to create menu."}, 406
        if not num_check(json_data['meal_id']):
            return {"status": "Failed!", "message": "Meal id must be an integer"}, 406
        meal_item = json_data['meal_item']
        meal_id = json_data['meal_id']
        meal = Meal.query.filter_by(id=meal_id).first()
        if space_stripper(meal_item) == '':
            return {"status": "Failed!",
                    "message": "Menu item can neither be empty nor contain special characters."}, 406
        if meal_id == '':
            return {"status": "Failed!",
                    "message": "Meal id can not be empty."}, 406
        if meal is None:
            return {"status": "Failed!", "message": "Meal id does not exist."}, 404
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        user_id = current_user.id
        if meal.user_id == current_user.id:
            menu = Menu(meal_id=meal_id, meal_item=meal_item, user_id=user_id)
            menu.save()
            response = json.loads(json.dumps(menu.json_dump()))
            return {"status": "success", "data": response}, 201
        return {"message": "Meal does not exist"}, 404
