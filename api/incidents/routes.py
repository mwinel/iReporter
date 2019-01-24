"""
Redflag routes
"""
from flask import Blueprint
from api.incidents.controllers import IncidentsController
from api.auth.helpers import token_required

incidents = Blueprint('incidents', __name__)
incidents_controller = IncidentsController()


@incidents.route("/red-flags", methods=['POST'])
@token_required
def create_redflag(current_user):
    """
    api endpoint to create redflag
    """
    return incidents_controller.create_incident(current_user)


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


@incidents.route("/red-flags/<int:incident_id>", methods=['PUT'])
# @token_required
def update_redflag(incident_id):
    """
    api endpoint to update a redflag
    """
    return incidents_controller.edit_incident(incident_id)
