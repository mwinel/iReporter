import re
import datetime
from passlib.apps import custom_app_context as pwd_context


class BaseUser:

    user_id = 1

    def __init__(self, firstname, lastname, othernames, phoneNumber):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.phoneNumber = phoneNumber
        self.registered = datetime.datetime.now()
        self.id = BaseUser.user_id
        BaseUser.user_id += 1  
         

class User:

    def __init__(self, base, username, email, password):
        self.base = base
        self.username = username
        self.email = email
        self.password = password
        self.isAdmin = False

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def validate_user_input(self):
        if not self.username or self.username.isspace():
            return "Username field cannot be left empty."
        elif not self.email or self.email.isspace():
            return "Email field cannot be left empty."
        elif not self.password or self.password.isspace():
            return "Password field cannot be left empty."
        elif len(self.password) < 6:
            return "Password too short, must be atleast 6 characters or more."
        elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return "Enter a valid email address."

    def validate_base_input(self):
        if not self.base.firstname or self.base.firstname.isspace():
            return "Firstname field cannot be left empty."
        elif not self.base.lastname or self.base.lastname.isspace():
            return "Lastname field cannot be left empty."
        elif not self.base.othernames or self.base.othernames.isspace():
            return "Othernames field cannot be left empty."
        elif not self.base.phoneNumber or self.base.phoneNumber.isspace():
            return "Phone number field cannot be left empty." 

    @property
    def to_json(self):
        return {
            "id": self.base.id,
            "firstname": self.base.firstname,
            "lastname": self.base.lastname,
            "othernames": self.base.othernames,
            "username": self.username,
            "registered": self.base.registered,
            "admin": self.isAdmin,
            "email": self.email,
            "password": self.password, 
            "phoneNumber": self.base.phoneNumber
        }