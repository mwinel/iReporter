import unittest
from api import app

class TestIndex(unittest.TestCase):
    """ This class represents the index test case. """

    def setUp(self):
        """ Define index test variables and initialize app. """
        self.app = app.test_client()

    def test_index_api_endpoint(self):
        rv = self.app.get('api/v1/index')
        self.assertTrue(rv.status_code, 200)
        self.assertIn('Welcome to iReporter', str(rv.data)) 