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
