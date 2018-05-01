from app import create_app
import unittest
import json

config_name = "testing"
app = create_app(config_name)

class TestAuthenitication(unittest.TestCase):
    """
    Authenitication class to test the login and registration endpoints.
    """

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {"username":"zeus",
        				 "email":"email@gmail.com",
        				 "password":"4084",
                         "user_type":1
                  
                         }
        self.data2 = {"username":"kwanj",
        				 "email":"kwanj@gmail.com",
        				 "password":"4084",
                         "user_type":2
                  
                         }
        self.data3 = {"username":"kelvin",
        				 "email":"kelvin@gmail.com",
        				 "password":"4084",
                         "user_type":1
                  
                         }
        self.data1 = {
        				 "email":"email@gmail.com",
        				 "password":"4084",
                         }

    def test_register(self):
        res = self.app.post("/api/v1/auth/register", 
                    data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(res.status_code,201 )
       
    def test_login(self):
        user = {"username":"catsand rain",
        				 "email":"fu@gmail.com",
        				 "password":"4084",
                         "user_type":1
                  
                         }
        self.app.post("/api/v1/auth/login", 
                    data=json.dumps(user),
                            content_type='application/json')
        res    = self.app.post("/api/v1/auth/login", 
                    data=json.dumps(user),
                             content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_double_registration(self):
        res = self.app.post("/api/v1/auth/register", 
                    data=json.dumps(self.data2),
                            content_type='application/json')
        self.assertEqual(res.status_code,201 )
        res = self.app.post("/api/v1/auth/register", 
                    data=json.dumps(self.data2),
                            content_type='application/json')
        self.assertEqual(res.status_code,409 )                  