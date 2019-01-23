"""
user auth routes
"""
from flask import Blueprint
from api.auth.controllers import UserController
from api.auth.helpers import token_required

auth = Blueprint('auth', __name__)
user_controller = UserController()


@auth.route("/auth/signup", methods=['POST'])
def signup():
    """
    api endpoint to signup a user
    """
    return user_controller.create_user()


@auth.route("/auth/login", methods=['POST'])
def login():
    """
    api endpoint to login a user
    """
    return user_controller.user_login()


@auth.route("/users", methods=['GET'])
@token_required
def get_users(current_user):
    """
    api endpoint to return users
    """
    return user_controller.get_users()
