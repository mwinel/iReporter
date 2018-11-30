import unittest
from api import app

class BaseTestCase(unittest.TestCase):
    """ Tests base case. """

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass
