from app import create_app
import unittest
import json

config_name = "testing"
app = create_app(config_name)

class TestOrders(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {
                        "item":"fried chicken"
        				 }
       
    def test_create_orders(self):
        #Tests create then tests the get method
        response = self.app.post('/api/v1/orders',
                     data = json.dumps(self.data) ,
                      content_type = 'application/json')

        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode())
        self.assertEqual(result["item"], "fried chicken")

    def test_get_orders(self):
        res = self.app.get('/api/v1/orders')
        self.assertEqual(res.status_code, 200)

    def test_Orders_update(self):
        #Tests orders update
        response = self.app.put(
                                '/api/v1/orders/1',
                                data={
                                'item':'chai'}
            )
        self.assertEqual(response.status_code, 201)
        res = self.app.get(
                '/api/v1/orders/1'
            )
        self.assertIn('chai', str(res.data))
        
if __name__ == '__main__':
    unittest.main()
      