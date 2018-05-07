""" Testcases for menus endpoints"""
import unittest
import json

from app import create_app
from app.models import db
config_name = "testing"
app = create_app(config_name)


class TestMenu(unittest.TestCase):
    """
    Menu Test class to test create,get,update and delete endpoints.
    """

    def setUp(self):
        """ Set up test Variables"""
        self.app = create_app(config_name="testing")
        # initialize the test client
        self.client = self.app.test_client
        self.userdata = {
            "username": "zeus",
            "email": "email@gmail.com",
            "password": "kwanjkay",
            "is_admin": "true"}
        self.meal = {"meal_name": "Brunch"}
        self.data = {"meal_id": 1, "meal_item": "pancake"}
        self.data1 = {"meal_id": 1, "meal_item": "pancake22"}

        with self.app.app_context():
            """ create all tables """
            db.session.close()
            db.drop_all()
            db.create_all()
        self.client().post("api/v2/auth/register", data=json.dumps(self.userdata),
                           content_type='application/json')
        login = self.client().post('/api/v2/auth/login', data=json.dumps(self.userdata),
                                   content_type='application/json')
        self.token = json.loads(login.data.decode()).get('token')
        self.client().post('/api/v2/meals',
                           data=json.dumps(self.meal),
                           content_type="application/json",
                           headers=dict(Authorization="Bearer " + self.token))

    def test_get_menus(self):
        """Test get all meal items endpoints"""
        res = self.client().get('/api/v2/menus',
                                headers=dict(Authorization="Bearer " + self.token))
        self.assertEqual(res.status_code, 200)

    def test_create_menus(self):
        """Test create meal items endpoint"""
        res = self.client().post('/api/v2/menus',
                                 data=json.dumps(self.data),
                                 content_type="application/json",
                                 headers=dict(Authorization="Bearer " + self.token))
        self.assertEqual(res.status_code, 201)

    def test_get_menu_by_id(self):
        """ Test get meal item by id"""
        self.client().post("/api/v2/menus",
                           data=json.dumps(self.data),
                           content_type="application/json",
                           headers=dict(Authorization="Bearer " + self.token))
        res2 = self.client().get('/api/v2/menus/1',
                                 content_type="application/json",
                                 headers=dict(Authorization="Bearer " + self.token))
        self.assertEqual(res2.status_code, 200)

    def test_menu_update(self):
        """ Test meal item update"""
        self.client().post('/api/v2/menus',
                           data=json.dumps(self.data),
                           content_type="application/json",
                           headers=dict(Authorization="Bearer " + self.token))
        res = self.client().put('/api/v2/menus/1',
                                data=json.dumps(self.data1),
                                content_type="application/json",
                                headers=dict(Authorization="Bearer " + self.token))
        self.assertEqual(res.status_code, 200)

    def test_menu_delete(self):
        """Test meal item deletion"""
        self.client().post('/api/v2/menus',
                           data=json.dumps(self.data),
                           content_type="application/json",
                           headers=dict(Authorization="Bearer " + self.token))
        res = self.client().delete('/api/v2/menus/1',
                                   data=json.dumps(self.data),
                                   content_type="application/json",
                                   headers=dict(Authorization="Bearer " + self.token))
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
