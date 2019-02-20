"""
user validations class
"""
import re


class UserValidations:
    """
    A class used to represent user validations
    """
    def validate_user_email(self, email):
        """
        validates user email
        returns: error message
        """
        if not email or email.isspace():
            return "Email field cannot be left empty."
        if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
            return "Enter a valid email address."

    def validate_user_password(self, password):
        """
        validates user password
        returns: error message
        """
        if not password or password.isspace():
            return "Password field cannot be left empty."
        if len(password) < 6:
            return "Password too short, must be atleast 6 characters or more."

    def validate_user_input(self, username, firstname, lastname, phone_number):
        """
        validates user input
        returns: error message
        """
        if not username or username.isspace():
            return "Username field cannot be left empty."
        if not firstname or firstname.isspace():
            return "Firstname field cannot be left empty."
        if not lastname or lastname.isspace():
            return "Lastname field cannot be left empty."
        if not phone_number or phone_number.isspace():
            return "Phone number field cannot be left empty."
