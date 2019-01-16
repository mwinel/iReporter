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

    def test_create_redflag_with_missing_status(self):
        """Test API cannot create redflag with missing status field."""

        self.user["username"] = "mya1"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["status"] = " "
        rv = self.app.post(
            '/api/v1/red-flags', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] == "Status field cannot be left empty.")

    def test_create_redflag_with_missing_title(self):
        """Test API cannot create redflag with missing title field."""

        self.user["username"] = "mya2"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["title"] = " "
        rv = self.app.post(
            '/api/v1/red-flags', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] == "Title field cannot be left empty.")

    def test_create_redflag_with_missing_redflag_type(self):
        """Test API cannot create redflag with missing redflag field."""

        self.user["username"] = "mya3"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["redflagType"] = " "
        rv = self.app.post(
            '/api/v1/red-flags', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] == "Redflag Type field cannot be left empty.")

    def test_create_redflag_with_missing_location(self):
        """Test API cannot create redflag with missing location field."""

        self.user["username"] = "mya4"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["location"] = " "
        rv = self.app.post(
            '/api/v1/red-flags', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] == "Location field cannot be left empty.")

    def test_create_redflag_with_missing_image(self):
        """Test API cannot create redflag with missing image field."""

        self.user["username"] = "mya5"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["image"] = " "
        rv = self.app.post(
            '/api/v1/red-flags', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] == "Image field cannot be left empty.")

    def test_create_redflag_with_missing_video(self):
        """Test API cannot create redflag with missing video field."""

        self.user["username"] = "mya6"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["video"] = " "
        rv = self.app.post(
            '/api/v1/red-flags', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] == "Video field cannot be left empty.")

    def test_create_redflag_with_missing_comment(self):
        """Test API cannot create redflag with missing comment field."""

        self.user["username"] = "mya7"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["comment"] = " "
        rv = self.app.post(
            '/api/v1/red-flags', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] == "Comment field cannot be left empty.")

    def test_create_redflag_with_invalid_image(self):
        """Test API cannot create redflag with wrong image format."""

        self.user["username"] = "mya8"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["image"] = "image 1"
        rv = self.app.post(
            '/api/v1/red-flags', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] == "Invalid image format.")

    def test_create_redflag_with_invalid_video(self):
        """Test API cannot create redflag with wrong video format."""

        self.user["username"] = "mya9"
        res = self.app.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        auth_token = json.loads(res.data.decode())
        self.redflag["video"] = "image 1"
        rv = self.app.post(
            '/api/v1/red-flags', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 400)
        self.assertTrue(result["error"] == "Invalid video format.")

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

        self.user["username"] = "stone"
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
        
        self.redflag["title"] = "stolen Education money"
        res = self.app.put(
            '/api/v1/red-flags/11', 
            headers={'Authorization': "Bearer " + auth_token['auth_token']},
            content_type='application/json',
            data=json.dumps(self.redflag2)
        )
        result = json.loads(res.data.decode())
        self.assertTrue(res.status_code, 201)
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
            data=json.dumps(self.redflag)
        )
        result = json.loads(rv.data.decode())
        self.assertTrue(rv.status_code, 200)
        self.assertTrue(result["message"] == "Redflag was not found.")