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
def get_redflags():
    """
    api endpoint to fetch redflags
    """
    return incidents_controller.fetch_redflags()
