from app import create_app
import unittest
import json
from app.models import db

config_name = "testing"


class TestAuthenitication(unittest.TestCase):
    """
    Authenitication class to test the login and registration endpoints.
    """

    def setUp(self):
        """ Set up test Variables"""
        self.app = create_app(config_name="testing")
        # initialize the test client
        self.client = self.app.test_client
        app.testing = True
        self.data = {
            "user_name": "theesus",
            "user_email": "email@gmail.com",
            "password": "theesus",
        }
        with self.app.app_context():
            """ create all tables """
            db.session.close()
            db.drop_all()
            db.create_all()

    def test_register(self):
        res = self.app.post("/api/v1/auth/register",
                            data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_login(self):
        user = {"username": "catsand rain",
                "email": "fu@gmail.com",
                "password": "4084",
                "user_type": 1

                }
        self.app.post("/api/v1/auth/login",
                      data=json.dumps(user),
                      content_type='application/json')
        res = self.app.post("/api/v1/auth/login",
                            data=json.dumps(user),
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_double_registration(self):
        res = self.app.post("/api/v1/auth/register",
                            data=json.dumps(self.data2),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res = self.app.post("/api/v1/auth/register",
                            data=json.dumps(self.data2),
                            content_type='application/json')
        self.assertEqual(res.status_code, 409)
