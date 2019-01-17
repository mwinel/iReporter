from flask import Blueprint

api = Blueprint('redflags', __name__)

from api.redflags import routes
