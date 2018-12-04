import json
from tests.base import BaseTestCase

class TestUserAuth(BaseTestCase):
    """ Test auth api endpoints. """

    def test_signup_user(self):
        
        user = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": "molly@live.com",
            "password": "123456",
	        "phoneNumber": "256 781916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(rv.status_code, 201)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["status"], "User successfully created.")

    def test_signup_user_twice(self):

        user1 = {
	        "firstname": "sally",
	        "lastname": "wanjiru",
	        "othernames": "sallyo",
	        "username": "sallymore",
	        "email": "sallymore@live.com",
            "password": "654321",
	        "phoneNumber": "256 771916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user1))
        self.assertTrue(rv.status_code, 201)                   

        user2 = {
	        "firstname": "sally",
	        "lastname": "wanjiru",
	        "othernames": "sallyo",
	        "username": "sallymore",
	        "email": "sallymore@live.com",
            "password": "654321",
	        "phoneNumber": "256 771916565"
        }

        res = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user2))                   
        self.assertTrue(res.status_code, 400)
        status = json.loads(res.data.decode())
        self.assertEqual(status["error"], "User with username 'sallymore' already exists.")

    def test_signup_invalid_email(self):
        
        user = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": "mollylive.com",
            "password": "123456",
	        "phoneNumber": "256 781916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Enter a valid email address.")
        
    def test_signup_short_password(self):
        
        user = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": "molly@live.com",
            "password": "123",
	        "phoneNumber": "256 781916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Password too short.")

    def test_signup_invalid_email(self):
        
        user = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": "mollylive.com",
            "password": "123456",
	        "phoneNumber": "256 781916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Enter a valid email address.")

    def test_signup_missing_firstname(self):
        
        user = {
	        "firstname": " ",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": "molly@live.com",
            "password": "123456",
	        "phoneNumber": "256 781916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Firstname field cannot be left empty.")

    def test_signup_missing_lastname(self):
        
        user = {
	        "firstname": "moureen",
	        "lastname": " ",
	        "othernames": "molly",
	        "username": "more",
	        "email": "molly@live.com",
            "password": "123456",
	        "phoneNumber": "256 781916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Lastname field cannot be left empty.")

    def test_signup_missing_othernames(self):
        
        user = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": " ",
	        "username": "more",
	        "email": "molly@live.com",
            "password": "123456",
	        "phoneNumber": "256 781916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Othernames field cannot be left empty.")

    def test_signup_username_field(self):
        
        user = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": " ",
	        "email": "molly@live.com",
            "password": "123456",
	        "phoneNumber": "256 781916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Username field cannot be left empty.")

    def test_signup_invalid_email(self):
        
        user = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": "mollylive.com",
            "password": "123456",
	        "phoneNumber": "256 781916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Enter a valid email address.")

    def test_signup_missing_email(self):
        
        user = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": " ",
            "password": "123456",
	        "phoneNumber": "256 781916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Email field cannot be left empty.")

    def test_signup_missing_password(self):
        
        user = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": "sallymore@gmail.com",
            "password": " ",
	        "phoneNumber": "256 781916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Password field cannot be left empty.")

    def test_signup_missing_phonenumber(self):
        
        user = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": "sallymore@gmail.com",
            "password": "123456",
	        "phoneNumber": " "
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Phone number field cannot be left empty.")

    def test_user_login(self):

        user1 = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": "sallymore@gmail.com",
            "password": "123456",
	        "phoneNumber": "0781 916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user1))

        user = {
            "username": "more",
            "password": "123456"
        }

        res = self.app.post('api/v1/auth/login', content_type='application/json',
                            data=json.dumps(user))
        self.assertTrue(res.status_code, 200)
        message = json.loads(res.data.decode())
        self.assertEqual(message["status"], "Successfully logged in.")

    def test_user_login_invalid_credentials(self):

        user1 = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": "sallymore@gmail.com",
            "password": "123456",
	        "phoneNumber": "0781 916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user1))

        user = {
            "username": "more",
            "password": "12346"
        }

        res = self.app.post('api/v1/auth/login', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(res.status_code, 400)
        message = json.loads(res.data.decode())
        self.assertEqual(message["error"], "Invalid Credentials!")

    def test_user_login_not_signedup(self):

        user1 = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": "sallymore@gmail.com",
            "password": "123456",
	        "phoneNumber": "0781 916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user1))

        user1 = {
            "username": "morese",
            "password": "12346"
        }

        res = self.app.post('api/v1/auth/login', content_type='application/json',
                           data=json.dumps(user1))
        self.assertTrue(res.status_code, 200)
        message = json.loads(res.data.decode())
        self.assertEqual(message["error"], "User does not exist.")