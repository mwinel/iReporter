import json
from tests.base import BaseTestCase


class RedflagTestCase(BaseTestCase):
    """Test redflag api endpoints."""

    def test_create_redflag(self):
        """Test API can create redflag."""

        self.user["username"] = "mya"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.post(
            '/api/v1/red-flags', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 201)
        self.assertTrue(result["message"] == "Redflag successfully created.")

    def test_get_redflags(self):
        """Test API can fetch all redflags."""

        self.user["username"] = "paulk"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )

        auth_token = json.loads(res.data.decode())
        rv = self.app.get(
            '/api/v1/red-flags', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 200)
        self.assertTrue(result["message"] == "success")

    def test_get_a_specific_redflag(self):
        """Test API can fetch a specific redflag by its id."""

        self.user["username"] = "paula"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )

        auth_token = json.loads(res.data.decode())
        rv = self.app.get(
            '/api/v1/red-flags/1',
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 200)
        self.assertTrue(result["message"] == "success")

    def test_get_a_non_existing_specific_redflag(self):
        """Test API cannot fetch a non existing redflag."""

        self.user["username"] = "maria"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )

        auth_token = json.loads(res.data.decode())
        rv = self.app.get(
            '/api/v1/red-flags/100000000',
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 200)
        self.assertTrue(result["message"] == "Sorry! Redflag was not found.")

    def test_remove_a_specific_redflag(self):
        """Test API can delete a specific redflag."""

        self.user["username"] = "carla"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )

        auth_token = json.loads(res.data.decode())
        rv = self.app.delete(
            '/api/v1/red-flags/1',
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 200)
        self.assertTrue(result["message"] == "Redflag successfully deleted.")

    def test_remove_a_non_existing_redflag(self):
        """Test API cannot delete a non existing redflag."""

        self.user["username"] = "samuel"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )

        auth_token = json.loads(res.data.decode())
        rv = self.app.delete(
            '/api/v1/red-flags/9999999999',
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 200)
        self.assertTrue(result["message"] == "Redflag was not found.")

    def test_update_a_redflag(self):
        """Test API can update a redflag given its id."""

        self.user["username"] = "mary"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.post(
            '/api/v1/red-flags', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag2)
        )
        
        rv = self.app.put(
            '/api/v1/red-flags/2', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag_updated)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 201)
        self.assertTrue(result["message"] == "Redflag successfully updated.")

    def test_update_a_non_existing_redflag(self):
        """Test API cannot update a non existing redflag."""

        self.user["username"] = "marylin"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())

        rv = self.app.put(
            '/api/v1/red-flags/20000', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag_updated)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 200)
        self.assertTrue(result["message"] == "Redflag was not found.")