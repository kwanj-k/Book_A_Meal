from app import app
import unittest
import json

class TestOrders(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {
                        "id":1,
                        "owner":"kelvin",
                        "item":"fried chicken"
        				 }
       
    def test_get_and_create_orders(self):
        #Tests create then tests the get method
        response = self.app.post('/api/v1/orders',
                     data = json.dumps(self.data) ,
                      content_type = 'application/json')

        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data)
        self.assertEqual(result["message"], "fried chicken")

    def test_get_orders(self):
        res = self.app.get('/api/v1/orders')
        self.assertEqual(res.status_code, 200)

    def test_Orders_update(self):
        #Tests orders update
        response = self.app.post('/api/v1/orders',
                     data = { "owner":"kelvin",
                                "item":"ham"},
                      content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.put(
                                '/api/v1/orders/1',
                                data = { "owner":"kelvin",
                                "item":"badgia"},
            )
        self.assertEqual(rv.status_code, 200)
        res = self._and_createapp.get(
                '/api/v1/oreders/1'
            )
        self.assertIn('badgia', str(res.data))

if __name__ == '__main__':
    unittest.main()
      