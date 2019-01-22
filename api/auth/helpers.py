"""
helper functions
"""
import datetime
from functools import wraps
import jwt
from flask import request, jsonify


def encode_auth_token(username):
    """
    generates the auth token
    param: username
    returns: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=15),
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

def decode_auth_token(auth_token):
    """
    decodes auth token
    param: auth_token
    returns: string
    """
    try:
        payload = jwt.decode(auth_token, 'some-boy-just-went-mad-coding', algorithms='HS256')
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Token Expired. Please login again.'
    except jwt.InvalidTokenError:
        return 'Invalid Token. Please login again.'

def token_required(f):
    """
    decorator function to protect api endpoints
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                return "Provide a valid token"
        if not auth_token:
            return "Token is missing"
        try:
            decode_token = decode_auth_token(auth_token)
        except:
            message = "Invalid token"
            if isinstance(decode_token, str):
                message = decode_token
            return jsonify(message)

        return f(*args, **kwargs)
    return decorated
