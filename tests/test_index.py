from tests.base import BaseTestCase

class TestIndex(BaseTestCase):
    """ Test index api endpoint. """

    def test_index_api_endpoint(self):
        rv = self.app.get('api/v1/index')
        self.assertTrue(rv.status_code, 200)
