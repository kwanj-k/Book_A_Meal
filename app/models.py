from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_bcrypt import Bcrypt

class User(db.Model):
    """This class defines the users table """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    def __init__(self, email,orders, password):
        """Initialize the user with an email,orders and a password."""
        self.email = email
        self.orders= orders
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
            email=self.email
        )
class Meal(db.Model):

    __tablename__ = 'meals'
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    date_created = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(),
        nullable=False)

    def __init__(self, name,menus):
        """ Initialize with name of meal """
        self.name = name

    def json_dump(self):
        return dict(
            name=self.name,
            date_created=str(self.date_created)
        )

    def save(self):
        db.session.add(self)
        db.session.commit()

class Menu(db.Model):
    __tablename__ = 'menus'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    date_created = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(),
        nullable=False)
    # meal_id = db.Column(db.Integer, db.ForeignKey(
    #     'meals.id', ondelete='CASCADE'), nullable=False)
    # meal = db.relationship('Meal', backref=db.backref('menus',
    #                                                   lazy='dynamic'))

    def __init__(self, item,meal_id):
        self.item = item
        self.meal_id = meal_id

    def json_dump(self):
        return dict(
            item=self.item,
            date_created=str(self.date_created))

    def save(self):
        db.session.add(self)
        db.session.commit()

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, default=1)
    date_created = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(),
        nullable=False)

    def __init__(self,quantity):
        self.quantity = quantity

    def json_dump(self):
        return dict(
            quantity = self.quantity,
            date_created=str(self.date_created))

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    