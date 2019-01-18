"""
index routes
"""

from flask import Blueprint
from flask import jsonify

index = Blueprint('index', __name__)


@index.route("/", methods=['GET'])
@index.route("/index", methods=['GET'])
def welcome():
    """
    returns a welcome message
    """
    return jsonify({
        "status": 200,
        "message": "Welcome to iReporter.",
        "author": "Nelson Mwirumubi",
        "description": "ADC Cohort 15"
    }), 200
