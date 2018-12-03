from flask import jsonify, request
from api.auth import api
from api.auth.models import User, BaseUser
from db.database import UsersDb

users = UsersDb()

@api.route("/signup", methods=['POST'])
def signup():
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
    error = user.validate_input()
    if error:
        return jsonify({"error": error}), 400
    base_error = user.base.validate_base_input()
    if base_error:
        return jsonify({"error": base_error}), 400
    user_exists = users.find_by_username(username)
    if user_exists:
        return jsonify({
            "error": "User with username '{}' already exists."
            .format(username)
        })
    users.add_user(user)
    return jsonify({
        "status": "User successfully created.",
        "data": user.to_json() 
    }), 201