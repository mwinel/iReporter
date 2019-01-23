"""
redflag unit tests
"""
import json
from tests.base import BaseTestCase


class RedflagTestCase(BaseTestCase):
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
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 201)
        self.assertTrue(result["message"] == "Incident successfully created.")

    def test_create_redflag_with_missing_status(self):
        """Test API cannot create redflag with missing status field."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["status"] = " "
        rv = self.app.post(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] ==
                        "Status field cannot be left empty.")

    def test_create_redflag_with_missing_incident_type(self):
        """Test API cannot create incident with missing incident field."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["incident_type"] = " "
        rv = self.app.post(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
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
        self.redflag["location"] = " "
        rv = self.app.post(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] ==
                        "Location field cannot be left empty.")

    def test_create_redflag_with_missing_image(self):
        """Test API cannot create redflag with missing image field."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["image"] = " "
        rv = self.app.post(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] == "Image field cannot be left empty.")

    def test_create_redflag_with_missing_video(self):
        """Test API cannot create redflag with missing video field."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["video"] = " "
        rv = self.app.post(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] == "Video field cannot be left empty.")

    def test_create_redflag_with_missing_comment(self):
        """Test API cannot create redflag with missing comment field."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["comment"] = " "
        rv = self.app.post(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] ==
                        "Comment field cannot be left empty.")

    def test_create_redflag_with_invalid_image(self):
        """Test API cannot create redflag with wrong image format."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["image"] = "image 1"
        rv = self.app.post(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] == "Invalid image format.")

    def test_create_redflag_with_invalid_video(self):
        """Test API cannot create redflag with wrong video format."""

        res = self.app.post(
            'api/v2/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["video"] = "image 1"
        rv = self.app.post(
            '/api/v2/red-flags',
            headers={'Authorization': auth_token['access_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] == "Invalid video format.")

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
