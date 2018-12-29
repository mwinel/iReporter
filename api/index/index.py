from flask import jsonify
from api.index import api

@api.route("/index", methods=['GET'])
def index():
    return jsonify({"message": "Welcome to iReporter."}), 200
