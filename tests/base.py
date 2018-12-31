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
            "password": "654321",
            "phoneNumber": "256 781916565"
        }

        self.register_user = {
            "firstname": "paul",
            "lastname": "kasami",
            "othernames": "polo",
            "username": "polok",
            "email": "polok@live.com",
            "password": "654321",
            "phoneNumber": "256 781916565"
        }

        self.login_user = {
            "username": "more",
            "password": "654321"
        }
 
    def tearDown(self):
        pass