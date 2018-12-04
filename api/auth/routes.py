from flask import jsonify, request
from api.auth import api
from api.auth.models import User, BaseUser
from api.auth.utilities import UserValidation
from db.database import UsersDb

users = UsersDb()
validation = UserValidation()


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
        })
    users.add_user(user)
    return jsonify({
        "status": "User successfully created.",
        "data": user.to_json() 
    }), 201


@api.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    current_user = users.find_by_username(username)
    if not current_user:
        return jsonify({"error": "User does not exist."}), 200
    check_credentials = users.user_login(username, password)
    if check_credentials:
        return jsonify({"status": "Successfully logged in."}), 200
    return jsonify({"error": "Invalid Credentials!"}), 400 