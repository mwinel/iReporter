from flask import Blueprint

api = Blueprint('index', __name__)

from api.index import index 