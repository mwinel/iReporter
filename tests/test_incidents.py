"""
redflag unit tests
"""
import json
from tests.base import BaseTestCase


class IncidentTestCase(BaseTestCase):
    """Test redflag api endpoints."""

    def test_create_redflag(self):
        """Test API can create redflag."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.post(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 201)
        self.assertTrue(result["message"] == "Incident successfully created.")

    def test_create_redflag_with_missing_incident_type(self):
        """Test API cannot create incident with missing incident field."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.incident["incident_type"] = " "
        rv = self.app.post(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] ==
                        "Incident Type field cannot be left empty.")

    def test_create_redflag_with_missing_location(self):
        """Test API cannot create redflag with missing location field."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.incident["location"] = " "
        rv = self.app.post(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] ==
                        "Location field cannot be left empty.")

    def test_create_redflag_with_missing_comment(self):
        """Test API cannot create redflag with missing comment field."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.incident["comment"] = " "
        rv = self.app.post(
            '/api/v2/red-flags',
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

    def test_get_redflags(self):
        """Test API can fetch all redflags."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.get(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 200)
        self.assertTrue(result["message"] == "success")

    def test_get_a_specific_redflag(self):
        """Test API can fetch a specific redflag by its id."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        res = self.app.post(
            'api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        rv = self.app.get(
            '/api/v2/red-flags/1',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 200)
        self.assertTrue(result["message"] == "success")

    def test_get_a_non_existing_redflag(self):
        """Test API cannot fetch a non existing redflag."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.get(
            '/api/v2/red-flags/10000000',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 404)
        self.assertTrue(result["message"] == "Redflag Not Found.")

    def test_update_a_redflag(self):
        """Test API can update a redflag given its id."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.post(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        self.assertTrue(rv.status_code, 201)
        self.incident["comment"] = "stolen Education money"
        res = self.app.put(
            '/api/v2/red-flags/1',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        result = json.loads(res.data.decode())
        self.assertTrue(res.status_code, 201)
        self.assertTrue(result["message"] == "Incident successfully updated.")

    def test_update_a_non_existing_redflag(self):
        """Test API cannot update a non existing redflag."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.put(
            '/api/v2/red-flags/20000',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 404)
        self.assertTrue(result["message"] == "Incident was not found.")

    def test_remove_a_specific_redflag(self):
        """Test API can delete a specific redflag."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.post(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        result = self.app.delete(
            '/api/v2/red-flags/1',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        self.assertTrue(result.status_code, 200)

    def test_remove_a_non_existing_redflag(self):
        """Test API can delete a non existing redflag."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        result = self.app.delete(
            '/api/v2/red-flags/1000',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        self.assertTrue(result.status_code, 404)

    def test_get_interventions(self):
        """Test API can fetch all interventions."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.get(
            '/api/v2/interventions',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 200)
        self.assertTrue(result["message"] == "success")

    def test_get_intervention(self):
        """Test API can fetch an intervention."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.incident['incident_type'] = "intervention"
        res = self.app.post(
            'api/v2/interventions',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident)
        )
        rv = self.app.get(
            '/api/v2/interventions/1',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        self.assertTrue(rv.status_code, 200)

    def test_get_non_existing_intervention(self):
        """Test API cannot fetch a non existing intervention."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        rv = self.app.get(
            '/api/v2/interventions/10000',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        self.assertTrue(rv.status_code, 404)

    def test_remove_a_specific_intervention(self):
        """Test API can delete a specific intervention."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.admin)
        )
        response = self.app.post(
            'api/v2/auth/login',
            content_type='application/json',
            data=json.dumps({"username": "paulk", "password": "654321"})
        )
        auth_token = json.loads(response.data.decode())
        rv = self.app.post(
            '/api/v2/interventions',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.incident2)
        )
        self.assertTrue(rv.status_code, 201)
        result = self.app.delete(
            '/api/v2/interventions/1',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        self.assertTrue(result.status_code, 200)

    def test_remove_a_non_existing_intervention(self):
        """Test API can delete a non existing redflag."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        result = self.app.delete(
            '/api/v2/interventions/1000',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json'
        )
        self.assertTrue(result.status_code, 404)
