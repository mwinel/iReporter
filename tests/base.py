import unittest
from api import app

class BaseTestCase(unittest.TestCase):
    """Tests base case."""

    def setUp(self):
        """Define tests variables and initialize the app."""
        self.app = app.test_client()
        self.user = {
	        "firstname": "moureen",
	        "lastname": "murungi",
	        "othernames": "molly",
	        "username": "more",
	        "email": "molly@live.com",
            "password": "123456",
	        "phoneNumber": "256 781916565"
        }
 
    def tearDown(self):
        pass