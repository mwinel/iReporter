"""
Redflag routes
"""
from flask import Blueprint, jsonify
from api.incidents.controllers import IncidentsController
from api.auth.helpers import token_required

incidents = Blueprint('incidents', __name__)
incidents_controller = IncidentsController()


@incidents.route("/red-flags", methods=['POST'])
@incidents.route("/interventions", methods=['POST'])
@token_required
def post_incident(current_user):
    """
    api endpoint to create redflag and interventions
    incident
    """
    return incidents_controller.create_incident(current_user)


@incidents.route("/red-flags/<int:incident_id>", methods=['PUT'])
@incidents.route("/interventions/<int:incident_id>", methods=['PUT'])
@token_required
def update_incident(current_user, incident_id):
    """
    api endpoint to update a redflag and interventions
    incident
    """
    return incidents_controller.edit_incident(current_user, incident_id)


@incidents.route("/red-flags", methods=["GET"])
@token_required
def get_redflags(current_user):
    """
    api endpoint to fetch redflags
    """
    return incidents_controller.fetch_redflags()


@incidents.route("/red-flags/<int:incident_id>", methods=['GET'])
@token_required
def get_redflag(current_user, incident_id):
    """
    api endpoint to fetch a redflag
    """
    return incidents_controller.fetch_redflag(incident_id)


@incidents.route("/red-flags/<int:incident_id>", methods=['DELETE'])
@token_required
def delete_redflag(current_user, incident_id):
    """
    api endpoint to delete a redflag
    """
    if current_user['is_admin'] is True:
        return incidents_controller.delete_redflag(incident_id)
    return jsonify({
        "status": 403,
        "message": "Cannot perform this task."
    }), 403


@incidents.route("/interventions", methods=["GET"])
@token_required
def get_interventions(current_user):
    """
    api endpoint to fetch interventions
    """
    return incidents_controller.fetch_interventions()


@incidents.route("/interventions/<int:incident_id>", methods=['GET'])
@token_required
def get_intervention(current_user, incident_id):
    """
    api endpoint to fetch an intervention incident
    """
    return incidents_controller.fetch_intervention(incident_id)


@incidents.route("/interventions/<int:incident_id>", methods=['DELETE'])
@token_required
def delete_intervention(current_user, incident_id):
    """
    api endpoint to delete an intervention incident
    """
    if current_user['is_admin'] is True:
        return incidents_controller.delete_intervention(incident_id)
    return jsonify({
        "status": 403,
        "message": "Cannot perform this task."
    }), 403
