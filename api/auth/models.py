"""
user models
"""
import re


class User:
    """
    A class used to represent a User.

    ...

    Attributes
    ----------
    firstname : str
        the first name of the user
    lastname : str
        the last name of the user
    othernames : str
        the other names of the user
    username : str
        the username of the user
    email : str
        the email of the user
    password : str
        the password of the user
    phone_number : str
        the phone number of the user

    Methods
    -------
    validate_user_email
        validates user email
    validate_user_password
        validates user password
    validate_user_input
        validates user input

    """

    def __init__(self, firstname, lastname, othernames, username, email, password, phone_number):
        """
        initialize user attributes
        """
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.username = username
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def validate_user_email(self):
        """
        validates user email
        returns: error message
        """
        if not self.email or self.email.isspace():
            return "Email field cannot be left empty."
        if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return "Enter a valid email address."

    def validate_user_password(self):
        """
        validates user password
        returns: error message
        """
        if not self.password or self.password.isspace():
            return "Password field cannot be left empty."
        if len(self.password) < 6:
            return "Password too short, must be atleast 6 characters or more."

    def validate_user_input(self):
        """
        validates user input
        returns: error message
        """
        if not self.username or self.username.isspace():
            return "Username field cannot be left empty."
        if not self.firstname or self.firstname.isspace():
            return "Firstname field cannot be left empty."
        if not self.lastname or self.lastname.isspace():
            return "Lastname field cannot be left empty."
        if not self.othernames or self.othernames.isspace():
            return "Othernames field cannot be left empty."
        if not self.phone_number or self.phone_number.isspace():
            return "Phone number field cannot be left empty."
       