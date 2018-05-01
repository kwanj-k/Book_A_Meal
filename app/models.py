class Meal:
    """
    A Meal class to mode the meal entity and provides a json_dump method.
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
    A Menu class to model the menu entity and provides a json_dump method.
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
            id=self.id)


class Order(Menu):
    """
    A Order class to model the order entity and provides a json_dump method.
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
    A mock-db class to simulate a a database.
    """
    meals = []
    menus = []
    orders = []
    user_accounts = []

    @classmethod
    def get_user(cls, email, password):
        for user in cls.user_accounts:
            if user.email == email and user.password == password:
                return user

    @classmethod
    def get_meal_by_id(cls, id):
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
                return user


class Account:
    """
    An Acouunt class to model the user entity and provides get_user_type method.
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
