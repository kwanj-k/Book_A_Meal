from app import create_app
import unittest
import json

config_name = "testing"
app = create_app(config_name)

class TestMeal(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {
                        "name":"lunch"
        				 }
        self.data1 = {
                        "name":"lunchhh"
        				 }
       
    def test_create_meals(self):
        #Tests create method then tests get method.
        response = self.app.post('/api/v1/meals',
                     data = json.dumps(self.data) ,
                      content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        
    def test_get_meals(self):
        res = self.app.get('/api/v1/meals')
        self.assertEqual(res.status_code, 200)

    def test_meal_update(self):
        #Tests meal update
        response = self.app.post('/api/v1/meals',
                     data = json.dumps(self.data) ,
                      content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        res = self.app.put(
                                '/api/v1/meals/1',
                                data=json.dumps(self.data1) ,
                                content_type= 'application/json')
        self.assertEqual(res.status_code, 200)
    def test_meal_delete(self):
        self.app.post('/api/v1/meals',
                     data = json.dumps(self.data) ,
                      content_type = 'application/json')
        res = self.app.put('/api/v1/meals/1',
                            data=json.dumps(self.data1) ,
                            content_type= 'application/json')
        self.assertEqual(res.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()