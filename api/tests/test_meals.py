from app import app
import unittest
import json




class TestMeal(unittest.TestCase):

    def setUp(self):
        app.testing = True

        self.app = app.test_client()

        self.data = {
                        "id":1,
                        "meal_name":"lunch"
        				 }
       

    def test_get_and_create_meals(self):
        #Tests create method then tests get method.
        response = self.app.post('/api/v1/meals',
                     data = json.dumps(self.data) ,
                      content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data)
        self.assertEqual(result["message"], "lunch")
        res = self.app.get('/api/v1/meals')
        self.assertEqual(res.status_code, 200)




    def test_meal_update(self):
        #Tests meal update

        response = self.app.post('/api/v1/meals',
                     data = {'meal_name':'supper'} ,
                      content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.put(
                                '/api/v1/meals/1',
                                data={'meal_name':'dinner'}
            )
        self.assertEqual(rv.status_code, 200)

        res = self.app.get(
                '/api/v1/meals/1'
            )
        self.assertIn('dinner', str(res.data))


    def test_meal_deletion(self):
        #Tests meal deletion
        
        response = self.app.post(
            '/meals',
            data={'meal_name': 'BreakFast'})

        self.assertEqual(response.status_code, 201)

        res = self.app.delete('/meals/1')

        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.app.get('/meals/1')

        self.assertEqual(result.status_code, 404)

       


if __name__ == '__main__':
    unittest.main()
      