"""
This file lets python treat the api directory as a package.

- creates a flask instance
- creates the jwt instance
- handles auth exception error for jwt authentication
- handles url request exceptions and,
- registers the api blueprints
"""

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from api.index.routes import index as index_blueprint
from api.auth.routes import auth as auth_blueprint
from api.redflags.routes import redflags as redflags_blueprint
from api.errors.request_errors import RequestError

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = "you-own-your-own"


# Auth exceptions
@jwt.expired_token_loader
def expired_token_callback():
    """
    a callback function called when an expired token
    trys to access a protected api endpoint
    returns: error message
    """
    return jsonify({
        "status": 401,
        "message": "The token has expired, please login again."
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(invalid_token_msg):
    """
    a callback function called when an invalid token
    trys to access a protected api endpoint
    returns: invalid_token_msg
    """
    invalid_token_msg = "Invalid token, please login again."
    return jsonify({
        "status": 401,
        "message": invalid_token_msg
    }), 401


@jwt.unauthorized_loader
def unauthorized_callback(unauthorized_msg):
    """
    a callback function called when a request with no
    JWT trys to access a protected api endpoint
    returns: unauthorized_msg
    """
    unauthorized_msg = "Missing Authorization Header."
    return jsonify({
        "status": 401,
        "message": unauthorized_msg
    }), 401


# Request exceptions
app.errorhandler(404)(RequestError.not_found)
app.errorhandler(405)(RequestError.method_not_allowed)

# Register blueprints
app.register_blueprint(index_blueprint, url_prefix='/api/v1')
app.register_blueprint(auth_blueprint, url_prefix='/api/v1')
app.register_blueprint(redflags_blueprint, url_prefix='/api/v1')
