"""
user controller
"""
import datetime
from flask import request, jsonify, make_response
from db.database import DatabaseConnection
from api.auth.validators import UserValidations
from api.auth.helpers import encode_auth_token

db = DatabaseConnection()
user_validations = UserValidations()


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
        data = request.get_json(force=True)

        firstname = data['firstname']
        lastname = data['lastname']
        othernames = data['othernames']
        username = data['username']
        email = data['email']
        password = data['password']
        phone_number = data['phone_number']
        created_on = datetime.datetime.now()

        # validate user input
        validate_input = user_validations.validate_user_input(username, firstname, lastname,
                                                              othernames, phone_number)
        validate_email = user_validations.validate_user_email(email)
        validate_password = user_validations.validate_user_password(password)
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
                "error": "User already exists. Please login."
            }), 202
        add_user = db.insert_user_data(firstname, lastname, othernames, username, email,
                                       password, phone_number, created_on)
        auth_token = encode_auth_token(username).decode('utf-8')
        return jsonify({
            "status": 201,
            "message": "User successfully created.",
            "data": add_user,
            "access_token": auth_token
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
        user = db.check_login_credentials(username, password)
        if user:
            auth_token = encode_auth_token(username).decode('utf-8')
            response = {
                "status": 200,
                "message": "Successfully logged in.",
                "access_token": auth_token
            }
            return make_response(jsonify(response)), 200
        return jsonify({
            "status": 401,
            "error": "Invalid Credentials!",
        }), 401

    def get_users(self):
        users = db.fetch_all('users')
        return jsonify(users=users), 200
