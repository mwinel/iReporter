"""
user models
"""


class User:
    """
    A class used to represent a User.

    ...

    Attributes
    ----------
    
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
        self.is_admin = False
