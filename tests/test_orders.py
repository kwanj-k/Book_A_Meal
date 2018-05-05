from app import create_app
import unittest
import json

config_name = "testing"
app = create_app(config_name)


class TestOrders(unittest.TestCase):
    """
    Orders Test class to test create,get,update and delete endpoints.
    """

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {
            "name": "lunch",
            "item": "chicken",
            "quantity": 1
        }
        self.data1 = {
            "name": "lunch",
            "item": "chicken",
            "quantity": 2
        }

    def test_create_orders(self):
        response = self.app.post('/api/v1/orders',
                                 data=json.dumps(self.data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_orders(self):
        res = self.app.get('/api/v1/orders')
        self.assertEqual(res.status_code, 200)

    def test_Orders_update(self):
        self.app.post('/api/v1/orders',
                      data=json.dumps(self.data),
                      content_type='application/json')
        response = self.app.put('/api/v1/orders/1',
                                data=json.dumps(self.data1),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_Orders_delete(self):
        self.app.post('/api/v1/orders',
                      data=json.dumps(self.data),
                      content_type='application/json')
        response = self.app.put('/api/v1/orders/1',
                                data=json.dumps(self.data1),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
