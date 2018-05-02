'''Validators for user inputs'''
import re

def email_validator(email):
    '''validates user provided email'''
    if re.match(
            "^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$",
            email):
        return True
def password_validator(password):
    '''validates user provided password length'''
    if len(password) > 6:
        return True
def user_name_validator(user_name):
    '''validates user provided username'''
    if re.match("^[a-zA-Z0-9_]*$", user_name):
        return True
def mealname_and__menuitem_validator(name):
    '''Validates names provided for meals and menus'''
    if re.match("^[a-zA-Z0-9_\s]*$", name):
        return True