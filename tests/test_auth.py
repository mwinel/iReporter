import json
import unittest
from api import app

class TestUserAuth(unittest.TestCase):
    """ This class represents the auth test case. """

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

    def test_signup_user(self):
        """ Test user signup works well. """
        rv = self.app.post(
            'api/v1/auth/signup', 
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 201)
        self.assertEqual(result["status"], "User successfully created.")

    def test_signup_user_twice(self):
        """ Test user cannot be signed up twice. """
        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 201)
        second_rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(second_rv.data.decode())
        self.assertTrue(second_rv.status_code, 202)
        self.assertEqual(result["error"], "User with username 'sally01' already exists.")

    def test_signup_invalid_email(self):
        """ Test user cannot signup with invalid email. """
        
        user = {
	        "firstname": "sally",
            "lastname": "wanjiru",
            "othernames": "sal",
            "username": "sally01",
            "email": "sallyexample.com",
            "password": "123456",
            "phoneNumber": "0772 000222"
        }

        rv = self.app.post(
            'api/v1/auth/signup', 
            content_type='application/json',
            data=json.dumps(user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertEqual(result["error"], "Enter a valid email address.")
        
    def test_signup_short_password(self):
        """ Test user cannot signup with a short password. """ 
        
        user = {
	        "firstname": "sally",
            "lastname": "wanjiru",
            "othernames": "sal",
            "username": "sally01",
            "email": "sally@example.com",
            "password": "1234",
            "phoneNumber": "0772 000222"
        }

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertEqual(result["error"], "Password too short.")

    def test_signup_missing_firstname(self):
        """ Test user cannot signup with a missing firstname. """
        
        user = {
	        "firstname": " ",
            "lastname": "wanjiru",
            "othernames": "sal",
            "username": "sally01",
            "email": "sally@example.com",
            "password": "123456",
            "phoneNumber": "0772 000222"
        }

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        result = json.loads(rv.data.decode())    
        self.assertTrue(rv.status_code, 400)
        self.assertEqual(result["error"], "Firstname field cannot be left empty.")

    def test_signup_missing_lastname(self):
        """ Test user cannot signup with missing lastname. """
        
        user = {
	        "firstname": "sally",
            "lastname": " ",
            "othernames": "sal",
            "username": "sally01",
            "email": "sally@example.com",
            "password": "123456",
            "phoneNumber": "0772 000222"
        }

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertEqual(result["error"], "Lastname field cannot be left empty.")

    def test_signup_missing_othernames(self):
        """ Test user cannot signup with missing othername. """
        
        user = {
	        "firstname": "sally",
            "lastname": "wanjiru",
            "othernames": " ",
            "username": "sally01",
            "email": "sally@example.com",
            "password": "123456",
            "phoneNumber": "0772 000222"
        }

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertEqual(result["error"], "Othernames field cannot be left empty.")

    def test_signup_missing_username(self):
        """ Test user cannot signup with missing username. """
        
        user = {
	        "firstname": "sally",
            "lastname": "wanjiru",
            "othernames": "sal",
            "username": " ",
            "email": "sally@example.com",
            "password": "123456",
            "phoneNumber": "0772 000222"
        }

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertEqual(result["error"], "Username field cannot be left empty.")
    
    def test_signup_missing_email(self):
        """ Test user cannot signup with missing email. """
        
        user = {
	        "firstname": "sally",
            "lastname": "wanjiru",
            "othernames": "sal",
            "username": "sally01",
            "email": " ",
            "password": "123456",
            "phoneNumber": "0772 000222"
        }

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertEqual(result["error"], "Email field cannot be left empty.")

    def test_signup_missing_password(self):
        """ Test user cannot signup with missing password. """
        
        user = {
	        "firstname": "sally",
            "lastname": "wanjiru",
            "othernames": "sal",
            "username": "sally01",
            "email": "sally@example.com",
            "password": " ",
            "phoneNumber": "0772 000222"
        }

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertEqual(result["error"], "Password field cannot be left empty.")

    def test_signup_missing_phonenumber(self):
        """ Test user cannot signup with missing phonenumber. """
        
        user = {
	        "firstname": "sally",
            "lastname": "wanjiru",
            "othernames": "sal",
            "username": "sally01",
            "email": "sally@example.com",
            "password": "123456",
            "phoneNumber": " "
        }

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertEqual(result["error"], "Phone number field cannot be left empty.")

    def test_user_login(self):
        """ Test registered user can login. """

        rv = self.app.post(
            'api/v1/auth/signup', 
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 201)           

        login_user = {
            "username": "sally01",
            "password": "123456"
        }
        res = self.app.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(login_user)
        )
        result = json.loads(res.data.decode())
        self.assertTrue(res.status_code, 200)
        self.assertEqual(result["status"], "Successfully logged in.")
        self.assertTrue(result["access_token"])

    def test_user_login_invalid_credentials(self):
        """ Test registered user cannot login with invalid credentials. """

        rv = self.app.post(
            'api/v1/auth/signup', 
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 201)           

        login_user = {
            "username": "sally01",
            "password": "623456"
        }
        res = self.app.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(login_user)
        )
        result = json.loads(res.data.decode())
        self.assertTrue(res.status_code, 401)
        self.assertEqual(result["error"], "Invalid Credentials!")