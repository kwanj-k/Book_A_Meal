from flask import Flask,request,jsonify,make_response
from flask_restful import reqparse, abort, Api, Resource
from instance.config import app_config
from resources.meal import MealResource
from resources.menu import Menu,MenuList
from resources.order import Order,OrderList

def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')


    api.add_resource(MealResource, '/api/v1/meals', '/api/v1/meals/<int:id>')

    api.add_resource(MenuList, '/api/v1/menus')
    api.add_resource(Menu, '/api/v1/menus/<menu_id>')

    api.add_resource(OrderList, '/api/v1/orders')
    api.add_resource(Order, '/api/v1/orders/<order_id>')

    return app