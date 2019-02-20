"""
Redflag routes
"""
from flask import Blueprint
from api.incidents.controllers import IncidentsController
from api.auth.helpers import token_required, is_admin

incidents = Blueprint('incidents', __name__)
incidents_controller = IncidentsController()


@incidents.route("/incidents", methods=["GET"])
@token_required
def get_incidents(current_user):
    """
    api endpoint to fetch incidents
    """
    return incidents_controller.fetch_incidents()


@incidents.route("/incidents", methods=['POST'])
@token_required
def post_incident(current_user):
    """
    api endpoint to create redflag and intervention
    incidents
    """
    return incidents_controller.create_incident(current_user)


@incidents.route("/incidents/<int:incident_id>", methods=['GET'])
@token_required
def get_incident(current_user, incident_id):
    """
    api endpoint to fetch an incident
    """
    return incidents_controller.fetch_incident(incident_id)


@incidents.route("/incidents/<int:incident_id>", methods=['PUT'])
@token_required
def update_incident(current_user, incident_id):
    """
    api endpoint to update a redflag and interventions
    incident
    """
    return incidents_controller.edit_incident(current_user, incident_id)


@incidents.route("/incidents/<int:incident_id>", methods=['GET'])
@token_required
def get_intervention(current_user, incident_id):
    """
    api endpoint to fetch an incident record
    """
    return incidents_controller.fetch_incident(incident_id)


# Admin protected routes
# Only the admin can perform these tasks
@incidents.route("/incidents/<int:incident_id>", methods=['DELETE'])
@is_admin
def delete_incident(incident_id):
    """
    api endpoint to delete an intervention incident
    """
    return incidents_controller.delete_incident(incident_id)
