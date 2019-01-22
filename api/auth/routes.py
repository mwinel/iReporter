"""
user auth routes
"""
from flask import Blueprint
from api.auth.controllers import UserController

auth = Blueprint('auth', __name__)
user_controller = UserController()


@auth.route("/auth/signup", methods=['POST'])
def signup():
    """
    api endpoint to signup a user
    """
    return user_controller.create_user()
