from flask import json, request
from flask_restful import Resource,reqparse
from app.models import db, Menu,Meal
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from .validators import require_admin
class MenuResource(Resource):
    """
    Menu Resource with GET, POST, PUT and DELETE methods
    """

    @jwt_required
    def get(self, id):
        """
        Method gets a menu by id.
        """
        menu = Menu.query.filter_by(id=id).first()
        if menu is None:
            return {"status":"Failed!!",
            "data":"Menu id does not exist.Please enter a valid menu id"}
        response = menu.json_dump()
        return response
    @jwt_required
    @require_admin
    def put(self, id):
        """
        Method updates menu.
        """
        json_data = request.get_json(force=True)
        menu = Menu.query.filter_by(id=id).first()
        if 'meal_id' not in json_data or 'menu_item' not in json_data:
            return {"status":"Failed!","data":"Please provide a meal_id and menu_item to update."}
        if  menu is None:
            return {"status":"Failed!!",
            "data":"Menu id does not exist.Please enter a valid meal id"}
        meal= Meal.query.filter_by(id=json_data['meal_id']).first()
        if  meal is None:
            return {"status":"Failed!!",
            "data":"Meal id does not exist.Please enter a valid meal id"}
        if json_data['menu_item']== '':
            return {"status":"Failed!!",
            "data":"Menu item can not be empty.Please enter a valid menu item"}
        else:
            if json_data['meal_id']:
                menu.meal_id = json_data['meal_id']
            if json_data['menu_item']:
                menu.menu_item = json_data['menu_item']
            db.session.commit()
            response = menu.json_dump()
            return{"status": "success", "data": response}, 200

    @jwt_required
    @require_admin
    def delete(self, id):
        """
         Method deletes a menu by id.
        """
        json_data = request.get_json(force=True)
        menu= Menu.query.filter_by(id=id).first()
        if  menu is None:
            return {"status":"Failed!!",
            "data":"Menu id does not exist.Please enter a valid meal id"}
        else:
            Menu.query.filter_by(id=id).delete()
            db.session.commit()
            response = json.loads(json.dumps(json_data))
            return {"status": "deleted!", "data": response}, 200


class MenuListResource(Resource):
    """
    MenuList resource that has a get and post method.
    """
    @jwt_required
    def get(self):
        """
        Method to get all menus.
        """
        menus = Menu.query.all()
        response = [menu.json_dump() for menu in menus]
        return {"status": "success", "data": response}, 200
    @jwt_required
    @require_admin
    def post(self):
        """
         Method creates a menu.
        """
        json_data = request.get_json(force=True)
        
        if 'meal_id'not in json_data or 'menu_item' not in json_data:
            return {"status":"Failed!",
                    "data":"Please a valid provide a meal_id and menu_item to create menu."}
        menu_item = json_data['menu_item']
        meal_id   = json_data['meal_id']
        meal= Meal.query.filter_by(id=meal_id).first()
        if menu_item == '':
            return {"status":"Failed",
            "data":"Menu item can not be empty.Please enter a valid menu item"}
        elif meal_id == '' :
            return {"status":"Failed",
            "data":"Meal id can not be empty.Please enter a valid meal id"}
        if  meal is None:
            return {"status":"Failed!!","data":"Please enter a valid meal id"}
        menu = Menu(meal_id=meal_id,menu_item=menu_item)
        menu.save()
        response = json.loads(json.dumps(menu.json_dump()))
        return {"status": "success", "data": response}, 201
