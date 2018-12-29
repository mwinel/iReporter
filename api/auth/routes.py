from api.auth import api
from api.auth.controllers import UserController

user_controller = UserController()

@api.route("/signup", methods=['POST'])
def signup():
    return user_controller.create_user()