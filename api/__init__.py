"""
create api package
"""
import datetime
from flask import Flask, jsonify
from api.index.routes import index as index_blueprint
from api.auth.routes import auth as auth_blueprint
from api.errors.request_errors import RequestError

app = Flask(__name__)

# Request exceptions
app.errorhandler(404)(RequestError.not_found)
app.errorhandler(405)(RequestError.method_not_allowed)

# Register blueprints
app.register_blueprint(index_blueprint, url_prefix='/api/v2')
app.register_blueprint(auth_blueprint, url_prefix='/api/v2')
