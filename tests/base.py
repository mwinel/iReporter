"""
tests base case
"""
import unittest
from api import app
from db.database import DatabaseConnection

class BaseTestCase(unittest.TestCase):
    """Tests base case."""

    def setUp(self):
        """Define tests variables and initialize the app."""
        self.app = app.test_client()
        self.db = DatabaseConnection()
        self.db.create_tables()
        self.user = {
            "firstname": "moureen",
            "lastname": "murungi",
            "othernames": "molly",
            "username": "more",
            "email": "molly@live.com",
            "password": "654321",
            "phone_number": "256 781916565"
        }

    def tearDown(self):
        self.db.drop_tables()
