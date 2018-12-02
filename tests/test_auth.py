import json
from tests.base import BaseTestCase

class TestUserAuth(BaseTestCase):
    """ Test auth api endpoints. """

    def test_user_signup(self):
        
        user = {
	        "firstname": "nelson",
	        "lastname": "murungi",
	        "othernames": "mwirumubi",
	        "username": "mwinel",
	        "email": "mwinel@live.com",
	        "phoneNumber": "256 781 916565"
        }

        rv = self.app.post('api/v1/auth/signup', content_type='application/json',
                           data=json.dumps(user))
        self.assertTrue(rv.status_code, 201)
        res = json.loads(rv.data.decode())
        self.assertEqual(res['status'], "User successfully created.")