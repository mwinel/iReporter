"""
tests base case
"""

import unittest
from api import app
from db.database import DbConnection

class BaseTestCase(unittest.TestCase):
    """Tests base case."""

    def setUp(self):
        """Define tests variables and initialize the app."""
        self.app = app.test_client()
        self.db = DbConnection()
        self.user = {
            "firstname": "moureen",
            "lastname": "murungi",
            "othernames": "molly",
            "username": "more",
            "email": "molly@live.com",
            "password": "654321",
            "phone_number": "256 781916565"
        }
        self.redflag = {
            "title": "stolen HIV/AIDS money",
            "redflag_type": "red-flag",
            "location": "lat long cordinates",
            "status": "draft",
            "image": "image1.jpg",
            "video": "video.mkv",
            "comment": "Alot of money has stolen since 2010."
        }
        self.redflag2 = {
            "title": "stolen HIV/AIDS money",
            "redflag_type": "red-flag",
            "location": "jinja",
            "status": "draft",
            "image": "image2.jpeg",
            "video": "video2.mp4",
            "comment": "Alot of money has stolen since 2010."
        }

    def tearDown(self):
        self.db.drop_tables()
