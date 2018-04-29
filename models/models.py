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
    meals            = []
    menus            = []
    orders           = []
    user_accounts    = []
    caterer_accounts = []

    @classmethod
    def get_user(cls, email, password):
        for user in cls.user_accounts or cls.caterer_accounts:
            if user.email == email and user.password == password:
                return user

    
class Account:
    count = 1
    def __init__(self,username,email,password,user_type=1):
        self.id        = Account.count
        self.username  = username
        self.email     = email
        self.password  = password
        self.user_type = user_type
        Account.count += 1

    def get_user_type(self,num):
        if num == 1:
            return 'customer'
        elif num == 2:
            return 'caterer'



    