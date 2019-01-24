"""
helper functions
"""
import datetime
from functools import wraps
import jwt
from flask import request, jsonify
from db.database import DatabaseConnection

db = DatabaseConnection()


def get_user(username):
    user = db.get_by_argument('users', 'username', username)
    return user


def encode_auth_token(username):
    """
    generates the auth token
    param: username
    returns: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=1500),
            'iat': datetime.datetime.utcnow(),
            'sub': username
        }
        return jwt.encode(
            payload,
            'some-boy-just-went-mad-coding',
            algorithm='HS256'
        )
    except Exception as e:
        return e


def token_required(f):
    """
    decorator to protect api endpoints
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return jsonify({
                "status": 401,
                "error": "Missing Authorization Header"
            }), 401
        auth_token = request.headers['Authorization']
        try:
            identinty = jwt.decode(
                auth_token, 'some-boy-just-went-mad-coding')
            current_user = get_user(username=identinty['sub'])
        except jwt.ExpiredSignatureError:
            return jsonify({
                "status": 401,
                "error": "Token expired. Please login again."
            }), 401
        except jwt.InvalidSignatureError:
            return jsonify({
                "status": 401,
                "error": "Invalid Token. Please login again."
            }), 401
        return f(current_user, *args, **kwargs)
    return decorated
