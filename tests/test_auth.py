""" Authenitication test cases"""

import unittest
import json
from app import create_app
from app.models import db
class TestAuthenitication(unittest.TestCase):
    """
    Authenitication class to test the login and registration endpoints.
    """

    def setUp(self):
        """ Set up test Variables"""
        self.app = create_app(config_name="testing")
        # initialize the test client
        self.client = self.app.test_client
        self.data = {
            "username":"zeus",
        	"email":"email@gmail.com",
        	"password":"kwanjkay",
            "is_admin":"true"
            }
        with self.app.app_context():
            """ create all tables """
            db.session.close()
            db.drop_all()
            db.create_all()

    def test_registration(self):
        """ Verify user registration works correctly """
        res = self.client().post("api/v2/auth/register", data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(res.status_code,201 )

    def test_already_registered_user(self):
        """Verify that a user cannot be registered twice."""
        res = self.client().post('/api/v2/auth/register', data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)
        second_res = self.client().post('/api/v2/auth/register', data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(second_res.status_code, 202)
       
    def test_login(self):
        """ Verify a registered user can login"""
        res = self.client().post('/api/v2/auth/register', data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(res.status_code,201)
        login_response = self.client().post('/api/v2/auth/login',data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(login_response.status_code, 200)

    def test_non_registered_user_login(self):
        """Test non registered users cannot login."""
        not_a_user = {
            'email': 'cuhicuhi@example.com',
            'password': 'yesnoyesno'
        }
        res = self.client().post('/api/v2/auth/login',data=json.dumps(not_a_user),
                            content_type='application/json')
        self.assertEqual(res.status_code, 401)             
