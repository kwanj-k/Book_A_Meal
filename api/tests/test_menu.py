from app import app
import unittest
import json




class TestMenu(unittest.TestCase):

    def setUp(self):
        app.testing = True

        self.app = app.test_client()

        self.data = {
                        "id":1,
                        "name":"fried chicken"
        				 }
       

    def test_get_and_create_menus(self):
        #Tests create then continues to test get

        response = self.app.post('/api/v1/menu',
                     data = json.dumps(self.data) ,
                      content_type = 'application/json')

        

        self.assertEqual(response.status_code, 201)

        result = json.loads(response.data)


        self.assertEqual(result["message"], "fried chicken")

        res = self.app.get('/api/v1/menus')

        self.assertEqual(res.status_code, 200)

       


if __name__ == '__main__':
    unittest.main()
      