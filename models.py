
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Meal(db.Model):
    

    __tablename__ = 'meals'

    id              = db.Column(db.Integer, primary_key=True)
    meal_name       = db.Column(db.String(50))
    meal_menu       = db.relationship('Menu',
                                           cascade="all, delete-orphan",
                                           lazy='dynamic')
    date_created    = db.Column(db.DateTime,
                             default=db.func.current_timestamp())
    date_modified   = db.Column(db.DateTime,
                              default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    def __init__(self, name):
        """initialize with name."""
        self.meal_name =meal_name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Meal.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Meal: {}>".format(self.meal_name)

class Menu(db.Model):
    
    __tablename__ = 'menus'

    id              = db.Column(db.Integer, primary_key=True)
    meal_id         = db.Column(db.Integer, db.ForeignKey('meals.id'))
    menu_name       = db.Column(db.String(50))
    menu_price      = db.Column(db.Float())
    date_created    = db.Column(db.DateTime,
                             default=db.func.current_timestamp())
    date_modified   = db.Column(db.DateTime,
                              default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())





    
