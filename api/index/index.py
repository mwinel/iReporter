from flask import jsonify
from api.index import api


@api.route("/", methods=['GET'])
@api.route("/index", methods=['GET'])
def index():
    return jsonify({
        "status": 200,
        "message": "Welcome to iReporter.",
        "author": "Nelson Mwirumubi",
        "description": "ADC Cohort 15"
    }), 200
