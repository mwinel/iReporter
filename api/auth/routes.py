from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from api.auth import api
from api.auth.controllers import UserController

user_controller = UserController()


@api.route("/signup", methods=['POST'])
def signup():
    return user_controller.create_user()
    

@api.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    current_user = user_controller.find_user(username)
    if not current_user:
        return jsonify({"error": "User does not exist."}), 200
    check_credentials = user_controller.check_login_credentials(
        username, password)
    if check_credentials:
        access_token = create_access_token(identity=username)
        return jsonify({
            "status": "Successfully logged in.",
            "access_token": access_token
        }), 200
    return jsonify({"error": "Invalid Credentials!"}), 401


@api.route("/users", methods=['GET'])
@jwt_required
def fetch_users():
    current_user = get_jwt_identity()
    return user_controller.get_all_users()     