"""
incident unit tests
"""
import json
from tests.base import BaseTestCase


class IncidentTestCase(BaseTestCase):
    """Test incident api endpoints."""

    def test_create_incident(self):
        """Test API can create incident."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.post(
            '/api/v2/incidents',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 201)
        self.assertTrue(result["message"] == "Incident successfully created.")

    def test_create_incident_with_missing_incident_type(self):
        """Test API cannot create incident with missing incident type field."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.incident["incident_type"] = " "
        rv = self.app.post(
            '/api/v2/incidents',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] ==
                        "Incident Type field cannot be left empty.")

    def test_create_incident_with_missing_location(self):
        """Test API cannot create incident with missing location field."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.incident["location"] = " "
        rv = self.app.post(
            '/api/v2/incidents',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] ==
                        "Location field cannot be left empty.")

    def test_create_incident_with_missing_comment(self):
        """Test API cannot create incident with missing comment field."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.incident["comment"] = " "
        rv = self.app.post(
            '/api/v2/incidents',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] ==
                        "Comment field cannot be left empty.")

    def test_get_incidents(self):
        """Test API can fetch all incidents."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.get(
            '/api/v2/incidents',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 200)
        self.assertTrue(result["message"] == "success")

    def test_get_a_specific_incident(self):
        """Test API can fetch a specific incident by its id."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        res = self.app.post(
            'api/v2/incidents',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        rv = self.app.get(
            '/api/v2/incidents/1',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 200)
        self.assertTrue(result["message"] == "success")

    def test_get_user_incidents(self):
        """Test API can fetch all incidents by a given user."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.get(
            '/api/v2/user-incidents',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 200)
        self.assertTrue(result["message"] == "success")

    def test_get_a_non_existing_incident(self):
        """Test API cannot fetch a non existing incident record."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.get(
            '/api/v2/incidents/10000000',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 404)
        self.assertTrue(result["message"] == "Incident Not Found.")

    def test_update_an_incident(self):
        """Test API can update an incident record given its id."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.post(
            '/api/v2/incidents',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        self.assertTrue(rv.status_code, 201)
        self.incident["comment"] = "stolen Education money"
        res = self.app.put(
            '/api/v2/incidents/1',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        result = json.loads(res.data.decode())
        self.assertTrue(res.status_code, 201)
        self.assertTrue(result["message"] == "Incident successfully updated.")

    def test_update_a_non_existing_incident(self):
        """Test API cannot update a non existing incident."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.put(
            '/api/v2/incidents/20000',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 404)
        self.assertTrue(result["message"] == "Incident was not found.")

    def test_remove_a_specific_incident(self):
        """Test API can delete a specific incident."""

        user_login = {"username": "paulk", "password": "654321"}
        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.admin)
        )
        self.assertTrue(res.status_code, 201)
        login = self.app.post(
            'api/v2/auth/login',
            content_type='application/json',
            data=json.dumps(user_login)
        )
        auth_token = json.loads(login.data.decode())
        rv = self.app.post(
            '/api/v2/incidents',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        self.assertTrue(rv.status_code, 200)
        result = self.app.delete(
            '/api/v2/incidents/1',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        self.assertTrue(result.status_code, 200)

    def test_remove_a_non_existing_incident(self):
        """Test API can delete a non existing incident."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.admin)
        )
        auth_token = json.loads(res.data.decode())
        result = self.app.delete(
            '/api/v2/incidents/1000',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        self.assertTrue(result.status_code, 404)

    def test_get_an_incident(self):
        """Test API can fetch an incident record."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.incident['incident_type'] = "intervention"
        res = self.app.post(
            'api/v2/incidents',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        rv = self.app.get(
            '/api/v2/incidents/1',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        self.assertTrue(rv.status_code, 200)
