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
        self.admin = {
            "firstname": "paul",
            "lastname": "kasami",
            "othernames": "polk",
            "username": "paulk",
            "email": "paulk@live.com",
            "password": "654321",
            "phone_number": "256 781916565",
            "is_admin": True
        }
        self.user = {
            "firstname": "moureen",
            "lastname": "murungi",
            "othernames": "molly",
            "username": "more",
            "email": "molly@live.com",
            "password": "654321",
            "phone_number": "256 781916565"
        }
        self.incident = {
            "incident_type": "red-flag",
            "location": "lat long cordinates",
            "status": "draft",
            "images": "girl-ethiopian-child-portrait-38634.jpeg",
            "videos": "girl-ethiopian-child-portrait-38634.mkv",
            "comment": "Alot of money has stolen since 2010."
        }
        self.incident2 = {
            "incident_type": "intervention",
            "location": "lat long cordinates",
            "status": "draft",
            "images": "girl-ethiopian-child-portrait-38634.jpeg",
            "videos": "girl-ethiopian-child-portrait-38634.mkv",
            "comment": "Alot of money has stolen since 2010."
        }

    def tearDown(self):
        self.db.drop_tables()
