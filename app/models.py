class Meal:
    """
    A meal class to define meal.
    It has a json_dump method to format data to json.
    """
    count = 1

    def __init__(self, name):
        self.name = name
        self.id = Meal.count
        Meal.count += 1
    def json_dump(self):
        return dict(
            name=self.name,
            id=self.id)

class Menu(Meal):
    """
    A menu class that inherits from meal and defines menu.
    It has a json_dump method to format data to json.
    """
    count = 1

    def __init__(self, name, item):
        Meal.__init__(self, name)
        self.id = Menu.count
        self.item = item
        Menu.count += 1
    def json_dump(self):
        return dict(
            name=self.name,
            item=self.item,
            id = self.id)

class Order(Menu):
    """
    A menu class that inherits from meal and defines menu.
    It has a json_dump method to format data to json.
    """
    count = 1

    def __init__(self, name, item, quantity=1):
        Menu.__init__(self, name, item)
        self.id = Order.count
        self.quantity = quantity
        self.id = Order.count
        Order.count += 1

    def json_dump(self):
        return dict(
            name=self.name,
            item=self.item,
            quantity=self.quantity,
            id=self.id)


class Db(object):
    """
    A mock-database class to hold meals,menus,orders and accounts.
    It also provides get_user,get_meal_by_id,get_user_info and get_order_by_id methods.
    """
    meals = []
    menus = []
    orders = []
    user_accounts = [

    @classmethod
    def get_user(cls, email, password):
        for user in cls.user_accounts:
            if user.email == email and user.password == password:
                return user

    @classmethod
    def get_meal_by_id(cls,id)
        for meal in cls.meals:
            if meal.id == id:
                return meal

    @classmethod
    def get_order_by_id(cls, id):
        for order in cls.orders:
            if order.id == id:
                return order

    @classmethod
    def get_user_info(cls, username, email):
        for user in cls.user_accounts:
            if user.email == email and user.username == username:
                return us

class Account:
    """
     Account class to define user account.
     Also provides get user_type method 
    """
    count = 1

    def __init__(self, username, email, password, user_type=1):
        self.id = Account.count
        self.username = username
        self.email = email
        self.password = password
        self.user_type = user_type
        Account.count += 1

    def get_user_type(self, num):
        if num == 1:
            return 'customer'
        elif num == 2:
            return 'caterer'

