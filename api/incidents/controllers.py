"""
incident controller
"""
import datetime
from flask import request, jsonify
from db.database import DatabaseConnection
from api.incidents.validators import IncidentValidations
from api.incidents.helpers import (get_redflags_by_redflag_type,
                                   get_interventions_by_intervention_type)

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
        validate_media = incident_validations.validate_incident_media(
            images, videos)
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

    def fetch_redflags(self):
        """
        returns a list with redflags
        """
        redflags = get_redflags_by_redflag_type()
        return jsonify({
            "status": 200,
            "redflags": redflags,
            "message": "success"
        }), 200

    def edit_incident(self, current_user, incident_id):
        """
        updates an incident
        """
        incident = db.get_by_argument('incidents', 'incident_id', incident_id)
        if incident:
            if int(incident['created_by']) == int(current_user['user_id']):
                data = request.get_json()
                incident_type = data.get('incident_type', incident['incident_type'])
                location = data.get('location', incident['location'])
                status = data.get('status', incident['status'])
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

    def fetch_redflag(self, incident_id):
        """
        returns a single redflag incident
        """
        redflags = get_redflags_by_redflag_type()
        redflag = [
            redflag for redflag in redflags if redflag['incident_id'] == incident_id]
        if redflag:
            return jsonify({
                "status": 200,
                "redflag": redflag,
                "message": "success"
            }), 200
        return jsonify({
            "status": 404,
            "message": "Redflag Not Found."
        })

    def delete_redflag(self, incident_id):
        """
        deletes a redflag incident
        """
        redflags = get_redflags_by_redflag_type()
        redflag = [
            redflag for redflag in redflags if redflag['incident_id'] == incident_id]
        if redflag:
            db.delete_by_argument('incidents', 'incident_id', incident_id)
            return jsonify({
                "status": 200,
                "message": "Redflag successfully deleted."
            }), 200
        return jsonify({
            "status": 404,
            "message": "Redflag Not Found."
        })

    def fetch_interventions(self):
        """
        returns a list with intervention incidents
        """
        interventions = get_interventions_by_intervention_type()
        return jsonify({
            "status": 200,
            "redflags": interventions,
            "message": "success"
        }), 200

    def fetch_intervention(self, incident_id):
        """
        returns a single intervention incident
        """
        interventions = get_interventions_by_intervention_type()
        intervention = [
            intervention for intervention in interventions \
            if intervention['incident_id'] == incident_id]
        if intervention:
            return jsonify({
                "status": 200,
                "redflag": intervention,
                "message": "success"
            }), 200
        return jsonify({
            "status": 404,
            "message": "Intervention Not Found."
        })

    def delete_intervention(self, incident_id):
        """
        deletes an intervention incident
        """
        interventions = get_interventions_by_intervention_type()
        intervention = [
            intervention for intervention in interventions \
            if intervention['incident_id'] == incident_id]
        if intervention:
            db.delete_by_argument('incidents', 'incident_id', incident_id)
            return jsonify({
                "status": 200,
                "message": "Intervention successfully deleted."
            }), 200
        return jsonify({
            "status": 404,
            "message": "Intervention Not Found."
        })
