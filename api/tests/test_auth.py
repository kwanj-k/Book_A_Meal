from app import app
import unittest
import json




class TestAuthenitication(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {"username":"zeus",
        				 "email":"email@gmail.com",
        				 "password":"4084"}
       

    def test_signup_and_login(self):
    	#Tests signup then preceeds to test login
    	response = self.app.post('/api/v1/register', 
    		data = json.dumps(self.data) , content_type = 'application/json')
    	self.assertEqual(response.status_code, 201)
        result = json.loads(response.data)
        self.assertEqual(result["username"], "zeus")
        self.assertEqual(result["email"], "email@gmail.com")
        self.assertEqual(result["password"], "4084")
        self.assertEqual(result["message"], "You are logged in")
        res = self.app.get('/api/v1/login')
        self.assertEqual(res.status_code, 200)


    def test_already_registered_user(self):
    	#Test User can not be registered twice
    	res = self.app.post('/api/v1/register',
    			data = json.dumps(self.data) , content_type = 'application/json'
    		)
    	self.assertEqual(res.status_code, 201)
    	response = self.app.post('/api/v1/register',
    			data = json.dumps(self.data) , content_type = 'application/json'
    		)
    	self.assertEqual(response.status_code, 202)
    	result = json.loads(second_res.data.decode())
    	self.assertEqual(
           result['message'], "User already exists. Please login.")






if __name__ == '__main__':
    unittest.main()
      