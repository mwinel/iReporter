from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from api.index import api as index_blueprint
from api.auth import api as auth_blueprint
from api.redflags import api as redflags_blueprint
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
    """
    return jsonify({
        "status": 401,
        "message": "The token has expired, please login again."
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(callback):
    """
    a callback function called when an invalid token
    trys to access a protected api endpoint
    """
    return jsonify({
        "status": 401,
        "message": "Invalid token, please login again."
    }), 401


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    """
    a callback function called when a request with no
    JWT trys to access a protected api endpoint
    """
    return jsonify({
        "status": 401,
        "message": "Missing Authorization Header."
    }), 401


# Request exceptions
app.errorhandler(404)(RequestError.not_found)
app.errorhandler(405)(RequestError.method_not_allowed)

# Register blueprints
app.register_blueprint(index_blueprint, url_prefix='/api/v1')
app.register_blueprint(auth_blueprint, url_prefix='/api/v1/auth')
app.register_blueprint(redflags_blueprint, url_prefix='/api/v1')
