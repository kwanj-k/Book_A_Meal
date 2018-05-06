""" Testcases for the orders endpoints"""
import unittest
import json

from app import create_app
from app.models import db
config_name = "testing"
app = create_app(config_name)


class TestOrder(unittest.TestCase):
    """
    order Test class to test create,get,update and delete endpoints.
    """

    def setUp(self):
        """ Set up test Variables"""
        self.app = create_app(config_name="testing")
        # initialize the test client
        self.client = self.app.test_client
        self.userdata = {
            "username": "zeus",
            "email": "email@gmail.com",
            "password": "kwanjkay",
            "is_admin": "true"}
        self.meal = {"meal_name": "Brunch"}
        self.menu = {"meal_id": 1, "meal_item": "pancake"}
        self.data = {"item_id": 1, "quantity": 4}
        self.data1 = {"item_id": 1, "quantity": 35}

        with self.app.app_context():
            """ create all tables """
            db.session.close()
            db.drop_all()
            db.create_all()
        self.client().post("api/v2/auth/register", data=json.dumps(self.userdata),
                           content_type='application/json')
        login = self.client().post('/api/v2/auth/login', data=json.dumps(self.userdata),
                                   content_type='application/json')
        self.token = json.loads(login.data.decode()).get('token')
        self.client().post('/api/v2/meals',
                           data=json.dumps(self.meal),
                           content_type="application/json",
                           headers=dict(Authorization="Bearer " + self.token))
        self.client().post('/api/v2/menus',
                           data=json.dumps(self.menu),
                           content_type="application/json",
                           headers=dict(Authorization="Bearer " + self.token))

    def test_get_orders(self):
        """Test get all orders enpoint"""
        res = self.client().get('/api/v2/orders',
                                headers=dict(Authorization="Bearer " + self.token))
        self.assertEqual(res.status_code, 200)

    def test_create_orders(self):
        """ Test create orders endpoint"""
        res = self.client().post('/api/v2/orders',
                                 data=json.dumps(self.data),
                                 content_type="application/json",
                                 headers=dict(Authorization="Bearer " + self.token))
        self.assertEqual(res.status_code, 201)

    def test_get_order_by_id(self):
        """Test get order by id """
        self.client().post("/api/v2/orders",
                           data=json.dumps(self.data),
                           content_type="application/json",
                           headers=dict(Authorization="Bearer " + self.token))
        res2 = self.client().get('/api/v2/orders/1',
                                 content_type="application/json",
                                 headers=dict(Authorization="Bearer " + self.token))
        self.assertEqual(res2.status_code, 200)

    def test_order_update(self):
        """Test order update endpoint"""
        self.client().post('/api/v2/orders',
                           data=json.dumps(self.data),
                           content_type="application/json",
                           headers=dict(Authorization="Bearer " + self.token))
        res = self.client().put('/api/v2/orders/1',
                                data=json.dumps(self.data1),
                                content_type="application/json",
                                headers=dict(Authorization="Bearer " + self.token))
        self.assertEqual(res.status_code, 200)

    def test_order_delete(self):
        """Test order delete endpoint"""
        self.client().post('/api/v2/orders',
                           data=json.dumps(self.data),
                           content_type="application/json",
                           headers=dict(Authorization="Bearer " + self.token))
        res = self.client().delete('/api/v2/orders/1',
                                   data=json.dumps(self.data),
                                   content_type="application/json",
                                   headers=dict(Authorization="Bearer " + self.token))
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
