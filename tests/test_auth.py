import json
from tests.base import BaseTestCase

class TestUserAuth(BaseTestCase):
    """Test auth api endpoints."""

    def test_signup_user(self):
        """Test user signup."""

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 201)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["status"], "User successfully created.")

    def test_signup_user_twice(self):
        """Test user cannot signup twice."""

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 201)                   

        user2 = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": "molly@live.com",
            "password": "123456",
	        "phoneNumber": "256 781916565"
        }

        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user2)
        )                   
        self.assertTrue(res.status_code, 400)
        status = json.loads(res.data.decode())
        self.assertEqual(status["error"], "User with username 'more' already exists.")

    def test_signup_with_invalid_email(self):
        """Test user cannot signup with an invalid email."""

        self.user["email"] = "mollylive.com"

        rv = self.app.post(
            'api/v1/auth/signup', 
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Enter a valid email address.")
        
    def test_signup_with_short_password(self):
        """Test user cannot signup with a short password."""

        self.user["password"] = "1234"

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Password too short.")

    def test_signup_with_missing_firstname(self):
        """Test user cannot signup with missing firstname field."""

        self.user["firstname"] = " "
        
        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Firstname field cannot be left empty.")

    def test_signup_with_missing_lastname(self):
        """Test user cannot signup with missing lastname field."""

        self.user["lastname"] = " "

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Lastname field cannot be left empty.")

    def test_signup_with_missing_othernames(self):
        """Test user cannot signup with missing othernames field."""

        self.user["othernames"] = " "

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Othernames field cannot be left empty.")

    def test_signup_with_missing_username(self):
        """Test user cannot signup with missing username field."""
        
        self.user["username"] = " "

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Username field cannot be left empty.")

    def test_signup_with_missing_email(self):
        """Test user cannot signup with missing email field."""
        
        self.user["email"] = " "

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Email field cannot be left empty.")

    def test_signup_with_missing_password(self):
        """Test user cannot signup with missing password field."""

        self.user["password"] = " "

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Password field cannot be left empty.")

    def test_signup_with_missing_phonenumber(self):
        """Test user cannot signup with missing phonenumber field."""

        self.user["phoneNumber"] = " "

        rv = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 400)
        status = json.loads(rv.data.decode())
        self.assertEqual(status["error"], "Phone number field cannot be left empty.")                                          