from app import app
import unittest
import json

class TestMenu(unittest.TestCase):

    def setUp(self):
        app.testing = True

        self.app = app.test_client()

        self.data = {
                        "name":"fried chicken"
        				 }
       
    def test_create_menu(self):
        #Tests create then continues to test get
        response = self.app.post('/api/v1/menus',
                     data = json.dumps(self.data) ,
                      content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
       

    def test_get_menu(self):
        res = self.app.get('/api/v1/menus')
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()
      