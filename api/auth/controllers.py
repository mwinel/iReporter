from flask import request, jsonify
from api.auth.models import User, BaseUser
from db.database import UsersDb

users = UsersDb()

def get_user_by_username(username):
    user = users.find_user_by_username(username)
    return user


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

        error = user.validate_user_input()
        base_error = user.validate_base_input()
        if error:
            return jsonify({"error": error}), 400
        if base_error:
            return jsonify({"error": base_error}), 400
        user_exists = users.find_user_by_username(username)
        if user_exists:
            return jsonify({
                "error": "User already exists. Please login."
            }), 202

        users.add_user(user)
        # generate auth token
        auth_token = user.encode_auth_token(username)
        return jsonify({
            "status": "User successfully created.",
            "data": user.to_json,
            "auth_token": auth_token.decode('UTF-8')
        }), 201

    def user_login(self):
        data = request.get_json()
        try:
            user = get_user_by_username(username=data.get('username'))
            auth_token = user.encode_auth_token(user.username)
            if auth_token:
                response = {
                    "status": "Successfully logged in.",
                    "auth_token": auth_token.decode('UTF-8')
                }
                return jsonify(response), 200
        except Exception as e:
            print(e)
            response = {
                "status": "Invalid credentials, Please try again."
            }
            return jsonify(response), 500

    def get_all_users(self):
        all_users = [i.to_json for i in users.get_all_users()]
        if all_users:
            return jsonify({
                "status": "success",
                "Users": all_users
            }), 200
        return jsonify({
            "error": "Sorry! No users were found.",
        }), 200