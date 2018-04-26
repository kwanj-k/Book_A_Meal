from app import app
import unittest
import json

class TestMeal(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {
                        "name":"lunch"
        				 }
       
    def test_create_meals(self):
        #Tests create method then tests get method.
        response = self.app.post('/api/v1/meals',
                     data = json.dumps(self.data) ,
                      content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data)
        self.assertEqual(result["name"], "lunch")
        

    def test_get_meals(self):
        res = self.app.get('/api/v1/meals')
        self.assertEqual(res.status_code, 200)

    def test_meal_update(self):
        #Tests meal update
        response = self.app.put(
                                '/api/v1/meals/1',
                                data={
                                'name':'dinner'}
            )
        self.assertEqual(response.status_code, 201)
        res = self.app.get(
                '/api/v1/meals/1'
            )
        self.assertIn('dinner', str(res.data))

    def test_meal_deletion(self):
        #Tests meal deletion        
        res = self.app.delete('/api/v1/meals/meal2')
        self.assertEqual(res.status_code, 204)
        

if __name__ == '__main__':
    unittest.main()
      