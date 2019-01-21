"""
index unit tests
"""

from tests.base import BaseTestCase

class TestIndex(BaseTestCase):
    """Test index api endpoint."""

    def test_index_api_endpoint(self):
        """Test api index endpoint."""
        rv = self.app.get('api/v2/index')
        self.assertTrue(rv.status_code, 200)
        self.assertIn('Welcome to iReporter', str(rv.data))
        self.assertTrue(rv.content_type == 'application/json')
