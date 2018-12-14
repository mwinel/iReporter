from flask import jsonify, request, make_response
from flask_jwt_extended import create_access_token
from api.auth.models import User, BaseUser
from api.auth.utilities import UserValidation
from db.database import UsersDb

users = UsersDb()
validation = UserValidation()


class UserController:

    def create_user(self):
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
        error = validation.validate_user_input(username, email, password)
        if error:
            return jsonify({"error": error}), 400
        base_error = validation.validate_base_input(firstname, lastname, 
                                                    othernames, phoneNumber)
        if base_error:
            return jsonify({"error": base_error}), 400
        user_exists = users.find_by_username(username)
        if user_exists:
            return jsonify({
                "error": "User with username '{}' already exists."
                .format(username)
            }), 202
        users.add_user(user)
        access_token = create_access_token(identity=username)
        return jsonify({
            "status": "User successfully created.",
            "data": user.to_json,
            "access_token": access_token 
        }), 201

    def find_user(self, username):
        user = users.find_by_username(username)
        return user

    def check_login_credentials(self, username, password):
        user = users.user_login(username, password)
        return user  

    def get_all_users(self):
        all_users = [i.to_json for i in users.get_all_users()]
        if not all_users:
            return jsonify({
                "error": "Sorry! No users were found.",
            }), 200
        return jsonify({
            "status": "success",
            "Users": all_users
        }), 200