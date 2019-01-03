import json
import unittest
from api import app


class RedflagTestCase(unittest.TestCase):
    """Test redflag api endpoints."""

    def setUp(self):
        """Define tests variables and initialize the app."""
        self.app = app.test_client()
        self.redflag = {
            "title": "stolen HIV/AIDS money",
            "redflagType": "red-flag",
            "location": "lat long cordinates",
            "status": "draft",
            "image": "Image 1",
            "video": "Image 1",
            "comment": "Alot of money has stolen since 2010."
        }

    def signup_user(self, firstname="molly", lastname="murungi", othernames="molly",
                    username="molison", email="molly@live.com", password="654321",
                    phoneNumber="256 781916565"):

        user_data = {
            "firstname": firstname,
            "lastname": lastname,
            "othernames": othernames,
            "username": username,
            "email": email,
            "password": password,
            "phoneNumber": phoneNumber
        }
        return self.app.post(
                '/api/v1/auth/signup',
                content_type='application/json',
                data=json.dumps(user_data)
            )

    def login_registered_user(self, username="molison", password="654321"):

        login_data = {
            "username": username,
            "password": password
        }
        return self.app.post(
                '/api/v1/auth/login', 
                content_type='application/json',
                data=json.dumps(login_data)
            )

    def test_get_users(self):
        """Test API can fetch all users."""

        res = self.signup_user()
        auth_token = json.loads(res.data.decode()).get('auth_token')
        rv = self.app.get(
            '/api/v1/auth/users',
            headers=dict(Authorization="Bearer " + str(auth_token)),
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(res.status_code, 200)

    def test_create_redflag(self):
        """Test API can create a redflag."""

        res = self.signup_user()
        auth_token = json.loads(res.data.decode()).get('auth_token')
        rv = self.app.post(
            '/api/v1/red-flags',
            headers=dict(Authorization="Bearer " + auth_token),
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 201)
        self.assertTrue(result["message"] == "Redflag successfully created.")