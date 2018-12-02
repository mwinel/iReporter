from api.auth import api
from api.auth.controllers import UserController

user_controllers = UserController()

@api.route("/signup", methods=['POST'])
def signup():
    return user_controllers.create_user(), 201
