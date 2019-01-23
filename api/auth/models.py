"""
user models
"""
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
