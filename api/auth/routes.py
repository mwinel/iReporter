from flask_jwt_extended import jwt_required
from api.auth import api
from api.auth.controllers import UserController

user_controller = UserController()

@api.route("/signup", methods=['POST'])
def signup():
    return user_controller.create_user()

@api.route("/login", methods=['POST'])
def login():
    return user_controller.user_login()

@api.route("/users", methods=['GET'])
@jwt_required
def get_users():
    return user_controller.fetch_all_users()