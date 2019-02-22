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
        data = request.get_json(force=True)
        incident_type = data['incident_type']
        location = data['location']
        status = 'draft'
        images = data['images']
        videos = data['videos']
        comment = data['comment']
        created_on = datetime.datetime.now()
        created_by = current_user.get('user_id')
        # validate incident
        validate_input = incident_validations.validate_incident_input(status, incident_type,
                                                                      location, comment)
        if validate_input:
            return jsonify({
                "status": 400,
                "error": validate_input
            }), 400
        incident = db.insert_incident_data(incident_type, location, status,
                                           images, videos, comment, created_on, created_by)
        return jsonify({
            "status": 201,
            "message": "Incident successfully created.",
            "data": incident
        }), 201

    def fetch_incidents(self):
        """
        returns all incidents
        """
        incidents = db.fetch_all('incidents')
        return jsonify({
            "status": 200,
            "incidents": incidents,
            "message": "success"
        }), 200

    def fetch_incidents_by_user(self, current_user):
        """
        returns all incidents of a given user
        """
        created_by = current_user["user_id"]
        incidents = db.get_all_by_argument(
            'incidents', 'created_by', created_by)
        return jsonify({
            "status": 200,
            "incidents": incidents,
            "message": "success"
        }), 200

    def fetch_incident(self, incident_id):
        """
        returns a single incident
        """
        incident = db.get_by_argument('incidents', 'incident_id', incident_id)
        if incident:
            return jsonify({
                "status": 200,
                "incident": incident,
                "message": "success"
            }), 200
        return jsonify({
            "status": 404,
            "message": "Incident Not Found."
        })

    def edit_incident(self, current_user, incident_id):
        """
        updates an incident
        """
        incident = db.get_by_argument('incidents', 'incident_id', incident_id)
        if incident:
            if int(incident['created_by']) == int(current_user['user_id']):
                data = request.get_json()
                incident_type = data.get(
                    'incident_type', incident['incident_type'])
                location = data.get('location', incident['location'])
                status = "draft"
                images = data.get('images', incident['images'])
                videos = data.get('videos', incident['videos'])
                comment = data.get('comment', incident['comment'])
                new_incident = db.update_incident(incident_type, location, status, images,
                                                  videos, comment, incident_id)
                return jsonify({
                    "status": 201,
                    "message": "Incident successfully updated.",
                    "data": new_incident
                }), 201
            return jsonify({
                "status": 403,
                "message": "You cannot edit this incident."
            }), 403
        return jsonify({
            "status": 404,
            "message": "Incident was not found.",
        }), 404

    def delete_incident(self, incident_id):
        """
        deletes an incident record
        """
        incidents = db.fetch_all('incidents')
        incident = [
            incident for incident in incidents if incident['incident_id'] == incident_id]
        if incident:
            db.delete_by_argument('incidents', 'incident_id', incident_id)
            return jsonify({
                "status": 200,
                "message": "Incident successfully deleted."
            }), 200
        return jsonify({
            "status": 404,
            "message": "Incident Not Found."
        })

    def edit_incident_status(self, incident_id):
        """
        updates incident status
        """
        data = request.get_json(force=True)
        status = data["status"]
        incident = db.get_by_argument('incidents', 'incident_id', incident_id)
        if incident:
            db.update_incident_status(status, incident_id)
            return jsonify({
                "status": 201,
                "message": "Successfully updated incident status."
            }), 201
        return jsonify({
            "status": 404,
            "error": "Incident not found."
        }), 404
