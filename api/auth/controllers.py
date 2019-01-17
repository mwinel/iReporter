from flask import request, jsonify
from flask_jwt_extended import create_access_token
from api import jwt
from api.auth.models import User, BaseUser
from db.database import UsersDb

users = UsersDb()

def get_user_by_username(username):
    """
    gets a user by username
    returns: user
    """
    user = users.find_user_by_username(username)
    return user

def check_login_credentials(username, password):
    """
    checks for user login credentials
    returns: user
    """
    user = users.check_user(username, password)
    return user 


class UserController:
    """
    A class used to represent the user controller

    ...

    Methods
    ----------
    create_user
        creates user account
    user_login
        logs in the user given the username and password
    """

    def create_user(self):
        """
        creates user account
        """
        data = request.get_json()
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        othernames = data.get('othernames')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password') 
        phoneNumber = data.get('phoneNumber')

        user = User(BaseUser(firstname, lastname, othernames, phoneNumber),
                    username, email, password)
        # validate user
        error = user.validate_user_input()
        base_error = user.validate_base_input()
        if error:
            return jsonify({
                "status": 400,
                "error": error
            }), 400
        if base_error:
            return jsonify({
                "status": 400,
                "error": base_error
            }), 400
        # check if user exists
        user_exists = users.find_user_by_username(username)
        if user_exists:
            return jsonify({
                "status": 202,
                "message": "User already exists. Please login."
            }), 202
        user.hash_password(password)
        users.add_user(user)
        auth_token = create_access_token(username)
        return jsonify({
            "status": 201,
            "message": "User successfully created.",
            "data": user.to_json,
            "auth_token": auth_token
        }), 201

    def user_login(self):
        """
        logs in the user
        """
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        current_user = get_user_by_username(username)
        if not current_user:
            return jsonify({
                "status": 200,
                "error": "User does not exist."
            }), 200
        # check for login credentials  
        check_credentials = check_login_credentials(username, password)
        if check_credentials:
            auth_token = create_access_token(identity=username)
            return jsonify({
                "status": 200,
                "message": "Successfully logged in.",
                "access_token": auth_token
            }), 200
        return jsonify({
            "status": 401,
            "error": "Invalid Credentials!"
        }), 401