from flask import jsonify, request, make_response
from api.auth.models import User, BaseUser
from db.database import UsersDb

users = UsersDb()

def find_by_username(username):
    for user in users:
        if user.username == username:
            return user
    return None        

class UserController:

    def __init__(self):
        pass

    def create_user(self):
        data = request.get_json()

        firstname = data.get('firstname')
        lastname = data.get('lastname')
        othernames = data.get('othernames')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password') 
        phoneNumber = data.get('phoneNumber')
        user = User(BaseUser(firstname, lastname, othernames, phoneNumber),
                    username, email, password)
        error = user.validate_input()
        if error:
            return jsonify({"error": error})
        users.add_user(user)
        return jsonify({
            "status": "User successfully created.",
            "data": user.to_json() 
        })

    def get_user_by_username():
        user = users.select(find_by_username)
        if user is None:
            return jsonify({"status": "User not found"})
        return user.to_json()    
