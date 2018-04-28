class Meal:
    count = 1
    def __init__(self, name):
        self.name   = name
        self.id     = Meal.count
        Meal.count += 1
    def json_dump(self):
        return dict(
            name=self.name,
            id=self.id)

class Menu:
    count = 1
    def __init__(self,meal, item):
        self.id     = Menu.count
        self.meal   = Meal(self.id)
        self.item   = item
        Menu.count += 1
    def json_dump(self):
        return dict(
            meal=self.meal.json_dump(),
            item=self.item,
            id=self.id)

class Order:
    count = 1
    def __init__(self,item, quantity=1):
        self.id         = Order.count
        self.item       = item
        self.quantity   = quantity
        Order.count += 1
    def json_dump(self):
        return dict(
            menu=self.item,
            quantity=self.quantity,
            id=self.id)


class Db(object):
    meals  = []
    menus  = []
    orders = []

    



# class Accounts(object):
#     def __init__(self):

#         self.list_of_accounts = [{'username':'admin',
#                                   'email':'admin@user.com',
#                                   'password':'4084'},

#                                   {'username':'user',
#                                   'email':'user@user.com',
#                                   'password':'4084'},
                                  
#                                   ]


#     def login(self, email, passwordd):
#         """Method for  Handling Login Requests"""
#         for account in self.list_of_accounts:
#             if email == account['email']:
#                 if password == account['password']:
#                     return "Success!"
#                 else:
#                     return "Invalid email, password combination"
#         return "Account not registered, sign up"

#     def registration(self, username, email, password):
#         """Method for creating new accounts."""
#         dict_for_each_account = {}

#         for account in self.list_of_accounts:
#             if email == account['email']:
#                 return "Your Account Already Active. Proceed to login"
#             else:
#               dict_for_each_account['username'] = username
#               dict_for_each_account['email'] = email
#               dict_for_each_account['password'] = password
#               self.list_of_accounts.append(dict_for_each_account)
            
#         return "Your account is now registered please proceed to login"   
            