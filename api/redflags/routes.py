from flask import request, jsonify
from flask_jwt_extended import jwt_required
from api.redflags import api
from api.redflags.controllers import RedFlagsController
from api.auth.models import User

redflags_controller = RedFlagsController()

@api.route("/red-flags", methods=['POST'])
@jwt_required
def create_redflag():
    return redflags_controller.create_redflag()

@api.route("/red-flags", methods=["GET"])
@jwt_required
def get_redflags():
    return redflags_controller.fetch_all_redflags()      