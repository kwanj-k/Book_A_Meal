'''Validators for user inputs'''
import re
from app.models import User
from functools import wraps
from flask_jwt_extended import (
    get_jwt_identity
)

def space_stripper(data):
    striped = re.sub(r'[\s]+','',data)
    return striped
def email_validator(email):
    '''validates user provided email'''
    if re.match(
            "^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$",
            email):
        return True

def password_validator(password):
    '''validates user provided password length'''
    striped = re.sub(r'[\s]+','',password)
    if len(password) > 6 and striped != '':
        return True

def user_name_validator(username):
    '''validates user provided username'''
    if re.match("^[a-zA-Z0-9_]*$", username):
        return True

def mealname_and__menuitem_validator(name):
    '''Validates names provided for meals and menus'''
    if re.match("^[a-zA-Z0-9_\s]*$", name):
        return True

def boolean_validator(bool):
    if bool == True or bool == False:
        return True

def require_admin(f):
    @wraps(f)
    def decorator(*args,**kwargs):
        current_user =User.query.filter_by(email=get_jwt_identity()).first()
        print(current_user)
        if not current_user.is_admin:
            return {"status":"Failed!","data":"Only administrators can access these resource."}
        return f(*args, **kwargs)
    return decorator  

