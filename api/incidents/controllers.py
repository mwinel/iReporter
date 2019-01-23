"""
incident controller
"""
import datetime
from flask import request, jsonify
from db.database import DatabaseConnection
from api.incidents.validators import IncidentValidations

db = DatabaseConnection()
incident_validations = IncidentValidations()


class IncidentsController:
    """
    A class used to represent the incidents controller

    ...

    Methods
    ----------
    create_incident
        creates a incident
    fetch_all_incidents
        returns a list of all incidents
    update_incident(incident_id)
        updates a incident given its id
    fetch_incident(incident_id)
        returns a single incident given its id
    delete_incident(incident_id)
        deletes a incident from the incidents_list
    """

    def create_incident(self, current_user):
        """
        creates a incident
        """
        data = request.get_json()
        incident_type = data.get('incident_type')
        location = data.get('location')
        status = data.get('status')
        images = data.get('image')
        videos = data.get('video')
        comment = data.get('comment')
        created_on = datetime.datetime.now()
        created_by = current_user.get('user_id')

        # validate incident
        validate_input = incident_validations.validate_incident_input(status, incident_type,
                                                                      location, comment)
        validate_media = incident_validations.validate_incident_media(images, videos)
        if validate_input:
            return jsonify({
                "status": 400,
                "error": validate_input
            }), 400
        if validate_media:
            return jsonify({
                "status": 400,
                "error": validate_media
            }), 400

        incident = db.insert_incident_data(incident_type, location, status,
                                           images, videos, comment, created_on, created_by)
        return jsonify({
            "status": 201,
            "message": "Incident successfully created.",
            "data": incident
        }), 201

    def fetch_redflags(self):
        incident_type = 'red-flag'
        redflags = db.get_all_by_argument('incidents', 'incident_type', incident_type)
        return jsonify({
            "status": 200,
            "redflags": redflags,
            "message": "success"
        }), 200
