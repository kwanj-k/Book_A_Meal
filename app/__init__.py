""" App module to bring together the whole app."""

from flask import Flask,send_from_directory
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta

from config import app_config
from app.views.meal import Meals, MealList
from app.views.menu import Menus, MenuList
from app.views.order import Orders, OrderList
from app.views.auth import Register, Login

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

    @app.route('/')
    def api_docs():
        """ Route to the api docs"""
        return send_from_directory('../api-docs', 'index.html')

    api.add_resource(MealList, '/api/v2/meals')
    api.add_resource(Meals, '/api/v2/meals/<int:id>')
    api.add_resource(MenuList, '/api/v2/menus')
    api.add_resource(Menus, '/api/v2/menus/<int:id>')
    api.add_resource(OrderList, '/api/v2/orders')
    api.add_resource(Orders, '/api/v2/orders/<int:id>')
    api.add_resource(Register, '/api/v2/auth/register')
    api.add_resource(Login, '/api/v2/auth/login')

    return app
