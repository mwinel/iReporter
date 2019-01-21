"""
user auth routes
"""

from flask import Blueprint
# from flask_jwt_extended import jwt_required
from api.auth.controllers import UserController

auth = Blueprint('auth', __name__)
user_controller = UserController()


@auth.route("/auth/signup", methods=['POST'])
def signup():
    """
    api endpoint to signup a user
    """
    return user_controller.create_user()


# @auth.route("/auth/login", methods=['POST'])
# def login():
#     """
#     api endpoint to login a user
#     """
#     return user_controller.user_login()


# @auth.route("/users", methods=['GET'])
# @jwt_required
# def get_users():
#     """
#     api endpoint to return users
#     """
#     return user_controller.fetch_users()
