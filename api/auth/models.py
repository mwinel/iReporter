import datetime
import re
import jwt
from api import app, bycrypt


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
        self.password = bycrypt.generate_password_hash(
            password
        ).decode()
        self.isAdmin = False

    def password_is_valid(self, password):
        return bycrypt.check_password_hash(self.password, password)

    def encode_auth_token(self, username):
        # generates auth token
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=200),
                'iat': datetime.datetime.utcnow(),
                'sub': username
            }
            return jwt.encode(
                payload,
                app.config['SECRET_KEY'],
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        # decodes auth token
        try:
            payload = jwt.decode(auth_token, app.config['SECRET_KEY'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return "Signature expired, please login again."
        except jwt.InvalidTokenError:
            return "Invalid Token, please login again."

    def validate_user_input(self):
        if not self.username or self.username.isspace():
            return "Username field cannot be left empty."
        elif not self.email or self.email.isspace():
            return "Email field cannot be left empty."
        elif not self.password or self.password.isspace():
            return "Password field cannot be left empty."
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