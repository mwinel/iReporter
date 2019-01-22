"""
user controller
"""
import datetime
from flask import request, jsonify
from db.database import DatabaseConnection

db = DatabaseConnection()


class UserController:
    """
    A class used to represent the user controller

    ...

    Methods
    ----------
    create_user
        creates user account
    """

    def create_user(self):
        """
        creates user account
        """
        data = request.get_json()
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        othernames = data.get('othernames')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        phone_number = data.get('phone_number')
        created_on = datetime.datetime.now()
        user = db.insert_user_data(firstname, lastname, othernames, username, email,
                            password, phone_number, created_on)
        return jsonify({
            "status": 201,
            "message": "User successfully created.",
            "data": user
        }), 201
