from flask_jwt_extended import jwt_required
from api.auth import api
from api.auth.controllers import UserController

user_controller = UserController()


@api.route("/auth/signup", methods=['POST'])
def signup():
    """
    api endpoint to signup a user
    """
    return user_controller.create_user()


@api.route("/auth/login", methods=['POST'])
def login():
    """
    api endpoint to login a user
    """
    return user_controller.user_login()


@api.route("/users", methods=['GET'])
@jwt_required
def get_users():
    """
    api endpoint to return users
    """
    return user_controller.fetch_users()
