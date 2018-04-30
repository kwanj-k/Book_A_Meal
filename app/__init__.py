from flask import Flask,request,jsonify,make_response
from flask_restful import reqparse, abort, Api, Resource
from config import app_config
from app.resources.meal import MealResource
from app.resources.menu import MenuResource
from app.resources.order import OrderResource
from app.resources.auth import RegisterResource,LoginResource

def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False
    api.add_resource(MealResource, '/api/v1/meals', '/api/v1/meals/<int:id>')
    api.add_resource(MenuResource, '/api/v1/menus', '/api/v1/menus/<int:id>')
    api.add_resource(OrderResource, '/api/v1/orders',
                     '/api/v1/orders/<int:id>')
    api.add_resource(RegisterResource, '/api/v1/auth/register')
    api.add_resource(LoginResource, '/api/v1/auth/login')
    return app
