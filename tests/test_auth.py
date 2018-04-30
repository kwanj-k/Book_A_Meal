from app import create_app
import unittest
import json

config_name = "testing"
app = create_app(config_name)

class TestAuthenitication(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {"username":"zeus",
        				 "email":"email@gmail.com",
        				 "password":"4084",
                         "user_type":1
                  
                         }
        self.data1 = {
        				 "email":"email@gmail.com",
        				 "password":"4084",
                         }

    def test_register(self):
        response = self.app.post("/api/v1/auth/register", 
                    data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(response.status_code, 201)
       
    def test_login(self):
        self.app.post("/api/v1/auth/register", 
                    data=json.dumps(self.data),
                            content_type='application/json')
        res    = self.app.post("/api/v1/auth/login", 
                    data=json.dumps(self.data1),
                             content_type='application/json')
        self.assertEqual(res.status_code, 200)