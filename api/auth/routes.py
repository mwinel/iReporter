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

@auth.route("/users/<int:user_id>", methods=['GET'])
@token_required
def get_user(current_user, user_id):
    """
    api endpoint to return a single user
    """
    return user_controller.fetch_user(user_id)

@auth.route("/users/<username>", methods=['GET'])
@token_required
def get_user_by_username(current_user, username):
    """
    api endpoint to return a single user by username
    """
    return user_controller.fetch_user_by_username(username)
