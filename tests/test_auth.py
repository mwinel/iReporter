"""
auth unit tests
"""
import json
from tests.base import BaseTestCase


class TestUserAuth(BaseTestCase):
    """Test auth api endpoints."""

    def test_signup_user(self):
        """Test user signup."""

        rv = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 201)
        self.assertTrue(result["status"] == 201)
        self.assertTrue(result["message"] == "User successfully created.")

    def test_signup_user_twice(self):
        """Test user cannot signup twice."""

        rv = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 201)
        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(res.data.decode())
        self.assertTrue(res.status_code, 202)
        self.assertTrue(result["status"] == 202)
        self.assertTrue(result["message"] ==
                        "User already exists. Please login.")

    def test_signup_with_invalid_email(self):
        """Test user cannot signup with an invalid email."""

        self.user["email"] = "mollylive.com"
        rv = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["status"] == 400)
        self.assertTrue(result["error"] == "Enter a valid email address.")

    def test_signup_with_missing_firstname(self):
        """Test user cannot signup with missing firstname field."""

        self.user["firstname"] = " "
        rv = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["status"] == 400)
        self.assertTrue(result["error"] ==
                        "Firstname field cannot be left empty.")

    def test_signup_with_missing_lastname(self):
        """Test user cannot signup with missing lastname field."""

        self.user["lastname"] = " "
        rv = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["status"] == 400)
        self.assertTrue(result["error"] ==
                        "Lastname field cannot be left empty.")

    def test_signup_with_missing_username(self):
        """Test user cannot signup with missing username field."""

        self.user["username"] = " "
        rv = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["status"] == 400)
        self.assertTrue(result["error"] ==
                        "Username field cannot be left empty.")

    def test_signup_with_missing_email(self):
        """Test user cannot signup with missing lastname field."""

        self.user["email"] = " "
        rv = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["status"] == 400)
        self.assertTrue(result["error"] == "Email field cannot be left empty.")

    def test_signup_with_missing_password(self):
        """Test user cannot signup with missing password field."""

        self.user["password"] = " "
        rv = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["status"] == 400)
        self.assertTrue(result["error"] ==
                        "Password field cannot be left empty.")

    def test_signup_with_missing_othernames(self):
        """Test user cannot signup with missing othernames field."""

        self.user["othernames"] = " "
        rv = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["status"] == 400)
        self.assertTrue(result["error"] ==
                        "Othernames field cannot be left empty.")

    def test_signup_with_missing_phonenumber(self):
        """Test user cannot signup with missing phonenumber field."""

        self.user["phone_number"] = " "
        rv = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["status"] == 400)
        self.assertTrue(result["error"] ==
                        "Phone number field cannot be left empty.")

    def test_signup_with_short_password(self):
        """Test user cannot signup with short password."""

        self.user["password"] = "1234"
        rv = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["status"] == 400)
        self.assertTrue(
            result["error"] == "Password too short, must be atleast 6 characters or more.")

    def test_login_for_registered_user(self):
        """Test registered user can successfully login."""

        registered_user = {
            "username": "more",
            "password": "654321"
        }
        # signup user
        rv = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(rv.status_code, 201)
        # Login registered user
        res = self.app.post(
            'api/v2/auth/login',
            content_type='application/json',
            data=json.dumps(registered_user)
        )
        result = json.loads(res.data.decode())
        self.assertTrue(res.status_code, 200)
        self.assertTrue(result["message"] == "Successfully logged in.")

    def test_login_for_non_registered_user(self):
        """Test non registered user cannot successfully login."""

        non_registered_user = {
            "username": "isaac",
            "password": "123456"
        }
        # Login registered user
        res = self.app.post(
            'api/v2/auth/login',
            content_type='application/json',
            data=json.dumps(non_registered_user)
        )
        result = json.loads(res.data.decode())
        self.assertTrue(res.status_code, 200)
        self.assertTrue(result["error"] ==
                        "User does not exist. Please signup.")

    def test_user_login_with_invalid_credentials(self):
        """Test user cannot successfully login with invalid credentials."""

        # Register user
        rv = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 201)
        # Login registered user
        res = self.app.post(
            'api/v2/auth/login',
            content_type='application/json',
            data=json.dumps({"username": "more", "password": "654329"})
        )
        result = json.loads(res.data.decode())
        self.assertTrue(res.status_code, 401)
        self.assertTrue(result["status"] == 401)
        self.assertTrue(result["error"] == "Invalid Credentials!")

    def test_get_all_users(self):
        """Test is API returns a list of users."""

        # signup user
        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        self.assertTrue(res.status_code, 201)
        # login user
        response = self.app.post(
            'api/v2/auth/login',
            content_type='application/json',
            data=json.dumps({"username": "more", "password": "654321"})
        )
        auth_token = json.loads(response.data.decode())
        rv = self.app.get(
            'api/v2/users',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        self.assertTrue(rv.status_code, 200)

    def test_get_all_users_with_invalid_token(self):
        """Test is API cannit returns list of users with invalid token."""

        rv = self.app.get(
            'api/v2/users',
            headers={'Authorization': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDg\
                                       yMzM5NDMsImlhdCI6MTU0ODIzMzg4Mywic3ViIjoibXdpbmVsIn0.\
                                       JOegZPMtfiuoSjddQ-XfJabF232K5mR7N9Bju_yeoY"},
            content_type='application/json'
        )
        self.assertTrue(rv.status_code, 401)

    def test_get_all_users_with_missing_token(self):
        """Test is API cannit returns list of users with missing token."""

        rv = self.app.get(
            'api/v2/users',
            content_type='application/json'
        )
        self.assertTrue(rv.status_code, 401)
