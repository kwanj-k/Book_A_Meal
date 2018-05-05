'''Validators for user inputs'''
import re
from app.models import User
from functools import wraps
from flask_jwt_extended import (
    get_jwt_identity
)

def space_stripper(data):
    striped = "".join(data.split())
    return striped

def bool_transform(data):
    strng = "".join(data.split())
    if strng == "true":
        return True
    if strng == "false":
        return False
    else:
        return {"data":"Please enter true or false in the admin field"}  

def num_check(data):
    num = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
    if re.match(num,data):
        return True  
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

def user_name_validator(data):
    '''validates user provided username'''
    username = "".join(data.split())
    striped = re.sub(r'[\s]+','',username)
    if re.match("^[a-zA-Z0-9_]*$", username) and striped != '':
        return True

def name_validator(name):
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

