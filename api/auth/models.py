"""
user models
"""
import re


class BaseUser:
    """
    A class used to represent a BaseUser.

    ...

    Attributes
    ----------
    firstname : str
        the first name of the user
    lastname : str
        the last name of the user
    othernames : str
        the other names of the user
    phone_number : str
        the phone number of the user
    """

    def __init__(self, firstname, lastname, othernames, phone_number):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.phone_number = phone_number


class User:
    """
    A class used to represent a User.

    ...

    Attributes
    ----------
    base : base
        used to inherit BaseUser properties
    username : str
        the username of the user
    email : str
        the email of the user
    password : str
        the password of the user

    Methods
    -------
    validate_user_email
        validates user email
    validate_user_password
        validates user password
    validate_user_input
        validates user input

    """

    def __init__(self, base, username, email, password):
        """
        initialize user attributes
        """
        self.base = base
        self.username = username
        self.email = email
        self.password = password

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
        if not self.base.firstname or self.base.firstname.isspace():
            return "Firstname field cannot be left empty."
        if not self.base.lastname or self.base.lastname.isspace():
            return "Lastname field cannot be left empty."
        if not self.base.othernames or self.base.othernames.isspace():
            return "Othernames field cannot be left empty."
        if not self.base.phone_number or self.base.phone_number.isspace():
            return "Phone number field cannot be left empty."
       