""" App module to bring together the whole app."""

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta

from config import app_config
from app.resources.meal import MealResource, MealListResource
from app.resources.menu import MenuResource, MenuListResource
from app.resources.order import OrderResource, OrderListResource
from app.resources.auth import RegisterResource, LoginResource

jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.url_map.strict_slashes = False
    app.config['JWT_SECRET_KEY'] = 'super-secret-key-that'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=72)
    jwt.init_app(app)
    from app.models import db
    db.init_app(app)

    api.add_resource(MealListResource, '/api/v2/meals')
    api.add_resource(MealResource, '/api/v2/meals/<int:id>')
    api.add_resource(MenuListResource, '/api/v2/menus')
    api.add_resource(MenuResource, '/api/v2/menus/<int:id>')
    api.add_resource(OrderListResource, '/api/v2/orders')
    api.add_resource(OrderResource, '/api/v2/orders/<int:id>')
    api.add_resource(RegisterResource, '/api/v2/auth/register')
    api.add_resource(LoginResource, '/api/v2/auth/login')

    return app
