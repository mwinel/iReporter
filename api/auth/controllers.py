"""
user controller
"""
import datetime
from flask import request, jsonify
from api.auth.models import User, BaseUser
from db.database import DatabaseConnection

db = DatabaseConnection()


class UserController:
    """
    A class used to represent the user controller

    ...

    Methods
    ----------
    create_user
        creates user account
    user_login
        logs in a registered user
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
        phone_number = data.get('phone_number')
        created_on = datetime.datetime.now()

        user = User(BaseUser(firstname, lastname, othernames, phone_number), username,
                    email, password)
        # validate user
        validate_input = user.validate_user_input()
        validate_email = user.validate_user_email()
        validate_password = user.validate_user_password()
        if validate_input:
            return jsonify({
                "status": 400,
                "error": validate_input
            }), 400
        if validate_email:
            return jsonify({
                "status": 400,
                "error": validate_email
            }), 400
        if validate_password:
            return jsonify({
                "status": 400,
                "error": validate_password
            }), 400
        # check if user exists
        user_exists = db.get_by_argument('users', 'username', username)
        if user_exists:
            return jsonify({
                "status": 202,
                "message": "User already exists. Please login."
            }), 202
        add_user = db.insert_user_data(firstname, lastname, othernames, username, email,
                                       password, phone_number, created_on)
        return jsonify({
            "status": 201,
            "message": "User successfully created.",
            "data": add_user
        }), 201

    def user_login(self):
        """
        logs in a registered user
        """
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        current_user = db.get_by_argument('users', 'username', username)
        if not current_user:
            return jsonify({
                "status": 200,
                "error": "User does not exist. Please signup."
            }), 200
        check_user = db.check_login_credentials(username, password)
        if check_user:
            return jsonify({
                "status": 200,
                "message": "Successfully logged in."
            }), 200
        return jsonify({
            "status": 401,
            "error": "Invalid Credentials!"
        }), 401
