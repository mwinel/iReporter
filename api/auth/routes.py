from api.auth import api
from api.auth.controllers import UserController

user_controller = UserController()


@api.route("/signup", methods=['POST'])
def signup():
    """
    api endpoint to signup a user
    """
    return user_controller.create_user()


@api.route("/login", methods=['POST'])
def login():
    """
    api endpoint to login a user
    """
    return user_controller.user_login()
