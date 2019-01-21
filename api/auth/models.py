"""
user models
"""

import re
import uuid
import datetime


class User:
    """
    A class used to represent a User.

    ...

    Attributes
    ----------

    Methods
    -------
    
    """

    user_id = 1

    def __init__(self, firstname, lastname, othernames, username, email, password, phone_number):
        """
        initialize user attributes
        """
        self.user_id = str(uuid.uuid4())
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.username = username
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.is_admin = False
        self.created_on = datetime.datetime.now()

    # def validate_user_input(self):
    #     """
    #     validates user input
    #     returns: error message
    #     """
    #     if not self.username or self.username.isspace():
    #         return "Username field cannot be left empty."
    #     if not self.email or self.email.isspace():
    #         return "Email field cannot be left empty."
    #     if not self.password or self.password.isspace():
    #         return "Password field cannot be left empty."
    #     if len(self.password) < 6:
    #         return "Password too short, must be atleast 6 characters or more."
    #     if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
    #         return "Enter a valid email address."

    # def validate_base_input(self):
    #     """
    #     validates user base input
    #     returns: error message
    #     """
    #     if not self.base.firstname or self.base.firstname.isspace():
    #         return "Firstname field cannot be left empty."
    #     if not self.base.lastname or self.base.lastname.isspace():
    #         return "Lastname field cannot be left empty."
    #     if not self.base.othernames or self.base.othernames.isspace():
    #         return "Othernames field cannot be left empty."
    #     if not self.base.phone_number or self.base.phone_number.isspace():
    #         return "Phone number field cannot be left empty."

    @property
    def to_json(self):
        """
        returns user data in json serializable format
        """
        return {
            "id": self.user_id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othernames": self.othernames,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "phone_number": self.phone_number
        }
