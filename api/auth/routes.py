"""
user auth routes
"""
from flask import Blueprint
from api.auth.controllers import UserController
from api.auth.helpers import token_required, is_admin

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
@is_admin
def get_users():
    """
    api endpoint to return users
    only the admin can view users
    """
    return user_controller.get_users()


@auth.route("/users/<int:user_id>/status", methods=['PATCH'])
@is_admin
def update_admin_status(user_id):
    """
    api endpoint to update an user status
    """
    return user_controller.edit_admin_status(is_admin, user_id)
