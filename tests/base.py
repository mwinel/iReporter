import unittest
import json
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
        self.redflag = {
            "title": "stolen HIV/AIDS money",
            "redflagType": "red-flag",
            "location": "lat long cordinates",
            "status": "draft",
            "image": "Image 1",
            "video": "Image 1",
            "comment": "Alot of money has stolen since 2010."
        }
 
    def tearDown(self):
        pass