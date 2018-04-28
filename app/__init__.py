from flask import Flask,request,jsonify,make_response
from flask_restful import reqparse, abort, Api, Resource
from instance.config import app_config
from resources.meal import MealResource
from resources.menu import MenuResource
from resources.order import OrderResource

def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')


    api.add_resource(MealResource, '/api/v1/meals', '/api/v1/meals/<int:id>')
    api.add_resource(MenuResource, '/api/v1/menus', '/api/v1/menus/<int:id>' )
    api.add_resource(OrderResource, '/api/v1/orders', '/api/v1/orders/<int:id>' )
    return app