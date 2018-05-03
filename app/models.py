from flask_sqlalchemy import SQLAlchemy
import jwt
from datetime import datetime, timedelta
db = SQLAlchemy()

from flask_bcrypt import Bcrypt

class User(db.Model):
    """This class defines the users table """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False, unique=True)
    user_email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    admin   = db.Column(db.Boolean)
    orders   = db.relationship('Order', backref='owner')
    meals   = db.relationship('Meal', backref='owner')

    def __init__(self, user_email,user_name , password):
        """Initialize the user with an email,orders and a password."""
        self.user_email = user_email
        self.user_name = user_name
    
        self.password = Bcrypt().generate_password_hash(password).decode()

    def password_is_valid(self, password):
        """
        Checks the password against it's hash to validates the user's password
        """
        return Bcrypt().check_password_hash(self.password, password)

    

    def save(self):
        """Save a user to the database.
        This includes creating a new user and editing one.
        """
        db.session.add(self)
        db.session.commit()

    def json_dump(self):
        return dict(
            id = self.id,
            user_email=self.user_email,
            user_name=self.user_name,
            orders = self.orders,
            meals= self.meals
        )
class Meal(db.Model):
    """
    Meal model to define the meal. 
    """

    __tablename__ = 'meals'
    id   = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(100), nullable=False)
    menu_items   = db.relationship('Menu', passive_deletes=True, backref=db.backref('meal'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'))
    date_created = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(),
        nullable=False)

    def __init__(self, meal_name):
        """ Initialize with name of meal """
        self.meal_name = meal_name
    
    def json_dump(self):
        """ Method to return a meal as a dict."""
        return dict(
            id= self.id,
            meal_name=self.meal_name,
            menu_items=[menu.json_dump() for menu in self.menu_items],
            date_created=str(self.date_created)
        )

    def save(self):
        """ Save the meal to database"""
        db.session.add(self)
        db.session.commit()

class Menu(db.Model):
    """
    Menu model to define the menu. 
    """
    __tablename__ = 'menus'
    id = db.Column(db.Integer, primary_key=True)
    menu_item = db.Column(db.String(100), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id',ondelete='CASCADE'))
    date_created = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(),
        nullable=False)


    def json_dump(self):
        """ Method to return a meal as a dict."""
        return dict(
            id = self.id,
            meal_id=self.meal_id,
            menu_item=self.menu_item,
            date_created=str(self.date_created))

    def save(self):
        db.session.add(self)
        db.session.commit()

class Order(db.Model):
    """
    Order model to define the orders. 
    """
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer,db.ForeignKey('menus.id'))
    quantity = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'))
    date_created = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(),
        nullable=False)


    def json_dump(self):
        """ Method to return an order as a dict."""
        return dict(
            user_id=self.user_id,
            item_id = self.item_id,
            quantity = self.quantity,
            date_created=str(self.date_created))

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    