"""
Redflag routes
"""

from flask import Blueprint
from flask_jwt_extended import jwt_required
from api.redflags.controllers import RedFlagsController

redflags = Blueprint('redflags', __name__)
redflags_controller = RedFlagsController()


@redflags.route("/red-flags", methods=['POST'])
@jwt_required
def create_redflag():
    """
    api endpoint to create redflag
    """
    return redflags_controller.create_redflag()


@redflags.route("/red-flags", methods=["GET"])
@jwt_required
def get_redflags():
    """
    api endpoint to fetch redflags
    """
    return redflags_controller.fetch_all_redflags()


@redflags.route("/red-flags/<int:redflag_id>", methods=["PUT"])
@jwt_required
def edit_redflag(redflag_id):
    """
    api endpoint to update redflag
    """
    return redflags_controller.update_redflag(redflag_id)


@redflags.route("/red-flags/<int:redflag_id>", methods=["GET"])
@jwt_required
def get_redflag(redflag_id):
    """
    api endpoint to fetch a single redflag
    """
    return redflags_controller.fetch_redflag(redflag_id)


@redflags.route("/red-flags/<int:redflag_id>", methods=["DELETE"])
@jwt_required
def delete_redflag(redflag_id):
    """
    api endpoint to delete a redflag
    """
    return redflags_controller.delete_a_redflag(redflag_id)
