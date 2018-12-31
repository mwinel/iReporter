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
def get_users():
    return user_controller.get_all_users()