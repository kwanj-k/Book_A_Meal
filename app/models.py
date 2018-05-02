from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_bcrypt import Bcrypt

class User(db.Model):
    """This class defines the users table """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    orders   = db.relationship('Order', backref='owner')

    def __init__(self, email, password):
        """Initialize the user with an email,orders and a password."""
        self.email = email
        
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
            email=self.email,

        )
class Meal(db.Model):
    """
    Meal model to define the meal. 
    """

    __tablename__ = 'meals'
    id   = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(100), nullable=False)
    menu_items   = db.relationship('Menu', backref=db.backref('meal'))
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
        db.session.add(self)
        db.session.commit()

class Menu(db.Model):
    __tablename__ = 'menus'
    id = db.Column(db.Integer, primary_key=True)
    menu_item = db.Column(db.String(100), nullable=False)
    orders   = db.relationship('Order', backref=db.backref('menu'))
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id',on_delete='CASCADE'))
    date_created = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(),
        nullable=False)


    def json_dump(self):
        return dict(
            meal_id=self.meal_id,
            menu_item=self.item,
            date_created=str(self.date_created))

    def save(self):
        db.session.add(self)
        db.session.commit()

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer,db.ForeignKey('menus.id'))
    quantity = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_created = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(),
        nullable=False)


    def json_dump(self):
        return dict(
            user_id=self.user_id,
            item_id = self.item_id,
            quantity = self.quantity,
            date_created=str(self.date_created))

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    