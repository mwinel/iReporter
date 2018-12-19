import json
import unittest
from api import app

class TestUsersRoute(unittest.TestCase):
    """ This class represents the users route test case. """

    def setUp(self):
        """ Define auth test variables and initialize app. """
        self.app = app.test_client()
        self.user = {
            "firstname": "sally",
            "lastname": "wanjiru",
            "othernames": "sal",
            "username": "sally01",
            "email": "sally@example.com",
            "password": "123456",
            "phoneNumber": "0772 000222"
        }

    def register_user(self, firstname="sally", lastname="wanjiru",
                      othernames="sal", username="sally01", email="sally@example.com",
                      password="123456", phoneNumber="0772 000222"):
        user_data = {
            'firstname': firstname,
            'lastname': lastname,
            'othernames': othernames,
            'username': username,
            'email': email,
            'password': password,
            'phoneNumber': phoneNumber
        }
        return self.app.post('api/v1/auth/signup', data=json.dumps(user_data))

    def login_user(self, username="sally01", password="123456"):
        user_data = {
            'username': username,
            'password': password
        }
        return self.app.post('api/v1/auth/login', data=json.dumps(user_data)) 

    def test_protected_route(self):
        """ Test API can fetch users. """
        self.register_user()
        result = self.login_user()
        # obtain access token  
        access_token = json.loads(result.data.decode())["access_token"]  

        res = self.app.get(
            'api/v1/auth/users',
            headers=dict(Authorization="Bearer " + access_token),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)