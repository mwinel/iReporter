import re
from api.auth.models import User


class UserValidation:

    def validate_user_input(self, username, email, password):
        if not username or username.isspace():
            return "Username field cannot be left empty."
        elif not email or email.isspace():
            return "Email field cannot be left empty."
        elif not password or password.isspace():
            return "Password field cannot be left empty."
        elif len(password) < 6:
            return "Password too short."
        elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
            return "Enter a valid email address."

    def validate_base_input(self, firstname, lastname, othernames, phoneNumber):
        if not firstname or firstname.isspace():
            return "Firstname field cannot be left empty."
        elif not lastname or lastname.isspace():
            return "Lastname field cannot be left empty."
        elif not othernames or othernames.isspace():
            return "Othernames field cannot be left empty."
        elif not phoneNumber or phoneNumber.isspace():
            return "Phone number field cannot be left empty."        